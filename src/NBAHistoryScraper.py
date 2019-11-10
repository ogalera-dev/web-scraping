#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:21:33 2019

@author: oscar
"""
from PlayersPageScraper import PlayersPageScraper as PlayersScraper

#Aquest modul conté la lògica que s'encarrega de descarregar totes les dades 
#de tots els jugadors de la història de la NBA. 
#
#Coneix el mòdul PlayersPageScraper
class NBAHistoryScraper():
    
    def __init__(self, pool):
        self.url = 'https://www.basketball-reference.com'
        self.subdomain = 'players'
        self.letters = list(map(chr, range(97, 123)))
        self.pool = pool
        self.player_scraper = PlayersScraper(self.pool)
        
    def __group_data_game(self, datas_per_game):
        id = []; year = []; games = []; age = []; team = []; assists = []; steals = []; blocks = []; personal_fouls = []; 
        ofensive_rebounds = []; defensive_rebounds = []; points_per_game = []
        for data_per_game in datas_per_game:
            id.append(data_per_game.id)
            year.append(data_per_game.year)
            games.append(data_per_game.games)
            age.append(data_per_game.age)
            team.append(data_per_game.team)
            assists.append(data_per_game.assists)
            steals.append(data_per_game.steals)
            blocks.append(data_per_game.blocks)
            personal_fouls.append(data_per_game.personal_fouls)
            ofensive_rebounds.append(data_per_game.ofensive_rebounds)
            defensive_rebounds.append(data_per_game.defensive_rebounds)
            points_per_game.append(data_per_game.points_per_game)
            
        return {'id': id, 'year': year, 'games': games, 'age': age, 'team': team, 'assists': assists, 'steals': steals, 
                'blocks': blocks, 'personal_fouls': personal_fouls, 'ofensive_rebounds': ofensive_rebounds, 
                'defensive_rebounds': defensive_rebounds, 'points_per_game': points_per_game}
    
    def __group_players_info(self, players_info):
        id = []; name = []; start_year = []; end_year = []; position = []; height = []; weight = []; birth_date = []; collage = []
        for player_info in players_info:
            id.append(player_info.id)
            name.append(player_info.name)
            start_year.append(player_info.start_year)
            end_year.append(player_info.end_year)
            position.append(player_info.position)
            height.append(player_info.height)
            weight.append(player_info.weight)
            birth_date.append(player_info.birth_date)
            collage.append(player_info.collage)
            
        return {'id': id, 'name': name, 'start_year': start_year, 'end_year': end_year, 'position': position, 
                'height': height, 'weight': weight, 'birth_date': birth_date, 'collage': collage}
    
    def __group_players_totals(self, players_totals):
        id = []; games = []; assists = []; steals = []; blocks = []; personal_fouls = []; 
        ofensive_rebounds = []; defensive_rebounds = []; points = []
        for total in players_totals:
            id.append(total.id)
            games.append(total.games)
            assists.append(total.assists)
            steals.append(total.steals)
            blocks.append(total.blocks)
            personal_fouls.append(total.personal_fouls)
            ofensive_rebounds.append(total.ofensive_rebounds)
            defensive_rebounds.append(total.defensive_rebounds)
            points.append(total.points)
            
        return {'id': id, 'games': games, 'assists': assists, 'steals': steals, 'blocks': blocks, 'personal_fouls': personal_fouls, 
         'ofensive_rebounds': ofensive_rebounds, 'defensive_rebounds': defensive_rebounds, 'points': points}
    
    def download_data(self):
        players_info = []
        games_data = []
        players_totals = []
        for letter in self.letters:
            letter_data = self.player_scraper.scrapPlayers(self.url,self.subdomain,letter)
            players_info = players_info + letter_data[0]
            games_data = games_data + letter_data[1]
            players_totals = players_totals + letter_data[2]
        
        return self.__group_players_info(players_info), self.__group_data_game(games_data), self.__group_players_totals(players_totals)