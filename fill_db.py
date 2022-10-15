from pymongo import MongoClient

from mongo_api import MongoAPI
import pymongo
import json

lecturerDict = {}
client = MongoClient("mongodb+srv://admin:LR3I3ChKSA59lVmC@vvzpp.5byhvi1.mongodb.net/?retryWrites=true&w=majority")

def addLecturer(lecturer):
    arr = []
    # print(lecturer)
    for lec in lecturer:
        mid = lec.get("id")



        arr.append(mid)
        content = {}
        for a, b in lec.items():

            if a == "id":
                content.update({"vvz_id": b})
            elif a != "id":
                # print (a,b)
                content.update({a: b})
        lecturerDict.update({mid: content})


        # if already exist you have to find them otherwise (can be done using the lecturerDict libary)
        # ans= client.lecturers.insertOne({mid: content})
    print(ans)



    # arr.append(mid)
    return arr


if __name__ == "__main__":
    with open("courses.json", "rb") as file:
        # json_bytes = file.read()
        data = json.load(file)
        print("test print")

    # newData=[]

    #  for element in data:
    #     newElem=[]
    #    for key, value in element.items():
    #       if key=="id":
    #          key="vvz-id"

    # newData.append(newElem)
    # print(key, value)
    # for i in range(data.length):
    #    for

    elemList = []

    for element in data:
        newElem = {}
        for key, value in element.items():
            if key == "id":
                newElem.update({"vvz_id": value})
            elif key == "lecturer":
                temp = addLecturer(value)
                newElem.update({"lecturer": temp})
            else:
                newElem.update({key: value})

                #instead of appending you should update the list
        elemList.append(newElem)
        # print(key, value)

    print(lecturerDict)

    #for element in elemList:
     #   for key, value in element.items():
      #      print(key, value)
       #     for i in range(10000):
        #        pass

     mongo = MongoAPI('vvzpp.5byhvi1.mongodb.net', 'VVZpp', 'server', 'Xr9wqtrvnlufZQho')

    # new_movie = {'name': 'First Man', 'length': 141}
    # res = mongo.insert_one('lectures', new_movie)

    # print(res)

    # json_str = json_bytes.decode('utf-8')
    # with open('fcc.json', 'r') as fcc_file:
    # fcc_data = json.load(fcc_file)
    # print(fcc_data)

# mapi = MongoAPI(db_address="vvzpp.5byhvi1.mongodb.net", db_username="admin", db_password="wsy6YW6AA1PIfhvA")

# res = mapi.insert(collection="lecturer", document_list=[{'a': 1, 'b': 'holla'}])
# print(res)

# mapi.delete(collection="lecturer")

# print(json.loads(json_str))
