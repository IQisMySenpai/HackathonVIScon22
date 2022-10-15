from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from courses import *
from db import mongo

app = FastAPI()
api = FastAPI()

@api.get("/courses")
def read_item():
    return get_courses(mongo)

app.mount("/api", api)
app.mount("/", StaticFiles(directory="../Webinterface", html=True), name="WebInterface")
