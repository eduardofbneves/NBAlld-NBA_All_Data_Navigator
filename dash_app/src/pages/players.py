from dash import Dash, register_page, html, dcc
import os

from utils.loader import load_dataframe
from components.player_profile import player_profile

register_page(__name__, path='/players')

player_info = load_dataframe('common_player_info')
player = player_info.loc[player_info['person_id'] == 51]

layout = html.Div(
    children=[
        player_profile(player)
    ]
)
