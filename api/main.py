from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from courses import *
from db import mongo

app = FastAPI()

# app.mount("/", StaticFiles(directory="../Webinterface", html=True), name="WebInterface")

@app.get("/api/courses")
def read_item():
    return get_courses(mongo)
