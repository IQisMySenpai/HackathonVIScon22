from pymongo import MongoClient

from mongo_api import MongoAPI
import pymongo
import json

lecturerDict = {}
client = MongoClient("mongodb+srv://admin:LR3I3ChKSA59lVmC@vvzpp.5byhvi1.mongodb.net/?retryWrites=true&w=majority")

client.lectctures