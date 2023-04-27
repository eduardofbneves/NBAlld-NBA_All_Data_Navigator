from dash import html
import dash_bootstrap_components as dbc
import pandas as pd

def player_profile(player) -> html.Div:
    return html.Div(
        children=[
            html.Div(
                children=[
                    dbc.Row([
                        dbc.Col([
                            html.H3(player['last_name'])
                        ]),
                        dbc.Col([
                            html.H6(player['first_name'])
                        ])
                    ])
                ],
                style={'display': 'inline-block'}
            )
            
            
        ]
    )