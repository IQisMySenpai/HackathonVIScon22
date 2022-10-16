from fastapi import Response, Request, Query
from bson.objectid import ObjectId
from mongo_api import *
from api_common import *
from structs import *
from typing import List
import jwt
import jwt.exceptions as jex

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

    return pack_response(response, 200, "ok", {"courses": Course.out(course_list)})


def list_courses(db: MongoAPI, response: Response, page):
    courses = db.find("courses", skip=20 * page, limit=20)
    return load_courses_helper(courses, db, response)


def query_courses(db: MongoAPI, response: Response, query: str, tags: List[str] = Query(default=None), page: int = 0):

    # name
    # mongo id
    # readable-id
    # description

    if query is not None:
        regex = ".*" + query + ".*"
        regex = regex.replace(" ", ".*")

    if tags is not None:
        tags = [ObjectId(tag) for tag in tags]

    print(tags)
    courses = None
    if query is not None and tags is None:
        courses = list(db.collection("courses").find({"title": {"$regex": regex, '$options': 'i'}}).skip(20*page).limit(20))
    elif query is not None and tags is not None:
        courses = list(db.collection("courses").find({"title": {"$regex": regex, '$options': 'i'}, "tags._id": {"$in": tags}}).skip(20*page).limit(20))
    elif query is None and Tag is not None:
        courses = list(db.collection("courses").find({"tags._id": {"$in": tags}}).skip(20*page).limit(20))
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


def load_lecturer_for_courses(db: MongoAPI, courses: List[Course]):
    for course in courses:
        if course.lecturers is None:
            continue
        course.lecturers = Lecturer.from_db(db.find("professors", find_all_id_query(course.lecturers), limit=10))


def test_login(request: Request, response: Response):
    id_token = request.headers.get("Authorization")
    print(id_token)

    if id_token is None:
        return pack_response(response=response, status=401, message="Login required")

    try:
        user_info = jwt.decode(jwt=id_token, key=key, algorithms=["RS256"], options={"verify_aud": False}), False
    except jex.InvalidSignatureError:
        return pack_response(response=response, status=401, message="Invalid Authorisation, Login Again"), False
    except jex.ExpiredSignatureError:
        return pack_response(response=response, status=401, message="Expired Authorisation, Login Again"), False

    return user_info, True


