'''
Aqui puedes buscar el ID asociado a un heroe
Shadow Fiend 11
Queen of Pain 39
Ember Spirit 106
'''

import requests
import pandas as pd
from openpyxl import Workbook

list_heroes_objects = requests.get(f'https://api.opendota.com/api/heroes')
list_heroes_objects = list_heroes_objects.json()
#print(list_heroes_objects)

heroes_df = pd.DataFrame(list_heroes_objects)
#print(heroes_df)

heroes_df.to_excel('heroes_df.xlsx')
print(heroes_df)

'''
nombres = [i['localized_name'] for i in list_heroes_objects]
#print(nombres)


search_hero = 'Queen of Pain'

for heroes_objects in list_heroes_objects:
    hero_name = heroes_objects['localized_name']
    hero_id = heroes_objects['id']
    if hero_name == search_hero:
        print(f'id {hero_name} = {hero_id}')
        id_heroe = hero_id
'''