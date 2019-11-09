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
        #self.letters = list(map(chr, range(97, 123)))
        self.letters = list(map(chr, range(97, 98)))
        self.pool = pool
        self.player_scraper = PlayersScraper(self.pool)
         
    def download_data(self):
        for letter in self.letters:
            self.player_scraper.scrapPlayers(self.url,self.subdomain,letter)