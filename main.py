import requests
trainer_token = "b7434b21f5324356a08cec74b143c8db"

url = "https://api.pokemonbattle.me:9104/pokemons"

headers = {"Content-Type": "application/json", "trainer_token": trainer_token}
payload = {
    "name": "generate",
    "photo": "generate"
}
response = requests.post(url, headers=headers, json=payload)
print(response.json())

url2 = "https://api.pokemonbattle.me:9104/pokemons"

payload2 = {
    "pokemon_id": "12748",
    "name": "NewNameNagibator"
}

response2 = requests.put(url2, headers=headers, json=payload2)

print(response2.json())

url3 = "https://api.pokemonbattle.me:9104/trainers/add_pokeball"

payload3 = {"pokemon_id": "12748"}

response3 = requests.post(url3, headers=headers, json=payload2)

print(response3.json())

