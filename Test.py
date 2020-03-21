import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

i = 1
j = 1
y = 2
m = ""
jo = ""
d = ""
Ldate = []
while y < 7:
	while j < 13:
		while i < 32:
			if j < 10:
                m = "0"+str(j)
            else:
                m=str(j)
            if i<10:
                jo="0"+str(i)
            else:
                jo=str(i)
            d=m+"/"+jo+"/201"+y
            print(d)
			# commande d'insertion dans la base
			i+=1
		j+=1
        i=1	
    y+=1
    j=1



dt=pd.read_csv("test.csv",sep=',')
dt.sort_values(by='ID')
print(dt)


# with open('data.json') as f:
    # file_data = json.load(f)

# collection_currency.insert_one(file_data)


# client = MongoClient()
# db = client.test_database #Creation database
# testcollec = db.testcollec #Creation Collection
# doc_id = testcollec.insert_one({"name":'bureau', "size":12}).inserted_id #insertion document dans collection
# print(doc_id)
# print(db.list_collection_names())
# print(testcollec.find_one({"name": "bureau"})) #recherche doc par un critere
