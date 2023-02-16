import requests
import json

class Superhero:
  
  def most_intelligence_hero(hero_list):
    heroes_int_list = {}
    url = "https://akabab.github.io/superhero-api/api/all.json"
    responce = requests.get(url)
    result = responce.json()
    for i in result:
      if i['name'] in hero_list:
        heroes_int_list[i['name']] = i['powerstats']['intelligence'] 
    print(max(heroes_int_list))
    