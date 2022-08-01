'''
Aqui analizamos las victorias y derrotas de partidas ranked (ranked solo y en equipo) para un heroe mio vs un heroe enemigo.
'''
import requests
import pandas as pd

id_player = 133228882 
id_heroe = 13
t_lobby = 7
id_enemigo = 39

variable1 = requests.get(f'https://api.opendota.com/api/players/{id_player}/wl?hero_id={id_heroe}&lobby_type={t_lobby}&against_hero_id={id_enemigo}')
variable1 = variable1.json()

print(variable1)


'''
Puck vs Shadow FIend --> {'win': 11, 'lose': 9}
Puck vs Ember Spirit --> {'win': 8, 'lose': 5}
Puck vs Queen of Pain --> {'win': 15, 'lose': 17}
'''