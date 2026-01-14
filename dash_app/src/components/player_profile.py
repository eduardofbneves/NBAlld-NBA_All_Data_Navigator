from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from utils.check_nan_players import check_nan_players

def player_profile(player) -> html.Div:
    return html.Div(
        [
        
            # content
        html.Div(
            children=[
                
                dbc.Row([
                    html.H1('Player profile')
                ], class_name='header-description'),
            dbc.Row([
                dbc.Col([
                    html.H4('Photo'),
                       ], xs=2),
                
                dbc.Col([
                    dbc.Row([
                        html.H1(player.iloc[0,1])
                        ], className='header-title'
                    ),
                    dbc.Row([
                        html.H4('#' + check_nan_players(player.iloc[0]['jersey']) 
                                + ' ' + check_nan_players(player.iloc[0]['position']))
                    ], className='align-center'),
                ], xs=3),
                dbc.Col([
                    dbc.Row([
                            #html.Div(children=[html.P('Country:'), html.H5(player.iloc[0]['country'])]),
                            html.P(['Country', html.H4(check_nan_players(player.iloc[0]['country']))]),
                            html.P(['Height', html.H4(check_nan_players(player.iloc[0]['height']))]),
                            ]),                
                ], xs=1, class_name='player-header-text'),
                dbc.Col([

                    dbc.Row([
                            #html.Div(children=[html.P('Country:'), html.H5(player.iloc[0]['country'])]),
                            html.P(['Year started', html.H4(check_nan_players(player.iloc[0]['from_year']))]),
                            html.P(['Drafted', html.H4('R' + check_nan_players(player.iloc[0]['draft_round'])
                                                        + ' ' + check_nan_players(player.iloc[0]['draft_number']))]),
                    ]),
                ], xs=1, class_name='player-header-text'), 
                dbc.Col([
                    dbc.Row([
                        html.H4(player.iloc[0]['team_city']),  
                        html.H1(player.iloc[0]['team_name'])
                    ], className='player-header-text')
                ], xs=4)
            ], className='p-2 align-items-stretch'),
            ],
            className="header",
        ),

    ]
)



'''
html.P(
                    children=(
                        "Analyze the behavior of avocado prices and the number"
                        " of avocados sold in the US between 2015 and 2018"
                    ),
                    className="header-description",
                ),
'''