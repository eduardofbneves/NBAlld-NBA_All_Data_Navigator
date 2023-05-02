from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

def player_profile(player) -> html.Div:
    return html.Div(
        [
            
            # content

        html.Div(

            children=[
        html.Div(
            children=[
                html.P(children="drena", className="header-emoji"),
                html.H1(
                    children="Avocado Analytics", className="header-title"
                ),
                html.P(
                    children=(
                        "Analyze the behavior of avocado prices and the number"
                        " of avocados sold in the US between 2015 and 2018"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        dbc.Row([
                html.H2('Player profile')
                ], className='text-center'),
            dbc.Row([
                dbc.Col([
                    html.H4('Photo'),
                       ], xs=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4(player['full_name'])
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
        ]
    )
    ]
)
