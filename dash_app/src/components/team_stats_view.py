from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from components.list_top_players_teams import list_top_players_teams
from utils.check_nan_players import check_nan_players
from utils.global_vars import ALL_SEASONS


def team_stats_view(team, team_stats, player, player_season_stats) -> html.Div:
    '''
    pts_fig = go.Figure()
    fig.add_trace(go.Bar(
        y=['fg2', 'fg3', 'ft']
    ))
    '''
    players = player[player['team_id']==team.iloc[0,0]]
    player_stats = player_season_stats[player_season_stats['player_id'].isin(players['id'].tolist())]
    print(players, player_stats)
    return html.Div(
        [

    html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                            html.Div(list_top_players_teams(player_stats, player, 
                                    'nmr_games', ALL_SEASONS, 'Top Players'),)
                ])
            ])


        ], xs=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    
                ])
            ], className='h-100 text-center')
        ], xs=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([

                ])
            ], className='h-100 text-center')
        ], xs=4)
    ], className='p-2 align-items-stretch'),
    # content
])

    ]
)
    
'''
dict(
                                        r=player_stats[['pts_home','ast_home', 'miss', 'blk_home', 'reb_home']].sum(axis=0).tolist(),
                                        theta=['pts_home','ast_home', 'miss', 'blk_home', 'reb_home']
                                    ),
                                    '''