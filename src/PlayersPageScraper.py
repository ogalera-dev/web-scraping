#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:40:41 2019

@author: oscar
"""

from bs4 import BeautifulSoup
from PlayerPageScraper import PlayerPageScraper as PlayerScraper

#Aquest modul conté la lògica que s'encarrega de descarregar totes les dades 
#de tots els jugadors on el seu nom comença per una determinada lletra.
#
#Coneix el mòdul PlayerPageScraper
class PlayersPageScraper():
    def __init__(self, pool):
        self.playerScraper = PlayerScraper(pool)
        self.pool = pool
        
    def __download_html(self, url):
        response = self.pool.request('GET', url)
        return response.data
    
    def __parse_player_name(self, soup):
        if soup.a is None:
            return ''
        return soup.a.string
    
    def __parse_player_url(self, soup):
        if soup.a is None:
            return ''
        return soup.a['href']
    
    def __parse_start_year(self, soup):
        return soup.string
        
    def __parse_end_year(self, soup):
        return soup.string
        
    def __parse_position(self, soup):
        return soup.string
        
    def __parse_height(self, soup):
        return soup.string
        
    def __parse_weight(self, soup):
        return soup.string
        
    def __parse_birthdate(self, soup):
        if soup.a is None:
            return ''
        return soup.a.string
        
    def __parse_collage(self, soup):
        if soup.a is None:
            return ''
        return soup.a.string
    
    def scrapPlayers(self, url, subdomain, letter):
        html = self.__download_html(url+'/'+subdomain+'/'+letter)
        soup = BeautifulSoup(html, 'html.parser')
        table_players = soup.find("table", id='players')
        rows = table_players.tbody.find_all('tr')
        i = 1
        for row in rows:
            if i == 1:
                player_fields = row.contents
                #Player name
                player_name = self.__parse_player_name(player_fields[0])
                print(player_name)
                #Player URL
                player_url = self.__parse_player_url(player_fields[0])
                print(player_url)
                #Start year
                start_year = self.__parse_start_year(player_fields[1])
                print(start_year)
                #End year
                end_year = self.__parse_end_year(player_fields[2])
                print(end_year)
                #Position
                position = self.__parse_position(player_fields[3])
                print(position)
                #Height (in feeds)
                height = self.__parse_height(player_fields[4])
                print(height)
                #Weight (in lb)
                weight = self.__parse_weight(player_fields[5])
                print(weight)
                #Birth date
                birth_date = self.__parse_birthdate(player_fields[6])
                print(birth_date)
                #Collage
                collage = self.__parse_collage(player_fields[7])
                print(collage)
                #Data per game
                print('URL '+url+'/'+player_url)
                data_per_game = self.playerScraper.scrap_player_career(url+'/'+player_url)
                print(data_per_game)
            i += 1
            