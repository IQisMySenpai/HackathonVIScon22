import bson.errors
from fastapi import FastAPI, Response, Query
from fastapi.staticfiles import StaticFiles

from typing import List

from courses import *
from db import mongo

app = FastAPI()
api = FastAPI()


@api.get("/tags")
def get_tags(response: Response):
    return list_tags(mongo, response)


@api.post("/tags")
def post_tag(tag: Tag, response: Response):
    return create_tag(mongo, response, tag)


# @api.get("/lecturers")
# def read_lecturers(response: Response):
#    return list_lecturers(mongo, response)

@api.get("/courses")
def read_courses(response: Response, course_id: Union[str, None] = None, page: int = 0):

    if course_id is not None:
        try:
            course_id = ObjectId(course_id)
        except (bson.errors.InvalidId, ValueError):
            return pack_response(response, 400, "invalid id")

    return list_courses(mongo, response, course_id, page)

@api.get("/query/courses")
def read_courses(response: Response, query: str = None,  tags: str = None, page: int = 0):

    if tags is not None:
        tags = tags.split(',')
        try:
            tags = [ObjectId(tag) for tag in tags]
        except (bson.errors.InvalidId, ValueError):
            return pack_response(response, 400, "Invalid Tags")

    return query_courses(mongo, response, query, tags, page)

@api.post("/courses/review")
def post_review(review: Review, response: Response):

    if review.course_id is None:
        return pack_response(response, 400, "missing course id")
    else:
        try:
            review.course_id = ObjectId(review.course_id)
        except (bson.errors.InvalidId, ValueError):
            return pack_response(response, 400, "Invalid course id")

    return create_review(mongo, response, review)

@api.post("/courses")
def post_course(course: Course, response: Response):
    return create_course(mongo, response, course)


@api.post("/test-login")
def post_test_login(request: Request, response: Response):
    return test_login(request, response)


app.mount("/api", api)
app.mount("/", StaticFiles(directory="../Webinterface", html=True), name="WebInterface")
