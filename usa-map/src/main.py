# -*- coding: utf-8 -*-

from MapPainter import MapPinter as MapPainter
import pandas as pd

#Quants jugadors han jugat a cada equip en la temporada year?
def sample1(data_player, year):
    teams_year = data_players[data_players['year'] == year]['team']
    numer_players = teams_year.groupby().agg(['count'])
    print(numer_players)
    for num, team in numer_players:
        print(num)
        print(team)
    #painter.print_map(teams, points, 'Number of players by team and region', '../results/caca')
    return 0
    

def sample2(data, year):
    
    return 0

#Quin es el jugador amb un major punts per partit en tota l'història?
def sample3(info_players, total_data):
    max_scorer = total_data[total_data['points'] == max(total_data['points'])]
    max_scorer_info = info_players[info_players['id'] == max_scorer['id']]
    print('Name: ' + max_scorer_info.iloc[0]['name'])
    print('Start year: ' + str(max_scorer_info.iloc[0]['start_year']))
    print('End year: ' + str(max_scorer_info.iloc[0]['end_year']))
    print('Points: ' + str(max_scorer.iloc[0]['points']))
    return 0

#Quí és el jugador més jove que va debutar a l'NBA i de quina universitat prové?
def sample4(info_players, data_players):
    grouped_data_by_player = data_players.groupby('id')['age'].agg('min')
    younger_player = info_players[info_players['age'] == min(info_players['age'])].iloc[0]
    print('Name: ' + younger_player['name'])
    print('Age: ' + younger_player['age'])
    print('Team: ' + younger_player['collage'])

DATA_PATH = '../../data/'

#Carregar les dades
data_players = pd.read_csv(DATA_PATH+'data_players.csv')
info_players = pd.read_csv(DATA_PATH+'info_players.csv')
totals = pd.read_csv(DATA_PATH+'totals.csv')

print(data_players.groupby('id')['age'].agg('min'))

#sample1(data_players, '1990-91')

#sample2(info_players, '1990-91')

#sample3(info_players, totals)

#sample4(info_players)

"""
players_by_id = data_players.groupby('id')
teams = ['BOS', 'TOR', 'MIA', 'MIL', 'PHI']
points = [10, 20, 30, 40, 50]
painter = MapPainter()
painter.print_map(teams, points, 'Caca', '../results/caca')
"""

#Quants equips hi ha per estat?


