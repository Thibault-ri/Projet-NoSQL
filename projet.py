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
dt = dt.dropna(subset=['Age'])

tridate=dt.sort_values('ID')



client = MongoClient()
db = client.Morts #Creation database
Victimes = db.Victimes #Creation Collection
for i in range(5000):  
	Victime_id = Victimes.insert_one({"Date":tridate.iloc[i]['Date'],"Age":tridate.iloc[i]['Age'], "Sex":tridate.iloc[i]['Sex'],"Race":tridate.iloc[i]['Race'],"DeathCity":tridate.iloc[i]['DeathCity'],"Heroin":tridate.iloc[i]['Heroin'],'Cocaine':tridate.iloc[i]['Cocaine'],'Fentanyl':tridate.iloc[i]['Fentanyl'],'FentanylAnalogue':tridate.iloc[i]['FentanylAnalogue'],'Oxycodone':tridate.iloc[i]['Oxycodone'],'Oxymorphone':tridate.iloc[i]['Oxymorphone'],'Ethanol':tridate.iloc[i]['Ethanol'],'Hydrocodone':tridate.iloc[i]['Hydrocodone'],'Benzodiazepine':tridate.iloc[i]['Benzodiazepine'],'Methadone':tridate.iloc[i]['Methadone'],'Amphet':tridate.iloc[i]['Amphet'],'Tramad':tridate.iloc[i]['Tramad'],'Morphine_NotHeroin':tridate.iloc[i]['Morphine_NotHeroin'],'Hydromorphone':tridate.iloc[i]['Hydromorphone'],'Other':tridate.iloc[i]['Other'],'OpiateNOS':tridate.iloc[i]['OpiateNOS'],'AnyOpioid':tridate.iloc[i]['AnyOpioid']}).inserted_id #insertion document dans collection
	#time.sleep(.1)






