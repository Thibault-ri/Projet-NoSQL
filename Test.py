import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import time
import os

client = MongoClient()
db = client.Morts #Creation database
Victimes = db.Victimes #Creation Collection

Liste_drogues=['Heroin','Cocaine','Fentanyl','FentanylAnalogue','Oxycodone','Oxymorphone','Ethanol','Hydrocodone','Benzodiazepine','Methadone','Amphet','Tramad','Morphine_NotHeroin','Hydromorphone','Other','OpiateNOS','AnyOpioid']
ListeVille=["HARTFORD","NEW HAVEN","WATERBURY","BRIDGEPORT", "NEW BRITAIN", "MERIDEN","NORWICH","BRISTOL","NEW LONDON","DANBURY", "TORRINGTON","MANCHESTER","MIDDLETOWN","ENFIELD","STAMFORD","EAST HARTFORD", "MILFORD", "WEST HAVEN","NORWALK","DERBY"]
Arret_prog=False

choix_m=0
choix_drug=""
while not Arret_prog:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Bienvenue sur le projet de Valentin BOUDON et Thibault RIEUL \n\n")
	print("Veuillez choisir une des requetes proposées:\n")
	print("Choix 1: Nombre de mort pour une drogue choisie et un age choisi ")
	print("Choix 2: Nombre de mort pour une drogue choisie et avant un age choisi ")
	print("Choix 3: Nombre de mort pour une drogue choisie et après un age choisi ")
	print("Choix 4: Nombre de mort pour une drogue choisie et un sexe choisi  ")
	print("Choix 5: Nombre de mort pour une drogue choisie et une ethnie choisie")
	print("Choix 6: Nombre de mort pour une ville choisie et un age choisi ")
	print("Choix 7: Nombre de mort pour une ville choisie et un sexe choisi ")
	print("Choix 8: Nombre de mort pour une ville choisie et après un age choisi ")
	print("Choix 9: Nombre de mort pour une ville choisie et avant un age choisi ")
	print("Choix 10: Nombre de mort pour une ville choisie et à un age choisi ")
	print("Choix 10: Nombre de mort pour une ethnie choisie et à un sexe choisi ")
	print("Choix 11: La ville ayant eu le plus de mort ")
	print("Choix 12: La drogue etant presente chez le plus de morts")
	print("Choix 13: La drogue etant presente chez le plus de morts après un age choisi ")
	print("Choix 14: La drogue etant presente chez le plus de morts avant un age choisi ")
	print("Choix 15: La moyenne d'age des victimes ")
	print("Choix 16: Quitter le programme ")
	print("Tapez le numero de la requete désirée")
	reponse=int(input())
	while reponse>17 & reponse<0:
		print("Ce numero ne correspond a aucun choix, veuillez le modifier: \n Entrez votre choix:\n")
		reponse=int(input())
	os.system('cls' if os.name == 'nt' else 'clear')
	if reponse==1:
		print("Veuillez choisir une drogue parmis cette liste: \n Heroin, Cocaine, Fentanyl, FentanylAnalogue, Oxycodone, Oxymorphone, Ethanol, Hydrocodone, Benzodiazepine, Methadone, Amphet, Tramad, Morphine_NotHeroin, Hydromorphone, Other, OpiateNOS, AnyOpioid\n et entrer son nom:")
		choix_drug=str(input())
		while choix_drug not in Liste_drogues:
			print("Cette drogue ne correspond a aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_drug=str(input())
		print("Veuillez choisir un age:")
		choix=int(input())
		temp=Victimes.find({choix_drug:"Y"})
		count=0
		for x in temp:
			if int(x["Age"])==choix:
				count+=1
		print("Il y a "+str(count)+" victimes correspondant à votre demande")
		Arret_prog=True
	if reponse==2:
		print("Veuillez choisir une drogue parmis cette liste: \n Heroin, Cocaine, Fentanyl, FentanylAnalogue, Oxycodone, Oxymorphone, Ethanol, Hydrocodone, Benzodiazepine, Methadone, Amphet, Tramad, Morphine_NotHeroin, Hydromorphone, Other, OpiateNOS, AnyOpioid\n et entrer son nom:")
		choix_drug=str(input())
		while choix_drug not in Liste_drogues:
			print("Cette drogue ne correspond a aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_drug=str(input())
		print("Veuillez choisir un age:")
		choix=int(input())
		temp=Victimes.find({choix_drug:"Y"})
		count=0
		for x in temp:
			if int(x["Age"])<choix:
				count+=1
		print("Il y a "+str(count)+" victimes correspondant à votre demande")
		Arret_prog=True
	if reponse==3:
		print("Veuillez choisir une drogue parmis cette liste: \n Heroin, Cocaine, Fentanyl, FentanylAnalogue, Oxycodone, Oxymorphone, Ethanol, Hydrocodone, Benzodiazepine, Methadone, Amphet, Tramad, Morphine_NotHeroin, Hydromorphone, Other, OpiateNOS, AnyOpioid\n et entrer son nom:")
		choix_drug=str(input())
		while choix_drug not in Liste_drogues:
			print("Cette drogue ne correspond a aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_drug=str(input())
		print("Veuillez choisir un age:")
		choix=int(input())
		temp=Victimes.find({choix_drug:"Y"})
		count=0
		for x in temp:
			if int(x["Age"])>choix:
				count+=1
		print("Il y a "+str(count)+" victimes correspondant à votre demande")
		Arret_prog=True
	if reponse==4:
		print("Veuillez choisir une drogue parmis cette liste: \n Heroin, Cocaine, Fentanyl, FentanylAnalogue, Oxycodone, Oxymorphone, Ethanol, Hydrocodone, Benzodiazepine, Methadone, Amphet, Tramad, Morphine_NotHeroin, Hydromorphone, Other, OpiateNOS, AnyOpioid\n et entrer son nom:")
		choix_drug=str(input())
		while choix_drug not in Liste_drogues:
			print("Cette drogue ne correspond a aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_drug=str(input())
		print("\nVeuillez choisir un sexe: Male ou Female")
		choix=str(input())
		while choix not in ["Male","Female"]:
			print("Ce sexe ne correspond a aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_drug=str(input())
		temp=Victimes.find({choix_drug:"Y"})
		count=0
		for x in temp:
			if str(x["Sex"])==choix:
				count+=1
		print("\nIl y a "+str(count)+" victimes correspondant à votre demande")
		Arret_prog=True
	if reponse==16:
			Arret_prog=True
				