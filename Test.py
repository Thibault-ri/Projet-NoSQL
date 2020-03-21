import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
client = MongoClient()
db = client.mortdrogue
collection_currency = db.victimes

data = json.load(open('data.json'))

df = pd.DataFrame(data["data"])

print(df)

#with open('data.json') as f:
    #file_data = json.load(f)

#collection_currency.insert_one(file_data)


#client = MongoClient()
#db = client.test_database #Creation database
#testcollec = db.testcollec #Creation Collection
#doc_id = testcollec.insert_one({"name":'bureau', "size":12}).inserted_id #insertion document dans collection
#print(doc_id)
#print(db.list_collection_names())
#print(testcollec.find_one({"name": "bureau"})) #recherche doc par un critere
