#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:56:13 2019

@author: oscar
"""

import urllib3
from NBAHistoryScraper import NBAHistoryScraper as NBA

pool = urllib3.PoolManager()
nba = NBA(pool)
nba.download_data()
#player = PlayersScraper(pool)
#print(player.scrapPlayers('https://www.basketball-reference.com'))