import bson.objectid
from fastapi import Response, Request, Query
from bson.objectid import ObjectId
from mongo_api import *
from api_common import *
from structs import *
from typing import List
import jose.jwt as jwt
import jose.exceptions as jex
import os

# ======================================================================================================================
# Globals
# ======================================================================================================================

key = (
    b'-----BEGIN PUBLIC KEY-----\n'
    b'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtP+L+6HuC6g/d6xJxjdS\n'
    b'gTMYusm9HehmbfB/NKbjKPBVQ7ebnoMuvPDI8MMRsQS4/vx5bdkofxD1qresiCJu\n'
    b'kBFZoZ25r7/WyPLv09VgaHiwevO+Ygy7pb2aySO9ByDrWTfwj2mN4N80GyNXJbH4\n'
    b'52vYXNdETPmBpawEp5O4uRs08tqxMYq0C4mWSTnAWZazuijmfA0FXUi7juVUEqtq\n'
    b'fJYGMWtj5nEOhjvv3u7uNpMPRjz/pk+Ffb+qQZ6PBymCx+jrBm1ThEtRAeSEauXl\n'
    b'xHvsfsCEt8fAr1YUR9Xu/16VbA/phZ5gzSrv8D+wdFdEB4BqvI0PpR1TJHzvdD82\n'
    b'JQIDAQAB\n'
    b'-----END PUBLIC KEY-----\n')


def list_tags(db: MongoAPI, response: Response):
    tags = db.find("tags")

    if len(tags) == 0:
        return pack_response(response, 204, "No tags found.")

    return pack_response(response, 200, "ok", {"tags": Tag.out(Tag.from_db(tags))})


def create_tag(db: MongoAPI, response: Response, tag: Tag):
    tag.id = db.insert_one("tags", tag.db_dict())

    if tag.id is None:
        return pack_response(response, 400, "Failed to create tag.")

    return pack_response(response, 200, "ok", {"id": tag.id.__str__()})


def list_lecturers(db: MongoAPI, response: Response):
    profs = db.find("professors")

    if len(profs) == 0:
        return pack_response(response, 204, "No Profs found.")

    return pack_response(response, 200, "ok", {"lecturers": Lecturer.out(Lecturer.from_db(profs))})


def load_courses_helper(courses: List[dict], db: MongoAPI, response: Response):
    if len(courses) == 0:
        return pack_response(response, 204, "No courses found.")

    course_list: List[Course] = Course.from_db(courses)
    load_lecturer_for_courses(db, course_list)
    filter_reported_reviews(course_list)

    return pack_response(response, 200, "ok", {"courses": Course.out(course_list)})


def list_courses(db: MongoAPI, response: Response, course_id: ObjectId, page: int):
    if course_id is None:
        courses = db.find("courses", skip=20 * page, limit=20)
    else:
        courses = db.find("courses", filter_dict={'_id': course_id}, limit=1)
    return load_courses_helper(courses, db, response)

def query_courses(db: MongoAPI, response: Response, query: str, tags: List[str] = None, page: int = 0):

    regex = None
    if query is not None:
        regex = ".*" + query + ".*"
        regex = regex.replace(" ", ".*")

    courses = None
    if query is not None and tags is None:
        courses = list(db.collection("courses").find({"title": {"$regex": regex, '$options': 'i'}}).skip(20*page).limit(20))
    elif query is not None and tags is not None:
        courses = list(db.collection("courses").find({"title": {"$regex": regex, '$options': 'i'}, "tags._id": {"$all": tags}}).skip(20*page).limit(20))
    elif query is None and Tag is not None:
        courses = list(db.collection("courses").find({"tags._id": {"$all": tags}}).skip(20*page).limit(20))
    else:
        return pack_response(response, 400, "Specify tags or query.")

    return load_courses_helper(courses, db, response)


def create_course(db: MongoAPI, response: Response, course: Course):

    # resolve tag data, resolve lecturers data
    if course.tags is not None:
        course.tags = Tag.from_db(db.find("tags", {'_id': {'$in': [ObjectId(tag.id) for tag in course.tags]}}))

    # check lecturers

    course.id = db.insert_one("courses", course.db_dict())

    if course.id is None:
        return pack_response(response, 400, "Failed to create course")

    return pack_response(response, 200, "ok", {"id": course.id.__str__()})

def create_review(db: MongoAPI, request: Request, response: Response, review: Review):

    data, logged = test_login(request, response)
    if not logged:
        return pack_response(response, 403, "sign in pls")

    print(data)
    review.author = data["preferred_username"]
    review.is_reported = False
    review.m_id = bson.objectid.ObjectId()
    review.date = time.time()

    count = db.update("courses", {'_id': review.course_id}, {
        '$push': {
            'reviews': review.db_dict()
        }
    })

    if count == 0:
        return pack_response(response, 400, "No course has been updated")

    if review.tags is not None:
        try:
            tags = [ObjectId(tag) for tag in review.tags]
        except (bson.objectid.InvalidId, ValueError):
            return pack_response(response, 200, "Ok, but tags were not added")

        fetched_tags: List[Tag] = Tag.from_db(db.find("tags", {'_id': {'$in': tags}}))
        # unsafe [0]ru2
        course: Course = Course.from_db(db.find("courses", {'_id': review.course_id}))[0]

        tag_ids = []
        if course.tags is not None:
            tag_ids = [tg.id for tg in course.tags]
        print(fetched_tags)
        print(course.tags)

        for tag in fetched_tags:
            do_add = True
            if tag.id not in tag_ids:
                db.update("courses", {'_id': course.m_id}, {'$push': {'tags': tag.db_dict()}})

    return pack_response(response, 200, "ok")

def flag_review(db: MongoAPI, request: Request, response: Response, course_id: ObjectId, review_id: ObjectId):

    data, logged = test_login(request, response)
    if not logged:
        return pack_response(response, 403, "sign in pls")

    username = data["preferred_username"]
    result = db.find_one("moderators", {'username': username})

    if result is None:
        return pack_response(response, 403, "forbidden?")

    count = db.update("courses", {"_id": course_id, "reviews._id": review_id}, {"$set": {'reviews.$.is_reported': True}})

    if count == 0:
        return pack_response(response, 400, "no review updated")

    return pack_response(response, 200, "ok")


def filter_reported_reviews(courses: List[Course]):
    for course in courses:
        if course.reviews is None:
            continue
        course.reviews = [review for review in course.reviews if not review.is_reported]

def calculate_average_rating(courses: List[Course]):
    ratings = []
    for course in courses:
        if course.reviews is None:
            continue
        avg = {}
        for review in course.reviews:
            if review.rating is None:
                continue
            for rating in review.rating:
                if rating.name not in avg:
                    avg[rating.name] = [rating.rating, 1]
                else:
                    avg[rating.name][0] += rating.rating
                    avg[rating.name][1] += 1

        result = []
        for k in avg.keys():
            result.append(avg[k][0] / avg[k][1])

        ratings.append(result)
    return ratings

def load_lecturer_for_courses(db: MongoAPI, courses: List[Course]):
    for course in courses:
        if course.lecturers is None:
            continue
        course.lecturers = Lecturer.from_db(db.find("professors", find_all_id_query(course.lecturers), limit=10))

def test_login(request: Request, response: Response):
    id_token = request.headers.get("Authorization")
    print(id_token)

    if id_token is None:
        return pack_response(response=response, status=401, message="Login required"), False

    # TODO this seems to be broken now with new dependencies.
    try:
        user_info = jwt.decode(jwt=id_token, key=key, algorithms=["RS256"], options={"verify_aud": False})
    except jex.InvalidSignatureError:
        return pack_response(response=response, status=401, message="Invalid Authorisation, Login Again"), False
    except jex.ExpiredSignatureError:
        return pack_response(response=response, status=401, message="Expired Authorisation, Login Again"), False

    return user_info, True


def get_lecturer_image(response: Response, vvz_id: int):
    folder = "../Webinterface/test_images"

    jpg = os.path.join(folder, f"{vvz_id}.jpg")
    png = os.path.join(folder, f"{vvz_id}.png")
    jpeg = os.path.join(folder, f"{vvz_id}.jpeg")
    gif = os.path.join(folder, f"{vvz_id}.gif")
    svg = os.path.join(folder, f"{vvz_id}.svg")

    if os.path.exists(jpg):
        return pack_response(response, 200, "Success", {"path": os.path.join("test_images", os.path.basename(jpg))})

    if os.path.exists(jpeg):
        return pack_response(response, 200, "Success", {"path": os.path.join("test_images", os.path.basename(jpeg))})

    if os.path.exists(png):
        return pack_response(response, 200, "Success", {"path": os.path.join("test_images", os.path.basename(png))})

    if os.path.exists(gif):
        return pack_response(response, 200, "Success", {"path": os.path.join("test_images", os.path.basename(gif))})

    if os.path.exists(svg):
        return pack_response(response, 200, "Success", {"path": os.path.join("test_images", os.path.basename(svg))})

    return pack_response(response, 404, "No Image found", {})


