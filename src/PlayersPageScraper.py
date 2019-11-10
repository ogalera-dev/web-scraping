#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:40:41 2019

@author: oscar
"""
import logging
from bs4 import BeautifulSoup
from PlayerPageScraper import PlayerPageScraper as PlayerScraper
import time

class PlayerInfo():
    def __init__(self, player_id, name, start_year, end_year, position, height, weight, birth_date, collage):
        self.id = player_id
        self.name = name
        self.start_year = start_year
        self.end_year = end_year
        self.position = position
        self.height = height
        self.weight = weight
        self.birth_date = birth_date
        self.collage = collage

#Aquest modul conté la lògica que s'encarrega de descarregar totes les dades 
#de tots els jugadors on el seu nom comença per una determinada lletra.
#
#Coneix el mòdul PlayerPageScraper
class PlayersPageScraper():
    def __init__(self, pool):
        self.playerScraper = PlayerScraper(pool)
        self.pool = pool
        
    def __download_html(self, url):
        logging.getLogger("urllib3").setLevel(logging.WARNING)
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
        
    def __parse_birthdate(self, soup):
        if soup.a is None:
            return ''
        return soup.a.string
        
    def __parse_collage(self, soup):
        if soup.a is None:
            return ''
        return soup.a.string
    
    def __get_table_indexs(self, table_per_game):
        indexs = {'Player': -1, 'From': -1, 'To': -1, 'Pos': -1, 'Ht': -1, 'Wt': -1, 'Birth Date': -1, 'Colleges': -1}
        cols = table_per_game.thead.find_all('th')
        i = 0
        for col in cols:
            if col.string in indexs.keys():
                indexs[col.string] = i
            i += 1
        return indexs
    
    def __select_col(self, indexs, col_name, fields, extractor):
        if col_name in indexs and indexs[col_name] != -1:
            return extractor(fields[indexs[col_name]])
        return ''
    
    def __extract_string(self, soap_object):
        return soap_object.string
    
    def scrapPlayers(self, url, subdomain, letter, sleep_between_player_download_s = 0.5):
        print('Scrapping letter: '+letter)
        players_info = []
        players_data = []
        players_totals = []
        html = self.__download_html(url+'/'+subdomain+'/'+letter)
        soup = BeautifulSoup(html, 'html.parser')
        table_players = soup.find("table", id='players')
        indexs = self.__get_table_indexs(table_players)
        rows = table_players.tbody.find_all('tr')
        
        i = 1
        num_rows = str(len(rows))
        for row in rows:
            try:
                player_fields = row.contents
                #Player indetifier
                player_id = i
                #Player name
                player_name = self.__select_col(indexs, 'Player', player_fields, self.__parse_player_name)
                #Player URL
                player_url = self.__select_col(indexs, 'Player', player_fields, extractor = self.__parse_player_url)
                #Start year
                start_year = self.__select_col(indexs, 'From', player_fields, extractor = self.__extract_string)
                #End year
                end_year = self.__select_col(indexs, 'To', player_fields, extractor = self.__extract_string)
                #Position
                position = self.__select_col(indexs, 'Pos', player_fields, extractor = self.__extract_string)
                #Height (in feeds)
                height = self.__select_col(indexs, 'Ht', player_fields, extractor = self.__extract_string)
                #Weight (in lb)
                weight = self.__select_col(indexs, 'Wt', player_fields, extractor = self.__extract_string)
                #Birth date
                birth_date = self.__select_col(indexs, 'Birth Date', player_fields, extractor = self.__parse_birthdate)
                #Collage
                collage = self.__select_col(indexs, 'Colleges', player_fields, extractor = self.__parse_collage)
                
                #Players info
                players_info.append(PlayerInfo(player_id, player_name, start_year, end_year, position, height, weight, birth_date, collage))
                
                #Get data per game
                print('\tScrapping player: ' + player_name + ' (' + str(i) + '/' + num_rows + ')' )
                player_data, player_totals = self.playerScraper.scrap_player_career(player_id, url+'/'+player_url)
                players_data = players_data + player_data
                players_totals.append(player_totals)
            except: 
                print('Error scrapping player '+ i + ' continue...')
            
            if sleep_between_player_download_s != -1:
                time.sleep(sleep_between_player_download_s)
        
            i += 1

        return players_info, players_data, players_totals
        
            