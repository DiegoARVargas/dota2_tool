'''
Aqui analizamos las victorias y derrotas de partidas ranked (ranked solo y en equipo) para un heroe mio vs un heroe enemigo.
-----------------------------
Shadow Fiend = 11
Kunkka = 23
Shadow Shaman = 27
Sniper = 35
Queen of Pain = 39
Templar Assassin = 46
Leshrac = 52
Disruptor = 87
Medusa = 94
Techies = 105
Ember Spirit = 106
Void Spirit = 126
'''
import requests
import pandas as pd
from openpyxl import Workbook


id_player = 133228882 
id_heroe = 13
t_lobby = 7
id_enemigo = {11:'Shadow Fiend', 23:'Kunkka', 27:'Shadow Shaman', 35:'Sniper', 39:'Queen of Pain', 46:'Templar Assassin', 52:'Leshrac', 87:'Disruptor', 94:'Medusa', 105:'Techies', 106:'Ember Spirit', 126:'Void Spirit'}
id_lanerole = 2 #No vamos a usar esta variable ya que el lane_role no es un dato confiable.. Se realizaron varias pruebas y el valor esperado no es el correcto.

'''
variable2 = requests.get(f'https://api.opendota.com/api/players/{id_player}/wl?hero_id={id_heroe}&lobby_type={t_lobby}&against_hero_id={id_enemigo}')
variable2 = variable2.json()
print(f'Variable2 --> {variable2}')
'''
dict_wl_enenyheros = {}
for k, v in id_enemigo.items():
    variable1 = requests.get(f'https://api.opendota.com/api/players/{id_player}/wl?hero_id={id_heroe}&lobby_type={t_lobby}&against_hero_id={k}')
    variable1 = variable1.json()
    dict_wl_enenyheros[v] = variable1

dict_wl_enemyheros_df = pd.DataFrame(dict_wl_enenyheros)
dict_wl_enemyheros_df.to_excel('win_or_lose_df.xlsx')
print(dict_wl_enemyheros_df)

'''
variable3 = requests.get(f'https://api.opendota.com/api/players/{id_player}/recentMatches')
variable3 = variable3.json()
#print(variable3)
variable3_df = pd.DataFrame(variable3)
print(variable3_df)
'''