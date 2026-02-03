from dash import html, dcc, register_page, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from utils.loader import load_dataframe
from components.season_stats import season_stats
from components.list_top_players import list_top_players
from components.list_top_players_conditions import list_top_players_conditions

register_page(__name__, path='/seasons')

team = load_dataframe('team')
team_season_stats = load_dataframe('team_season_stats')
player = load_dataframe('player')
player_season_stats = load_dataframe('player_season_stats')
season_ind = load_dataframe('season_ind')

layout = html.Div([
    html.Div([
         dbc.Card([
            dbc.CardBody([
                html.H4('Pick season range:'),
                dcc.RangeSlider(
                    season_ind.iloc[0, 0]-20000, 
                    season_ind.iloc[-2, 0]-20000, 
                    1, 
                    value=[
                        season_ind.iloc[0, 0]-20000, 
                        season_ind.iloc[-2, 0]-20000
                    ],
                    marks=dict(zip(list(
                        range(
                            season_ind.iloc[0, 0]-20000,
                            season_ind.iloc[-1, 0]-20000)
                        ), 
                        season_ind['season_str'].tolist()
                    )), 
                    allowCross=False, 
                    id='season-picker-season'
                ),
            ])
        ]),
        html.Div(id='season-profile'),
        dbc.Card([
            dbc.CardBody([
                html.H2("Best Stats Players home and away", id='center'),
                dcc.Checklist(
                    ['home', 'away'], 
                    value=['home', 'away'], 
                    id='check',
                    labelStyle={
                        "display": "flex", 
                        "align-items": "center"
                    },
                    inline=True
                ),
                html.Div(id='check-board', className='list-players-seasons')
            ])
        ]),        
    ]),
])


@callback(
    Output('season-profile', 'children'),
    Input('season-picker-season', 'value')
)
def update_season_page(seasons):
    if seasons is None:
        return season_stats(team, team_season_stats, player, player_season_stats)
    seasons = list(range(seasons[0]+20000, seasons[1]+20001))
    team_stats = team_season_stats[team_season_stats['season_id'].isin(seasons)]
    team_stats = team_stats.groupby(['team_id'], as_index=False).mean()
    player_stats = player_season_stats[player_season_stats['season_id'].isin(seasons)]
    player_stats = player_stats.groupby(['player_id'], as_index=False).mean()
    return season_stats(team, team_stats, player, player_stats)

@callback(
    Output('check-board', 'children'),
    Input('check', 'value'),
    State('season-picker-season', 'value')
)
def update_check(vals, seasons):
    seasons = list(range(seasons[0]+20000, seasons[1]+20001))
    if len(vals) == 0:
        return html.P('Select ground')
    elif len(vals) == 1 and vals[0]=='home':
        return dbc.Row([dbc.Col(list_top_players(player_season_stats, 
                                player, 'fg2_pts_home', seasons, 'Two pointers')),
                    dbc.Col(list_top_players(player_season_stats, 
                                player, 'fg3_pts_home', seasons, 'Three pointers')),
                    dbc.Col(list_top_players(player_season_stats, 
                                player, 'ast_home', seasons, 'Assists'))])

    elif len(vals) == 1 and vals[0]=='away':
        return dbc.Row([dbc.Col(list_top_players(player_season_stats, 
                                player, 'fg2_pts_away', seasons, 'Two pointers')),
                    dbc.Col(list_top_players(player_season_stats, 
                                player, 'fg3_pts_away', seasons, 'Three pointers')),
                    dbc.Col(list_top_players(player_season_stats, 
                                player, 'ast_away', seasons, 'Assists'))])
    else:
        return dbc.Row([dbc.Col(list_top_players_conditions(player_season_stats, 
                                           player, ['fg2_pts_home', 'fg2_pts_away'], seasons, 'Two pointers')),
                        dbc.Col(list_top_players_conditions(player_season_stats, 
                                           player, ['fg3_pts_home', 'fg3_pts_away'], seasons, 'Three pointers')),
                        dbc.Col(list_top_players_conditions(player_season_stats, 
                                           player, ['ast_home', 'ast_away'], seasons, 'Assist'))])
