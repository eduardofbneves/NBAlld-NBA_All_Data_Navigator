from dash import html, dcc, register_page, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from utils.loader import load_dataframe
from components.player_profile import player_profile
from components.dropdown_list import dropdown_list
from components.dropdown_vals import dropdown_vals
from components.player_stats_view import player_stats_view
from components.season_stats import season_stats
from components.list_top_players import list_top_players
from components.list_top_players_conditions import list_top_players_conditions

register_page(__name__, path='/seasons')

team = load_dataframe('team')
team_season_stats = load_dataframe('team_season_stats')
player = load_dataframe('player')
player_season_stats = load_dataframe('player_season_stats')
season_ind = load_dataframe('season_ind')
#player = player_info.loc[player_info['id'] == 51]

layout = html.Div([
    html.Div([
        # show team_season_stats
        html.P('Pick seasons:'),
        dcc.RangeSlider(season_ind.iloc[0, 0]-20000, 
                        season_ind.iloc[-2, 0]-20000, 1,
                        value=[season_ind.iloc[0, 0]-20000, 
                               season_ind.iloc[-2, 0]-20000],
                        marks=dict(zip(list(range(season_ind.iloc[0, 0]-20000,
                                                  season_ind.iloc[-1, 0]-20000)), 
                                       season_ind['season_str'].tolist())), 
                        allowCross=False, id='season-picker-season'),
        html.Div(id='season-profile'),
        dcc.Checklist(['home', 'away'], ['home', 'away'], 
                      id='check',
                      labelStyle={"display": "flex", "align-items": "center"},),
        html.Div(id='check-board', className='list-players-seasons')
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
    Input('season-picker-season', 'value')
)
def update_check(vals, seasons):
    if seasons is None:
        return season_stats(team, team_season_stats, player, player_season_stats)
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
    
'''
dbc.Row(
            [
                dbc.Col(html.H3('Points made')),
                dbc.Col(html.H3('Assists')),
                dbc.Col(html.H3('Rebounds')),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(id='pts-list'),
                dbc.Col(id='ast-list'),
                dbc.Col(id='rebs-list'),
            ]
            
        )
        
 dbc.Row(
            [
                dbc.Col(html.H3('Top players')),
                dbc.Col(dropdown_vals(season_ind['season_str'], 'Pick season:',
                                      'drop-season-home', '')),
            ]
        ),


@callback(Output('pts-list', 'children'), 
          Output('ast-list', 'children'),
          Output('rebs-list', 'children'),
          Input('drop-season-home', 'value'),)
        
def update_season(season):
    if season == None:
        season = season_ind['season_id'].unique()
    elif season == []:
        season = season_ind['season_id'].unique()
    else:
        season = season_ind[season_ind['season_str'].isin(season)]['season_id'].to_list()
    div1 = list_top_players(player_season_stats, player, 'pts_home', season)
    div2 = list_top_players(player_season_stats, player,'ast_home', season)
    div3 = list_top_players(player_season_stats, player,'reb_home', season)
    return div1, div2, div3

'''
