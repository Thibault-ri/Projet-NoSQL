import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

dt=pd.read_csv("test.csv",sep=',')
tridate=dt.sort_values('ID')

client = MongoClient()
db = client.Mort #Creation database
Victimes = db.Victimes #Creation Collection
for i in range(5100):
    
	Victime_id = Victimes.insert_one({"Age":tridate.iloc[i]['Age'], "size":12}).inserted_id #insertion document dans collection












# with open('data.json') as f:
	# file_data = json.load(f)

# collection_currency.insert_one(file_data)



# doc_id = testcollec.insert_one({"name":'bureau', "size":12}).inserted_id #insertion document dans collection
# print(doc_id)
# print(db.list_collection_names())
# print(testcollec.find_one({"name": "bureau"})) #recherche doc par un critere
