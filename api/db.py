from mongo_api import *

mongo = MongoAPI('vvzpp.5byhvi1.mongodb.net', 'VVZpp', 'admin', 'LR3I3ChKSA59lVmC')

print(mongo.insert("test_collection", [{"test": "Great Test!"}]))
