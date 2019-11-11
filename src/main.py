#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:56:13 2019

@author: oscar
"""

import logging
import urllib3
import pandas as pd
from NBAHistoryScraper import NBAHistoryScraper as NBA

PATH_DATA = '../data/'

#Posar el nivell de log del urllib3 a WARNING per evitar rebre molts missatges inecessaris.
logging.getLogger("urllib3").setLevel(logging.WARNING)

#El pool de connexions de urllib3 es comparteix entre totes les classes que fan scraping
pool = urllib3.PoolManager()
nba = NBA(pool)

#Es descarreguen les dades
players_info, datas_per_game, totals = nba.download_data()

#Es converteixen les dades a pandas DataFrame per poder fer l'exportació en CSV.
players_info_df = pd.DataFrame.from_dict(players_info)
datas_per_game_df = pd.DataFrame.from_dict(datas_per_game)
totals_df = pd.DataFrame.from_dict(totals)

#Es guarden els datasets en el directori ../data
players_info_df.to_csv(PATH_DATA + 'info_players.csv')
datas_per_game_df.to_csv(PATH_DATA + 'data_players.csv')
totals_df.to_csv(PATH_DATA + 'totals.csv')