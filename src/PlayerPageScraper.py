#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:40:41 2019

@author: oscar
"""

import logging
from bs4 import BeautifulSoup
    
#Model de dades per la informació estadística de un jugador en una temporada.
class PlayerGameData():
    def __init__(self, player_id, year, age, games, team, assists, steals, blocks, personal_fouls, 
                 ofensive_rebounds, defensive_rebounds, points_per_game):
        self.id = player_id
        self.year = year
        self.age = age
        self.games = games
        self.team = team
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.personal_fouls = personal_fouls
        self.ofensive_rebounds = ofensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.points_per_game = points_per_game

#Model de dades per la informació general d'un jugador durant la seva carrera professional.
class PlayerTotalData():
    def __init__(self, player_id, games, ofensive_rebounds, defensive_rebounds, 
                 assists, steals, blocks, personal_fouls, points):
        self.id = player_id
        self.games = games
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.personal_fouls = personal_fouls
        self.ofensive_rebounds = ofensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.points = points

#Aquest modul conté la lògica que s'encarrega de descarregar i processar la informació estadística 
#de cada jugador en cada temporada i de calcular els valors totals de cada jugador en la seva carrera professional.
class PlayerPageScraper():
    def __init__(self, pool):
        self.pool = pool
        
    def __download_html(self, url):
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        response = self.pool.request('GET', url)
        return response.data
    
    #Retorna un diccionari que "mappeja" el nom d'una dada de informació al seu índex
    def __get_table_indexs(self, table_per_game):
        indexs = {'Age': -1, 'G': -1, 'Tm': -1, 'AST': -1, 'STL': -1, 'BLK': -1, 'PF': -1, 'ORB': -1, 'DRB': -1, 'PTS': -1}
        cols = table_per_game.thead.find_all('th')
        #Es comença a -1 per saltar-se l'índex pel Season
        i = -1
        for col in cols:
            if col.string in indexs.keys():
                indexs[col.string] = i
            i += 1
        return indexs
    
    #Selecciona i extreu (extractor) la col_name dels fields en base al index que hi ha a indexs
    #Si col_name no existeix en indexs, es retorna la cadena buida
    def __select_col(self, indexs, col_name, fields, extractor):
        if col_name in indexs and indexs[col_name] != -1:
            return extractor(fields[indexs[col_name]])
        return ''
    
    def __extract_string(self, soap_object):
        return soap_object.string
    
    def __get_value(self, value):
        if value is None or len(value) == 0:
            return 0
        return float(value)
    
    #Processa les dades estadístiques d'un jugador per cada temporada i retorna una tupla
    #on el primer element és una llista de temporades i el segon un objecte de tipus PlayerTotalData
    #amb l'agregat de les temporades.
    def __parse_table_per_game(self, player_id, table_per_game):
        seasons = []
        indexs = self.__get_table_indexs(table_per_game)
        
        #Variables acumulatives per calcular els valors totals
        t_games = 0.0
        t_ofensive_rebounds = 0.0
        t_defensive_rebounds = 0.0
        t_assists = 0.0
        t_steals = 0.0
        t_blocks = 0.0
        t_personal_fouls = 0.0
        t_points = 0.0
        
        rows = table_per_game.tbody.find_all('tr')
        for row in rows:
            if row.find('th'):
                #Any de la temporada
                if row.th.find('a'):
                    year = row.th.a.string
                else:
                    year = row.th.string
                    
                fields = row.find_all('td')
                
                #Edat del jugador
                age = self.__select_col(indexs, 'Age', fields, extractor = self.__extract_string)
                
                #Equip del jugador
                team = self.__select_col(indexs, 'Tm', fields, extractor = self.__extract_string)
                
                #Nombre de partits que va jugar aquella temporada
                games = self.__select_col(indexs, 'G', fields, extractor = self.__extract_string)
                
                #Si no s'especifica el nombre de partits, es considera 0
                if games is None or len(games) == 0:
                    int_games = 0
                else:
                    int_games = int(games)
                    
                t_games += self.__get_value(games)
                
                #Percentatge de rebots ofensius
                ofensive_rebounds = self.__select_col(indexs, 'ORB', fields, extractor = self.__extract_string)
                t_ofensive_rebounds += self.__get_value(ofensive_rebounds) * int_games
                
                #Percentatge de rebots defensius
                defensive_rebounds = self.__select_col(indexs, 'DRB', fields, extractor = self.__extract_string)
                t_defensive_rebounds += self.__get_value(defensive_rebounds) * int_games
                
                #Percentatge d'assistències.
                assists = self.__select_col(indexs, 'AST', fields, extractor = self.__extract_string)
                t_assists += self.__get_value(assists) * int_games
                
                #Percentatge de robaments de pilota
                steals = self.__select_col(indexs, 'STL', fields, extractor = self.__extract_string)
                t_steals += self.__get_value(steals) * int_games
                
                #Percentatge de taps
                blocks = self.__select_col(indexs, 'BLK', fields, extractor = self.__extract_string)
                t_blocks += self.__get_value(blocks) * int_games
                
                #Percentatge de faltes personals
                personal_fouls = self.__select_col(indexs, 'PF', fields, extractor = self.__extract_string)
                t_personal_fouls += self.__get_value(personal_fouls) * int_games
                
                #Percentatge de punts per partit
                points_per_game = self.__select_col(indexs, 'PTS', fields, extractor = self.__extract_string)
                t_points += self.__get_value(points_per_game) * int_games
                
                #Es crea un objecte PlayerGameData que conté les dades del jugador per aquella temporada
                seasons.append(PlayerGameData(player_id, year, age, games, team, assists, steals, blocks, 
                                  personal_fouls, ofensive_rebounds, defensive_rebounds, points_per_game))
                
        #Es crea un objecte PlayerTotalData amb el total de cada temporada.
        player_total_data = PlayerTotalData(player_id, t_games, t_ofensive_rebounds, t_defensive_rebounds, 
                                        t_assists, t_steals, t_blocks, t_personal_fouls, t_points)
        
        return seasons, player_total_data
    
    #Descarrega i processa la informació estadística d'un jugador i retorna una tupla
    #on el primer element és una llista de temporades i el segon un objecte de tipus PlayerTotalData
    #amb l'agregat de les temporades.
    def scrap_player_career(self, player_id, url):
        html = self.__download_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        table_per_game = soup.find(id='per_game')
        return self.__parse_table_per_game(player_id, table_per_game)