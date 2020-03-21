import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import time
import os


dt=pd.read_csv("test.csv",sep=',')
tridate=dt.sort_values('ID')



client = MongoClient()
db = client.Morts #Creation database
Victimes = db.Victimes #Creation Collection
for i in range(30):  
	Victime_id = Victimes.insert_one({"Date":tridate.iloc[i]['Date'],"Age":tridate.iloc[i]['Age'], "Sex":tridate.iloc[i]['Sex'],"Race":tridate.iloc[i]['Race'],"DeathCity":tridate.iloc[i]['DeathCity'],"Heroin":tridate.iloc[i]['Heroin'],'Cocaine':tridate.iloc[i]['Cocaine'],'Fentanyl':tridate.iloc[i]['Fentanyl'],'FentanylAnalogue':tridate.iloc[i]['FentanylAnalogue'],'Oxycodone':tridate.iloc[i]['Oxycodone'],'Oxymorphone':tridate.iloc[i]['Oxymorphone'],'Ethanol':tridate.iloc[i]['Ethanol'],'Hydrocodone':tridate.iloc[i]['Hydrocodone'],'Benzodiazepine':tridate.iloc[i]['Benzodiazepine'],'Methadone':tridate.iloc[i]['Methadone'],'Amphet':tridate.iloc[i]['Amphet'],'Tramad':tridate.iloc[i]['Tramad'],'Morphine_NotHeroin':tridate.iloc[i]['Morphine_NotHeroin'],'Hydromorphone':tridate.iloc[i]['Hydromorphone'],'Other':tridate.iloc[i]['Other'],'OpiateNOS':tridate.iloc[i]['OpiateNOS'],'AnyOpioid':tridate.iloc[i]['AnyOpioid']}).inserted_id #insertion document dans collection
	#time.sleep(.1)








# with open('data.json') as f:
	# file_data = json.load(f)

# collection_currency.insert_one(file_data)



# doc_id = testcollec.insert_one({"name":'bureau', "size":12}).inserted_id #insertion document dans collection
# print(doc_id)
# print(db.list_collection_names())
# print(testcollec.find_one({"name": "bureau"})) #recherche doc par un critere
