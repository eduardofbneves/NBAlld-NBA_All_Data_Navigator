from dash import register_page, html, dcc, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

from utils.loader import load_dataframe
from components.player_profile_compare import player_profile_compare
from components.player_stats_compare import player_stats_compare

register_page(__name__, path_template='/compare_players/<player1_id>')

player = load_dataframe('player')
player_season_stats = load_dataframe('player_season_stats')

# TODO so as paginas com /id e que fazem esta cena de crescer
def layout(player1_id=None, **kwargs):
    if player1_id == None:
        return html.Div([])
    player1_id = int(player1_id)
    player1 = player[player['id'] == player1_id]
    player1_stats = player_season_stats[player_season_stats['player_id'] == player1_id]   
    
    return html.Div([
        dbc.Row([
            dcc.Dropdown(
                id='player2-drop',
                options=[{'label':player, 'value':player} for player in player['full_name'].to_list()],
                value = []
            ),
        ]),
        dbc.Row([
            dbc.Col([
                player_profile_compare(player1),
            ],xs=6),
            dbc.Col([
                html.Div(id='player2-profile')
            ],xs=6)
            
        ]),
        dbc.Row([
            dbc.Col([
                player_stats_compare(player1_stats),
            ],xs=6),
            dbc.Col([
                html.Div(id='player2-stats')
            ],xs=6)            
        ])
    ], className='url-support-page-div')


@callback(
    Output('player2-profile', 'children'),
    Output('player2-stats', 'children'),
    Input('player2-drop', 'value')
)
def update_player2(player_name):
    if len(player_name) == 0 or player_name == None:
        return html.Div([
            dbc.Col([
                dbc.Row([
                    html.H1('Choose Player to Compare'),
                ], className='header-title'),
            ], className='header-compare'),
        ]), html.Div()
    player2 = player[player['full_name'] == player_name]
    player2_stats = player_season_stats[player_season_stats['player_id'] == player2.iloc[0]['id']] 
    return player_profile_compare(player2), player_stats_compare(player2_stats)

