from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

from utils.loader import load_dataframe
from components.player_profile import player_profile

register_page(__name__, path='/players')

player_info = load_dataframe('player')
player = player_info.loc[player_info['id'] == 51]

layout = player_profile(player)