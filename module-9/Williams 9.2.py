#Brieanna Williams for CSD 325-T301

#API tutorial
import requests

response = requests.get("http://api.open-notify.org/astros.json")

print(response.status_code)

print(response.json())

# 
# Own API program- pull up stats of grass type pokemon
import json
response= requests.get("https://pokeapi.co/api/v2/type/grass/")

print(response.status_code)
print(response)
print(response.json())
