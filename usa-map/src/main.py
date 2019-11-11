# -*- coding: utf-8 -*-

from MapPainter import MapPinter as MapPainter
import pandas as pd

"""
Òscar Galera Alfaro.
11/11/2019


Aquest fitxe conté alguns calculs realitzats sobre les 
dades que s'han "scrapejat" en aquesta pràctica
"""

#Ruta on hi ha els datasets
DATA_PATH = '../../data/'

#Quants jugadors han jugat a cada equip en la temporada year?
def sample1(data_player, year):
    #Filtrar 
    teams_year = data_players[data_players['year'] == year]
    numer_players = teams_year.groupby('team')['id'].agg(['count'])
    map_painter = MapPainter()
    map_painter.print_map(numer_players.index.values.tolist(), numer_players['count'], 
                          'NBA team players by state', 'Number of players', 
                          '../results/states_num_players_by_team_2015_16.png')
    
#Quin es el jugador amb major nombre de punts per partit en tota l'història?
def sample2(info_players, total_data):
    max_scorer = totals[totals['points'] == max(totals['points'])]
    id_max_scorer = max_scorer['id'].iloc[0]
    max_scorer_info = info_players[info_players['id'] == id_max_scorer]
    print('Name: ' + max_scorer_info.iloc[0]['name'])
    print('Start year: ' + str(max_scorer_info.iloc[0]['start_year']))
    print('End year: ' + str(max_scorer_info.iloc[0]['end_year']))
    print('Points: ' + format(max_scorer.iloc[0]['points'], '.0f'))
    
#Quins són els jugadors més joves que van debutar a la NBA?
def sample3(info_players, data_players):
    #Agregar per identificador el dataset de temporades i buscar el mínim al camp age
    min_age_player = pd.DataFrame(data_players.groupby('id')['age'].agg('min'))
    min_age = min(min_age_player['age'])
    #Buscar els jugadors amb valor mínim en el seu age
    youngest_players = min_age_player[min_age_player['age'] == min_age]
    #Seleccionar els indexos
    youngest_players_index = youngest_players.index.values.tolist()
    #Obtenir la informació dels jugadors més joves
    youngest_players_info = info_players[info_players['id'].isin(youngest_players_index)]
    for index, player in youngest_players_info.iterrows():
        print('Id: ' +str(player['id']))
        print('Name: ' + player['name'])
        print('Age: ' + str(int(min_age)))
        print('Start year: ' + str(player['start_year']))
        print('End year: ' + str(player['end_year']))
        print('Position: ' + player['position'] + '\n')

#Carregar les dades
data_players = pd.read_csv(DATA_PATH+'data_players.csv')
info_players = pd.read_csv(DATA_PATH+'info_players.csv')
totals = pd.read_csv(DATA_PATH+'totals.csv')

print('***\nQuestion 1\n\n')
sample1(data_players, '2014-15')

print('***\nQuestion 2\n\n\n')
sample2(info_players, totals)

print('***\nQuestion 3\n')
sample3(info_players, data_players)

