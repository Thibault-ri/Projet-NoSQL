import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.test_database
testcollec = db.testcollec
doc_id = testcollec.insert_one({"name":'bureau', "size":12}).inserted_id
print(doc_id)
print(db.list_collection_names())
print(posts.find_one({"name": "bureau"}))