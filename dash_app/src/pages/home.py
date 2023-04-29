# package imports
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc

from utils.loader import load_dataframe

register_page(__name__, path='/')



layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col([html.Div("One of three columns"),
                        html.Div("Col")]),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
    ]
)

@callback(Output('content', 'children'), Input('radios', 'value'))
def home_radios(value):
    return f'You have selected {value}'
