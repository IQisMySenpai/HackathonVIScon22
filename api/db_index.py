from db import *

mongo.collection("courses").create_index([('title', 'text')])