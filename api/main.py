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

#@api.get("/lecturers")
#def read_lecturers(response: Response):
#    return list_lecturers(mongo, response)

@api.get("/courses")
def read_courses(response: Response, page: int = 0):
    return list_courses(mongo, response, page)

@api.get("/query/courses")
def read_courses(response: Response, query: str = None,  tags: List[str] = Query(default=None), page: int = 0):
    return query_courses(mongo, response, query, tags, page)

@api.post("/courses")
def post_course(course: Course, response: Response):
    return create_course(mongo, response, course)

app.mount("/api", api)
app.mount("/", StaticFiles(directory="../Webinterface", html=True), name="WebInterface")
