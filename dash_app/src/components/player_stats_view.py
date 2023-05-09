from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from utils.check_nan_players import check_nan_players

def player_profile(player) -> html.Div:
    return html.Div(
        [

    html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Dash Tabs component 1')
                ])
            ], className='text-center'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Dash Tabs component 2')
                        ])
                    ], className='text-center')
                ])
            ], className='pt-1')
        ], xs=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Dash Tabs component 3'),
                    html.H4('Dash Tabs component 4')
                ])
            ], className='h-100 text-center')
        ], xs=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Dash Tabs component 5')
                ], className='text-center')
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Dash Tabs component 6')
                        ], className='text-center')
                    ])
                ], xs=6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Dash Tabs component 7')
                        ], className='text-center')
                    ])
                ], xs=6)
            ], className='pt-1')
        ], xs=4)
    ], className='p-2 align-items-stretch'),
    # content
])

    ]
)