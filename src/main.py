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

logging.getLogger("urllib3").setLevel(logging.WARNING)

pool = urllib3.PoolManager()
nba = NBA(pool)
players_info, datas_per_game, totals = nba.download_data()
players_info_df = pd.DataFrame.from_dict(players_info)
datas_per_game_df = pd.DataFrame.from_dict(datas_per_game)
totals_df = pd.DataFrame.from_dict(totals)
#print(players_info)

#datas_per_game_df.show()
#player = PlayersScraper(pool)
#print(player.scrapPlayers('https://www.basketball-reference.com'))

save_data = True

if save_data:
    players_info_df.to_csv('../data/info_players.csv')
    datas_per_game_df.to_csv('../data/data_players.csv')
    totals_df.to_csv('../data/totals.csv')