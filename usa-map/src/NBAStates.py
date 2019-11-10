#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:36:31 2019

@author: oscar
"""

class NBAStates():
    
    def __init__(self):
        self.team2state = {'BOS': 'MA', 
                           #'TOR': , Toronto està fora de USA
                           'MIA': 'FL', 
                           'MIL': 'WI', 
                           'PHI': 'PA', 
                           'IND': 'IN', 
                           'CHO': 'NC', 
                           'BRK': 'NY',
                           'DET': 'MI', 
                           'CLE': 'OH', 
                           'ATL': 'GA', 
                           'ORL': 'FL', 
                           'CHI': 'IL', 
                           'WAS': 'DC', 
                           'NYK': 'NY', 
                           'LAL': 'CA', 
                           'DEN': 'CO', 
                           'LAC': 'CA', 
                           'UTA': 'UT', 
                           'MIN': 'MN', 
                           'HOU': 'TX', 
                           'PHO': 'AZ', 
                           'SAS': 'TX',
                           'DAL': 'TX', 
                           'OKL': 'OK', 
                           'POR': 'OR', 
                           'SAC': 'CA', 
                           'MEM': 'TN', 
                           'GSW': 'CA', 
                           'NOP': 'LA'}
        
    def getStateByTeam(self, state):
        return self.team2state.get(state)