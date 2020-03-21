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