# package imports
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc

from utils.loader import load_dataframe
from components.list_teams_home import list_teams_home

register_page(__name__, path='/')

team = load_dataframe('team')

layout = html.Div(
    [
        dbc.Row(dbc.Col(html.H3('East Conference'))),
        dbc.Row(
            [
                dbc.Col(list_teams_home(team, 'Atlantic')),
                dbc.Col(list_teams_home(team, 'Central')),
                dbc.Col(list_teams_home(team, 'Southeast')),
            ]
        ),
        dbc.Row(dbc.Col(html.H3('West Conference'))),
        dbc.Row(
            [
                dbc.Col(list_teams_home(team, 'Northwest')),
                dbc.Col(list_teams_home(team, 'Pacific')),
                dbc.Col(list_teams_home(team, 'Southwest')),
            ]
        ),
    ]
)

@callback(Output('content', 'children'), Input('radios', 'value'))
def home_radios(value):
    return f'You have selected {value}'
