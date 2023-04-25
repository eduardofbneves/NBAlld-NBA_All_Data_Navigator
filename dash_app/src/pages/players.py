from dash import Dash, register_page, html, dcc
import os

from utils.loader import load_dataframe
register_page(__name__)

team = load_dataframe('team')

layout = html.Div(
    children=[
    html.H6("Team"),
    dcc.Dropdown(
        id='dropdown',
        options = [{"label": team, "value": team}for team in team['full_name'].to_list()],
        multi=True,
    ),
    ]
)
