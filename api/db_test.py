from db import *

mongo.insert("courses", [{
    "name": "Test Kurs",
    "addition": "Lecture Number?",
    "tags": ["cool", "super", "duper"]
}])