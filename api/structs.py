class Course:
    id: str
    name: str
    addition: str
    tags: list

    @staticmethod
    def from_db(courses):
        return [Course(d) for d in courses]

    @staticmethod
    def out(courses):
        return [course.out_dict() for course in courses]

    def __init__(self, d=None):
        if d is not None:
            self.from_dict(d)

    def from_dict(self, d):
        self.id = d["_id"]
        self.name = d["name"]
        self.addition = d["addition"]
        self.tags = d["tags"]

    def out_dict(self):
        return {"id": self.id.__str__(), "name": self.name, "addition": self.addition, "tags": self.tags}

