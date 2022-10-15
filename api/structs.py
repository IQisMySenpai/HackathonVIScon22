import time
from typing import Union, List
from pydantic import BaseModel

class User(BaseModel):
    preferred_username: str

class Tag(BaseModel):
    id: Union[str, None] = None
    name: Union[str, None] = None
    color: Union[str, None] = None

    @staticmethod
    def from_db(tags):
        return [Tag().from_dict(d) for d in tags]

    @staticmethod
    def out(tags):
        if tags is None:
            return None
        return [tag.out_dict() for tag in tags]

    @staticmethod
    def db_out(tags):
        if tags is None:
            return None
        return [tag.db_dict() for tag in tags]


    def from_dict(self, d):
        self.id = d.get("_id")
        self.name = d.get("name")
        self.color = d.get("color")
        return self

    def db_dict(self):
        return {"name": self.name, "color": self.color}

    def out_dict(self):
        return {"id": self.id.__str__(), "name": self.name, "color": self.color}


class Lecturer(BaseModel):
    id: Union[str, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    title: Union[str, None] = None
    department: Union[str, None] = None

    @staticmethod
    def from_db(profs):
        return [Lecturer().from_dict(d) for d in profs]

    @staticmethod
    def out(profs):
        if profs is None:
            return []
        return [prof.out_dict() for prof in profs]

    def from_dict(self, d):
        self.id = d.get("_id")
        self.first_name = d.get("first_name")
        self.last_name = d.get("last_name")
        self.department = d.get("department")
        self.title = d.get("title")
        return self

    def out_dict(self):
        return {"id": self.id.__str__(), "first_name": self.first_name, "last_name": self.last_name,
                "title": self.title, "department": self.department}


class Review(BaseModel):
    id: Union[str, None] = None
    date: Union[int, None] = None
    rating: Union[int, None] = None
    pos: Union[int, None] = None
    neg: Union[int, None] = None

    @staticmethod
    def from_db(profs):
        return [Lecturer().from_dict(d) for d in profs]

    @staticmethod
    def out(profs):
        if profs is None:
            return []
        return [prof.out_dict() for prof in profs]

    def from_dict(self, d):
        self.id = d.get("_id")
        self.first_name = d.get("first_name")
        self.last_name = d.get("last_name")
        self.department = d.get("department")
        self.title = d.get("title")
        return self

    def out_dict(self):
        return {"id": self.id.__str__(), "first_name": self.first_name, "last_name": self.last_name, "title": self.title, "department": self.department}


class Course(BaseModel):
    id: Union[str, None] = None
    segments: Union[list, None] = None
    readable_id: Union[str, None] = None
    title: Union[str, None] = None
    course_type: Union[str, None] = None
    ects: Union[str, None] = None
    hours: Union[str, None] = None
    lecturers: Union[List[Lecturer], None] = None
    abstract: Union[str, None] = None
    objective: Union[str, None] = None
    content: Union[str, None] = None
    tags: Union[List[Tag], None] = None
    ratings: Union[int, None] = None

    @staticmethod
    def from_db(courses):
        return [Course().from_dict(d) for d in courses]

    @staticmethod
    def out(courses):
        return [course.out_dict() for course in courses]

    def from_dict(self, d):
        self.id = d.get("_id")
        self.title = d.get("title")
        self.abstract = d.get("abstract")

        self.segments = d.get("segments")
        self.readable_id = d.get("readable_id")
        self.course_type = d.get("course_type")
        self.ects = d.get("ects")
        self.hours = d.get("hours")
        self.objective = d.get("objective")
        self.content = d.get("content")
        self.ratings = d.get("ratings")

        if "tags" in d:
            self.tags = Tag.from_db(d["tags"])

        if "lecturer" in d:
            self.lecturers = []
            for lecturer_id in d["lecturer"]:
                lecturer = Lecturer()
                lecturer.id = lecturer_id
                #print(lecturer)
                self.lecturers.append(lecturer)

        return self

    def db_dict(self):
         return {"_id": self.id,
               "lecturer": Lecturer.out(self.lecturers), "tags": Tag.db_out(self.tags)}

    def out_dict(self):
        return {"id": self.id.__str__(), "title": self.title, "abstract": self.abstract,
                "lecturers": Lecturer.out(self.lecturers), "tags": Tag.out(self.tags)}

    def full_dict(self):
        return {"_id": self.id,
               "lecturer": Lecturer.out(self.lecturers),
                "tags": Tag.db_out(self.tags),
                "segments": self.segments,
                "readable_id": self.readable_id,
                "title": self.title,
                "course_type": self.course_type,
                "ects": self.ects,
                "hours": self.hours,
                "abstract": self.abstract,
                "objective": self.objective,
                "content": self.content,
                "ratings": self.ratings

        }
