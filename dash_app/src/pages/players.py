from dash import Dash, register_page, html, dcc
import dash_bootstrap_components as dbc
import os

from utils.loader import load_dataframe
from components.player_profile import player_profile

register_page(__name__, path='/players')

player_info = load_dataframe('common_player_info')
player = player_info.loc[player_info['person_id'] == 51]

layout = html.Div(
    [
        dbc.Row(dbc.Col(html.H3('East Conference'))),
        dbc.Row(
            [
                dbc.Col(),
                dbc.Col(),
                dbc.Col(),
            ]
        ),
        dbc.Row(dbc.Col(html.H3('West Conference'))),
        dbc.Row(
            [
                dbc.Col(),
                dbc.Col(),
                dbc.Col(),
            ]
        ),
    ]
)