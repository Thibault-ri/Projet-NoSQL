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
ListeEthnie=["White","Hispanic, White","Black","Hispanic, Black","Asian, Other","Asian Indian","Chinese","Hawaiian","Native American, Other"]
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
		print("Ce numero ne correspond à aucun choix, veuillez le modifier: \n Entrez votre choix:\n")
		reponse=int(input())
	os.system('cls' if os.name == 'nt' else 'clear')
	if reponse==1:
		print("Veuillez choisir une drogue parmis cette liste: \n Heroin, Cocaine, Fentanyl, FentanylAnalogue, Oxycodone, Oxymorphone, Ethanol, Hydrocodone, Benzodiazepine, Methadone, Amphet, Tramad, Morphine_NotHeroin, Hydromorphone, Other, OpiateNOS, AnyOpioid\n et entrer son nom:")
		choix_drug=str(input())
		while choix_drug not in Liste_drogues:
			print("Cette drogue ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_drug=str(input())
		print("Veuillez choisir un age:")
		choix=int(input())
		temp=Victimes.find({choix_drug:"Y"})
		count=0
		for x in temp:
			if int(x["Age"])==choix:
				count+=1
		print("Il y a "+str(count)+" victimes correspondant à votre demande")
		print("Souhaitez vous les afficher? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({choix_drug:"Y"})
			for x in temp:
				if int(x["Age"])==choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==2:
		print("Veuillez choisir une drogue parmis cette liste: \n Heroin, Cocaine, Fentanyl, FentanylAnalogue, Oxycodone, Oxymorphone, Ethanol, Hydrocodone, Benzodiazepine, Methadone, Amphet, Tramad, Morphine_NotHeroin, Hydromorphone, Other, OpiateNOS, AnyOpioid\n et entrer son nom:")
		choix_drug=str(input())
		while choix_drug not in Liste_drogues:
			print("Cette drogue ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_drug=str(input())
		print("Veuillez choisir un age:")
		choix=int(input())
		temp=Victimes.find({choix_drug:"Y"})
		count=0
		for x in temp:
			if int(x["Age"])<choix:
				count+=1
		print("\nIl y a "+str(count)+" victimes correspondant à votre demande")
		print("Souhaitez vous les afficher? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({choix_drug:"Y"})
			for x in temp:
				if int(x["Age"])<choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==3:
		print("Veuillez choisir une drogue parmis cette liste: \n Heroin, Cocaine, Fentanyl, FentanylAnalogue, Oxycodone, Oxymorphone, Ethanol, Hydrocodone, Benzodiazepine, Methadone, Amphet, Tramad, Morphine_NotHeroin, Hydromorphone, Other, OpiateNOS, AnyOpioid\n et entrer son nom:")
		choix_drug=str(input())
		while choix_drug not in Liste_drogues:
			print("Cette drogue ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_drug=str(input())
		print("Veuillez choisir un age:")
		choix=int(input())
		temp=Victimes.find({choix_drug:"Y"})
		count=0
		for x in temp:
			if int(x["Age"])>choix:
				count+=1
		print("Il y a "+str(count)+" victimes correspondant à votre demande")
		print("Souhaitez vous les afficher? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({choix_drug:"Y"})
			for x in temp:
				if int(x["Age"])>choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==4:
		print("Veuillez choisir une drogue parmis cette liste: \n Heroin, Cocaine, Fentanyl, FentanylAnalogue, Oxycodone, Oxymorphone, Ethanol, Hydrocodone, Benzodiazepine, Methadone, Amphet, Tramad, Morphine_NotHeroin, Hydromorphone, Other, OpiateNOS, AnyOpioid\n et entrer son nom:")
		choix_drug=str(input())
		while choix_drug not in Liste_drogues:
			print("Cette drogue ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_drug=str(input())
		print("\nVeuillez choisir un sexe: Male ou Female")
		choix=str(input())
		while choix not in ["Male","Female"]:
			print("Ce sexe ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix=str(input())
		temp=Victimes.find({choix_drug:"Y"})
		count=0
		for x in temp:
			if str(x["Sex"])==choix:
				count+=1
		print("\nIl y a "+str(count)+" victimes correspondant à votre demande")
		print("Souhaitez vous les afficher? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({choix_drug:"Y"})
			for x in temp:
				if str(x["Sex"])==choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==5:
		print("Veuillez choisir une drogue parmis cette liste: \n Heroin, Cocaine, Fentanyl, FentanylAnalogue, Oxycodone, Oxymorphone, Ethanol, Hydrocodone, Benzodiazepine, Methadone, Amphet, Tramad, Morphine_NotHeroin, Hydromorphone, Other, OpiateNOS, AnyOpioid\n et entrer son nom:")
		choix_drug=str(input())
		while choix_drug not in Liste_drogues:
			print("Cette drogue ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_drug=str(input())
		print("\nVeuillez choisir une ethnie parmis les suivantes (attention a bien respecter l orthographe): ")
		for x in ListeEthnie:
			print(x)
		print("\n")
		choix=str(input())
		while choix not in ListeEthnie:
			print("Cette ethnie ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix=str(input())
		temp=Victimes.find({choix_drug:"Y"})
		count=0
		for x in temp:
			if str(x["Race"])==choix:
				count+=1
		print("\nIl y a "+str(count)+" victimes correspondant à votre demande")
		print("Souhaitez vous les afficher? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({choix_drug:"Y"})
			for x in temp:
				if str(x["Race"])==choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==6:
		print("Veuillez choisir une ville parmis cette liste: \n HARTFORD,NEW HAVEN,WATERBURY,BRIDGEPORT, NEW BRITAIN, MERIDEN,NORWICH,BRISTOL,NEW LONDON,DANBURY, TORRINGTON,MANCHESTER,MIDDLETOWN,ENFIELD,STAMFORD,EAST HARTFORD, MILFORD, WEST HAVEN,NORWALK,DERBY\n et entrer son nom:")
		choix_ville=str(input())
		while choix_ville not in ListeVille:
			print("Cette ville ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_ville=str(input())
		print("Veuillez choisir un age:")
		choix=int(input())
		temp=Victimes.find({"DeathCity":choix_ville})
		count=0
		for x in temp:
			if int(x["Age"])==choix:
				count+=1
		print("\nIl y a "+str(count)+" victimes correspondant à votre demande")
		print("Souhaitez vous les afficher? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({"DeathCity":choix_ville})
			for x in temp:
				if int(x["Age"])==choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==7:
		print("Veuillez choisir une ville parmis cette liste: \n HARTFORD,NEW HAVEN,WATERBURY,BRIDGEPORT, NEW BRITAIN, MERIDEN,NORWICH,BRISTOL,NEW LONDON,DANBURY, TORRINGTON,MANCHESTER,MIDDLETOWN,ENFIELD,STAMFORD,EAST HARTFORD, MILFORD, WEST HAVEN,NORWALK,DERBY\n et entrer son nom:")
		choix_ville=str(input())
		while choix_ville not in ListeVille:
			print("Cette ville ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_ville=str(input())
		print("\nVeuillez choisir un sexe: Male ou Female")
		choix=str(input())
		while choix not in ["Male","Female"]:
			print("Ce sexe ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix=str(input())
		temp=Victimes.find({"DeathCity":choix_ville})
		count=0
		for x in temp:
			if str(x["Sex"])==choix:
				count+=1
		print("\nIl y a "+str(count)+" victimes correspondant à votre demande")
		print("Souhaitez vous les afficher? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({"DeathCity":choix_ville})
			for x in temp:
				if str(x["Sex"])==choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==8:
		print("Veuillez choisir une ville parmis cette liste: \n HARTFORD,NEW HAVEN,WATERBURY,BRIDGEPORT, NEW BRITAIN, MERIDEN,NORWICH,BRISTOL,NEW LONDON,DANBURY, TORRINGTON,MANCHESTER,MIDDLETOWN,ENFIELD,STAMFORD,EAST HARTFORD, MILFORD, WEST HAVEN,NORWALK,DERBY\n et entrer son nom:")
		choix_ville=str(input())
		while choix_ville not in ListeVille:
			print("Cette ville ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_ville=str(input())
		print("Veuillez choisir un age:")
		choix=int(input())
		temp=Victimes.find({"DeathCity":choix_ville})
		count=0
		for x in temp:
			if int(x["Age"])>choix:
				count+=1
		print("\nIl y a "+str(count)+" victimes correspondant à votre demande")
		print("Souhaitez vous les afficher? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({"DeathCity":choix_ville})
			for x in temp:
				if int(x["Age"])>choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==9:
		print("Veuillez choisir une ville parmis cette liste: \n HARTFORD,NEW HAVEN,WATERBURY,BRIDGEPORT, NEW BRITAIN, MERIDEN,NORWICH,BRISTOL,NEW LONDON,DANBURY, TORRINGTON,MANCHESTER,MIDDLETOWN,ENFIELD,STAMFORD,EAST HARTFORD, MILFORD, WEST HAVEN,NORWALK,DERBY\n et entrer son nom:")
		choix_ville=str(input())
		while choix_ville not in ListeVille:
			print("Cette ville ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_ville=str(input())
		print("Veuillez choisir un age:")
		choix=int(input())
		temp=Victimes.find({"DeathCity":choix_ville})
		count=0
		for x in temp:
			if int(x["Age"])<choix:
				count+=1
		print("\nIl y a "+str(count)+" victimes correspondant à votre demande\n")
		print("Souhaitez vous les afficher? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({"DeathCity":choix_ville})
			for x in temp:
				if int(x["Age"])<choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==10:
		print("\nVeuillez choisir une ethnie parmis les suivantes (attention a bien respecter l orthographe): ")
		for x in ListeEthnie:
			print(x)
		print("\n")
		choix=str(input())
		while choix not in ListeEthnie:
			print("Cette ethnie ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix=str(input())
		print("\nVeuillez choisir un sexe: Male ou Female")
		choix_sex=str(input())
		while choix_sex not in ["Male","Female"]:
			print("Ce sexe ne correspond à aucun choix, veuillez modifier votre choix: \n Entrez votre choix:\n")
			choix_sex=str(input())
		temp=Victimes.find({"Race":choix})
		count=0
		for x in temp:
			if str(x["Sex"])==choix_sex:
				count+=1
		print("\nIl y a "+str(count)+" victimes correspondant à votre demande")
		print("Souhaitez vous les afficher? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({"Race":choix})
			for x in temp:
				if str(x["Sex"])==choix_sex:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==11:
		max=0
		max_c=""
		for x in ListeVille:
			temp=Victimes.find({"DeathCity":x})
			count=0
			for y in temp:
				count+=1
			if count>max:
				max=count
				max_c=x
		print("\nLa ville avec le plus de mort est: "+max_c+" avec "+str(max)+" morts.")
		print("Souhaitez vous afficher leur informations? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({"DeathCity":max_c})
			for x in temp:
				print(x)
				print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==12:
		max=0
		max_d=""
		for x in Liste_drogues:
			temp=Victimes.find({x:"Y"})
			count=0
			for y in temp:
				count+=1
			if count>max:
				max=count
				max_d=x
		print("\nLa drogue presente chez le plus de mort est: "+max_d+" avec "+str(max)+" morts.")
		print("Souhaitez vous afficher leur informations? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({max_d:"Y"})
			for x in temp:
				print(x)
				print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==13:
		print("Veuillez choisir un age:")
		choix=int(input())
		max=0
		max_d=""
		for x in Liste_drogues:
			temp=Victimes.find({x:"Y"})
			count=0
			for y in temp:
				if int(y["Age"])>choix:
					count+=1
			if count>max:
				max=count
				max_d=x
		print("\nLa drogue presente chez le plus de mort de plus de "+str(choix)+"ans est: "+max_d+" avec "+str(max)+" morts.")
		print("Souhaitez vous afficher leur informations? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({max_d:"Y"})
			for x in temp:
				if int(x["Age"])>choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==14:
		print("Veuillez choisir un age:")
		choix=int(input())
		max=0
		max_d=""
		for x in Liste_drogues:
			temp=Victimes.find({x:"Y"})
			count=0
			for y in temp:
				if int(y["Age"])<choix:
					count+=1
			if count>max:
				max=count
				max_d=x
		print("\nLa drogue presente chez le plus de mort de moins de "+str(choix)+"ans est: "+max_d+" avec "+str(max)+" morts.")
		print("Souhaitez vous afficher leur informations? (y/n)")
		rep=str(input())
		if rep=="y" or rep=="Y":
			temp=Victimes.find({max_d:"Y"})
			for x in temp:
				if int(x["Age"])<choix:
					print(x)
					print("\n")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==15:
		Sage=0
		Nm=0
		temp=Victimes.find()
		for x in temp:
			Sage+=int(x["Age"])
			Nm+=1
		Moy=Sage/Nm
		print("\nLa moyenne d'age des victimes de drogue est de: "+str(Moy)+"ans.")
		print("\n\n Souhaitez vous revenir au menu ? (y/n)")
		quitter=input()
		if quitter!="y" and quitter!="Y":
			Arret_prog=True
	if reponse==16:
		Arret_prog=True
		os.system('cls' if os.name == 'nt' else 'clear')
				