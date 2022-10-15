from mongo_api import MongoAPI

if __name__ == "__main__":
    mongo = MongoAPI('vvzpp.5byhvi1.mongodb.net', 'VVZpp', 'server', 'Xr9wqtrvnlufZQho')

    new_movie = {'name': 'First Man', 'length': 141}
    res = mongo.insert_one('lectures', new_movie)

    print(res)