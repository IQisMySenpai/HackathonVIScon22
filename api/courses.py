from fastapi import Response, Query
from bson.objectid import ObjectId
from mongo_api import *
from api_common import *
from structs import *
from typing import List

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

def load_courses_helper(courses, db: MongoAPI, response: Response):
    if len(courses) == 0:
        return pack_response(response, 204, "No courses found.")

    courses = Course.from_db(courses)
    load_lecturer_for_courses(db, courses)

    return pack_response(response, 200, "ok", {"courses": Course.out(courses)})
def list_courses(db: MongoAPI, response: Response, page):
    courses = db.find("courses", skip=20 * page, limit=20)
    return load_courses_helper(courses, db, response)

def query_courses(db: MongoAPI, response: Response, query: str, tags: List[str] = Query(default=None), page: int = 0):

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

def load_lecturer_for_courses(db: MongoAPI, courses: list[Course]):
    for course in courses:
        if course.lecturers is None:
            continue
        course.lecturers = Lecturer.from_db(db.find("professors", find_all_id_query(course.lecturers), limit=10))


