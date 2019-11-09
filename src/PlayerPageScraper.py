#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:40:41 2019

@author: oscar
"""

from bs4 import BeautifulSoup
    
class PlayerPerSeason():
    def __init__(self, year, age, team, assists, steals, blocks, personal_fouls, 
                 ofensive_rebounds, defensive_rebounds, points_per_game):
        self.year = year
        self.age = age
        self.team = team
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.personal_fouls = personal_fouls
        self.ofensive_rebounds = ofensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.points_per_game = points_per_game

class PlayerCarrer():
    
    def __init__(self, soup):
        self.seasons = []
        table_per_game = soup.find(id='per_game')
        rows = table_per_game.tbody.find_all('tr')
        for row in rows:
            year = row.th.a.string
            fields = row.find_all('td')
            age = fields[0].string
            team = fields[1].string
            ofensive_rebounds = fields[20].string
            defensive_rebounds = fields[21].string
            assists = fields[23].string
            steals = fields[24].string
            blocks = fields[25].string
            personal_fouls = fields[26].string
            points_per_game = fields[27].string
            self.seasons.append(PlayerPerSeason(year, age, team, assists, steals, blocks, 
                                                personal_fouls, ofensive_rebounds, defensive_rebounds, points_per_game))
            
        for season in self.seasons:
            print(season.year)
            print(season.age)
            print(season.team)
            print(season.assists)
            print(season.steals)
            print(season.blocks)
            print(season.personal_fouls)
            print(season.ofensive_rebounds)
            print(season.defensive_rebounds)
            print(season.points_per_game)
        

class PlayerPageScraper():
    def __init__(self, pool):
        self.pool = pool
        
    def __download_html(self, url):
        response = self.pool.request('GET', url)
        return response.data
    
    def scrap_player_career(self, url):
        html = self.__download_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        return PlayerCarrer(soup)