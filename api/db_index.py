from db import *
from bson.objectid import ObjectId
from courses import Course, Tag

# mongo.collection("courses").create_index([('title', 'text')])

tags = Tag.from_db(mongo.find("tags"))
tags = [tag.db_dict() for tag in tags]

tags[0]['_id'] = ObjectId("aaaaaaaaaaaaaaaaaaaaaaaa")

courses = Course.from_db(mongo.find("courses", limit=1))

for course in courses:
    mongo.update("courses", filter_dict={'_id': course.id}, update_dict=[{'$set': {'tags': tags}}])