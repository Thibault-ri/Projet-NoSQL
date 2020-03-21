# Projet-NoSQL
Projet NoSQL de Valentin BOUDON et Thibault RIEUL
url = "https://data.ct.gov/api/views/rybz-nyjw/rows.json"

headers = {
    'x-rapidapi-host': "montanaflynn-fifa-world-cup.p.rapidapi.com",
    'x-rapidapi-key': "948ca828c0mshe8fd4cb616ef4afp1372fbjsnd5c9fcc4115c",
    'accepts': "json"
    }

response = requests.request("GET", url, headers=headers)
Data=response.json

print(response.text)

i = 1
j = 1
y = 2
m = ""
jo = ""
d = ""
Ldate = []
while y < 9:
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
			d=m+"/"+jo+"/201"+str(y)
			
			i+=1
		j+=1
		i=1	
	y+=1
	j=1