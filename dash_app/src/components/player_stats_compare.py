from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

from utils.check_nan_players import check_nan_players
from utils.global_vars import PLAYER_STATS_INDEXES

def player_stats_compare(player, player_stats) -> html.Div:
    '''
    pts_fig = go.Figure()
    fig.add_trace(go.Bar(
        y=['fg2', 'fg3', 'ft']
    ))
    '''
    years = np.subtract(player_stats['season_id'].tolist(),20000)
    line_fig = go.Figure()
    line_fig.add_trace(go.Scatter(x=years,
                                  y=player_stats['nmr_games'].tolist(),
                                  mode='lines+markers'))
    
    stats = player_stats[['pts_home','ast_home', 'miss', 'blk_home', 'reb_home']].mean(axis=0).tolist()
    stats_index = []
    for i in range(len(stats)):
        stats_index.append(stats[i]/PLAYER_STATS_INDEXES[i])
    stats_index
    
    radial_fig = go.Figure()
    radial_fig.add_trace(go.Scatterpolar(
                            r = stats_index,
                            theta=['pts_home','ast_home', 'miss', 'blk_home', 'reb_home'],                   
                            fill='toself'))
    radial_fig.update_polars(radialaxis=dict(range=[0, 6]))
    radial_fig.update_layout(dict(polar=dict(
        radialaxis=dict(visible=True, range=[0,6]))))

    return html.Div([
        dbc.Row([
            dbc.Card([
                dbc.CardBody([
                    html.H3('Games per seasons'),
                    dcc.Graph(figure = line_fig)
                ], className='text-center')
            ]),
        ]),
        dbc.Row([
            dbc.Card([
                dbc.CardBody([
                    html.H3('Player radial profile'),
                    dcc.Graph(
                        figure=go.Figure(data=go.Scatterpolar(
                            r = stats_index,
                            theta=['pts_home','ast_home', 'miss', 'blk_home', 'reb_home'],                   
                            fill='toself'
                        ))
                    )
                ], className='text-center')
            ])
        ]),
    ])
    
'''
dict(
                                        r=player_stats[['pts_home','ast_home', 'miss', 'blk_home', 'reb_home']].sum(axis=0).tolist(),
                                        theta=['pts_home','ast_home', 'miss', 'blk_home', 'reb_home']
                                    ),
                                    '''