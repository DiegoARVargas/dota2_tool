'''
Aqui analizamos las victorias y derrotas de partidas ranked (ranked solo y en equipo) para un heroe mio vs un heroe enemigo.
'''
import requests
import pandas as pd
from openpyxl import Workbook


id_player = 133228882 
id_heroe = 13
t_lobby = 7
id_enemigo = 39
id_lanerole = 2

'''
variable1 = requests.get(f'https://api.opendota.com/api/players/{id_player}/wl?hero_id={id_heroe}&lobby_type={t_lobby}&against_hero_id={id_enemigo}')
variable1 = variable1.json()
print(f'Variable1 --> {variable1}')

variable2 = requests.get(f'https://api.opendota.com/api/players/{id_player}/wl?lane_role={id_lanerole}&hero_id={id_heroe}&lobby_type={t_lobby}&against_hero_id={id_enemigo}')
variable2 = variable2.json()
print(f'Variable2 --> {variable2}')
'''

variable3 = requests.get(f'https://api.opendota.com/api/players/{id_player}/recentMatches')
variable3 = variable3.json()
#print(variable3)
variable3_df = pd.DataFrame(variable3)
print(variable3_df)

'''
Puck vs Shadow FIend --> {'win': 11, 'lose': 9}
Puck vs Ember Spirit --> {'win': 8, 'lose': 5}
Puck vs Queen of Pain --> {'win': 15, 'lose': 17}
-----------------------------
Lane roles
1) safe
2) mid
3) off
4) jungle
'''