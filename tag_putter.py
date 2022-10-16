import json

from api.mongo_api import MongoAPI
import random

def randomColor():
    sel = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    res_col = "#"
    for i in range(6):
        res_col += random.choice(sel)

    return res_col

def create_dics(list_a):
    return_list = []
    for el in list_a:
        return_list.append({
            "name": el,
            "color": randomColor()
        })
    return return_list


if __name__ == "__main__":
    mongo = MongoAPI('vvzpp.5byhvi1.mongodb.net', 'VVZpp', 'admin', 'LR3I3ChKSA59lVmC')

    # a = ["Autumn Semester", "Spring Semester", "CAS", "DAS", "Mobility student", "Master", "Bachelor", "Doctoral", "English", "German", "French", "Italian", "No script", "No life stream", "Graded semester performance", "No repetition", "No recording", "No correction", "No exercises", "Difficult", "GESS", "Seminar", "Languages", "Science", "Computer", "Programming", "Math", "Work", "Thesis", "Minor Courses", "Electives"]
    # a.extend(["Basisjahr", "Exchange Student", "Core Courses", "Basic Courses", "Architecture", "Biology", "Chemistry and Applied Bioscience", "Civil, Environmental and Geomatic Engineering", "Computer Sciences", "Earth Sciences", "Environmental System Science", "Health Sciences and Technology", "Humanities, Social and Political Sciences", "Information Technology and Electrical Engineering", "Materials", "Mathematics", "Mechanical and Process Engineering", "Physics", "Practical", "Jokes", "Fun", "Horrible", "History", "Literature", "Economics", "Philosophy", "Political Science", "Psychology", "Pedagogics", "Law", "UHZ"])
    # a.extend(["Glasklar", "Sociology", "Science Research", "Proseminar", "Experiment", "Labs", "Additional Courses", "Colloquia", "Limited Places", "Paying", "Pain", "Low grads", "High grads", "Strict Correction", "Introduction", "Advanced", "Analysis", "Linear Algebra", "Teamwork", "High credit low work", "High work low credit", "High work low grad", "Presentation", "Pitching", "Weekly homework", "Half semester", "Self-study", "Flipping classes", "Videos", "Fast speed", "Structured"])
    # a.extend(["No grading", "High pass rates", "High failing rates", "Q&A", "Take-home questions", "Quizzes", "Graded quizzes", "Klicker Frage", "Geht es besser", "Algorithm", "Statistic", "Problem Solving", "Workshop", "Esai", "Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6", "Exam", "No test", "Good", "Fancy", "Strict", "No technology", "Coding", "2 professors", "No lecture notes", "No reading", "Less people"])
    # a.extend(["Amazing professors", "No TA", "TC", "Teaching Diploma", "Specialized", "Focus", "Too much programming", "Too much math", "Too much physics", "Too much work", "Evident", "Logic", "Miracle", "Strange", "Educational Science", "AI", "Research", "Didactic", "TA", "Internship", "Professional Trainig", "Agricultural Science", "VIS", "Atmospheric and Climates Science", "Cyber Security", "Biomedical Engineering", "Food Science", "Interdisciplinary Brain", "Management", "Robotic", "Quantitative Finance"])

    # documents = create_dics(a)

    # print(len(a))

    all_Tags = mongo.find(collection="tags")

    courses = mongo.find(collection="courses")
    coutn = 0

    for course in courses:
        coutn += 1
        print(coutn)
        random_tags = []

        for i in range(5):
            random_tags.append(random.choice(all_Tags))

        print({"_id": course["_id"]})
        print({"$set": {"tags": random_tags}})
        mongo.update_one(collection="courses", filter_dict={"_id": course["_id"]}, update_dict={"$set": {"tags": random_tags}})
