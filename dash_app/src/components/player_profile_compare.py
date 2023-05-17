from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from utils.check_nan_players import check_nan_players

def player_profile_compare(player) -> html.Div:
    return html.Div([
        dbc.Col([
            dbc.Row([
            html.H1(player.iloc[0]['full_name'])
                ], className='header-title'
            ),
            dbc.Row([
                html.H4('#' + check_nan_players(player.iloc[0]['jersey']) 
                        + ' ' + check_nan_players(player.iloc[0]['position']))
            ], className='align-center'),
        ], className='header-compare'),
    ])



'''
html.P(
                    children=(
                        "Analyze the behavior of avocado prices and the number"
                        " of avocados sold in the US between 2015 and 2018"
                    ),
                    className="header-description",
                ),
'''