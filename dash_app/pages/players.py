from dash import Dash, register_page, html, dcc
import os

from . import loader
register_page(__name__)


def layout():
     return html.Div(
          children=[
            html.H6("Team"),
            dcc.Dropdown(
                id='dropdown',
                options = [{"label": team, "value": team}for team in team['full_name'].to_list()],
                #options=[{"label": year, "value": year} for year in all_nations],
                #value=all_nations,
                multi=True,
            ),
        ]
     )