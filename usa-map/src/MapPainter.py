#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:29:33 2019

@author: oscar
"""

from matplotlib import pyplot as plt
import plotly.graph_objects as go
from NBAStates import NBAStates as NBAStates
# Load data frame and tidy it.
import pandas as pd

class MapPinter():
    def __init__(self):
        self.states = NBAStates()
    
    def print_map(self, teams, draft_data, title, path2save):
        codes = []
        data = []
        i = 0
        for team in teams:
            state = self.states.getStateByTeam(team)
            if state is not None:                
                codes.append(state)
                data.append(draft_data[i])
            i += 1

        df = pd.DataFrame.from_dict({'code': codes, 'data': data})
        
        fig = go.Figure(data=go.Choropleth(
            locations=df['code'], # Spatial coordinates
            z = df['data'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = title,
        ))
        
        fig.update_layout(
            title_text = '2011 US Agriculture Exports by State',
            geo_scope='usa', # limite map scope to USA
        )
        fig.show()
        fig.write_image('path2save', format='png')