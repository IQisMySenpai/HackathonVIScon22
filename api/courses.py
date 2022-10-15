from mongo_api import *
from api_common import *
from structs import *

def get_courses(db: MongoAPI):
    courses = db.find("courses")

    if len(courses) == 0:
        return pack_response(204, "No courses found.")

    return pack_response(200, "ok", {"courses": Course.out(Course.from_db(courses))})

