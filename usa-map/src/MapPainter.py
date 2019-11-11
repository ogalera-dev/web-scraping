#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:29:33 2019

@author: oscar
"""

import plotly.graph_objects as go
# Load data frame and tidy it.
import pandas as pd

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

#Aquest mòdul conté la lògica necessaria per dibuixar un mapa demogràfic dels estats units d'amèrica
#a partir dels noms dels equips de la NBA.
class MapPinter():
    def __init__(self):
        self.states = NBAStates()
    
    def __group_by_state(self, teams, draft_data):
        grouped_data = {}
        i = 0
        for team in teams:
            state = self.states.getStateByTeam(team)
            if state is not None:
                if grouped_data.get(state) is None:
                    grouped_data[state] = 0.0
                grouped_data[state] = grouped_data[state] + draft_data[i]
            i += 1
            
        for key in list(grouped_data.keys()):
            print(key+ ' '+str((grouped_data[key])))
        return list(grouped_data.keys()), list(grouped_data.values())
    
    #Dibuixa un gràfic amb el mapa d'estats units a partir dels equips i amb un valor de
    #draft_data i title, aquest fitxer es pot exportar en format PNG si es passa valor
    #al paràmtre path2save
    def print_map(self, teams, draft_data, title = 'title', title_legend = 'title legend', path2save = None):
        codes, data = self.__group_by_state(teams, draft_data)
        df = pd.DataFrame.from_dict({'code': codes, 'data': data})
        
        fig = go.Figure(data=go.Choropleth(
            locations=df['code'], 
            z = df['data'].astype(float), 
            locationmode = 'USA-states', 
            colorscale = 'Reds',
            colorbar_title = title_legend,
        ))
        
        fig.update_layout(
            title_text = title,
            geo_scope='usa', 
        )
        fig.show()
        if path2save is not None:
            fig.write_image(path2save, format='png')