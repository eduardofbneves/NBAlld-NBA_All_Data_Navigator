from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from utils.check_nan_players import check_nan_players

def team_profile(team) -> html.Div:
    return html.Div(
        [
        
            # content
        html.Div(
            children=[
                
                dbc.Row([
                    html.H1('Team profile')
                ], class_name='header-description'),
            dbc.Row([
                dbc.Col([
                    html.H4('Icon'),
                       ], xs=2),
                
                dbc.Col([
                    dbc.Row([
                        html.H4(team.iloc[0]['city'])
                    ], className='align-center'),
                    dbc.Row([
                        html.H1(team.iloc[0]['nickname'])
                        ], className='header-title'
                    ),
                ], xs=3),
                dbc.Col([
                    dbc.Row([
                         dbc.Col([
                            #html.Div(children=[html.P('Country:'), html.H5(player.iloc[0]['country'])]),
                            [html.H2(team.iloc[0]['abbreviation'])],
                        ], xs=1),
                        dbc.Col([
                            #html.Div(children=[html.P('Country:'), html.H5(player.iloc[0]['country'])]),
                            html.P(['State', html.H4(team.iloc[0]['state'])]),
                        ]),
                        dbc.Col([
                            html.P(['Conference and Division', html.H4(html.H4(team.iloc[0]['team_conference'] + ' ' +
                               team.iloc[0]['team_division']))]),
                        ]),

                    ]),
                ], class_name='player-header-text'),
            ], className='player-header-text'),
            ],
            className="header-teams",
        ),
        

    ]
)