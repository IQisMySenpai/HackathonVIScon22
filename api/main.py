from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles

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
def read_courses(response: Response, page: int = 0):
    return list_courses(mongo, response, page)

@api.get("/query/courses")
def read_courses(query: str, response: Response, page: int = 0):
    return query_courses(mongo, response, query, page)

@api.post("/courses")
def post_course(course: Course, response: Response):
    return create_course(mongo, response, course)


@api.post("/test-login")
def post_test_login(request: Request, response: Response):
    return test_login(request, response)


app.mount("/api", api)
app.mount("/", StaticFiles(directory="../Webinterface", html=True), name="WebInterface")
