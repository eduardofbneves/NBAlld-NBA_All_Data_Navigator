# package imports
from dash import html, dcc, callback, Input, Output, State, register_page
import dash_bootstrap_components as dbc

from utils.loader import load_dataframe
from components.list_teams_home import list_teams_home
from components.dropdown_vals import dropdown_vals
from components.list_top_players import list_top_players

register_page(__name__, path='/')

team = load_dataframe('team')
season_ind = load_dataframe('season_ind')
player_season_stats = load_dataframe('player_season_stats')
player = load_dataframe('player')

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
        dbc.Row(
            [
                dbc.Col(html.H3('Top players')),
                dbc.Col(dropdown_vals(season_ind['season_str'], 'Pick season:',
                                      'drop-season-home', '')),
            ]
        ),
        dbc.Row(
            [
                dbc.Col('Points made'),
                dbc.Col('Assists'),
                dbc.Col('Rebounds'),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(id='pts-list'),
                dbc.Col(id='ast-list'),
                dbc.Col(id='rebs-list'),
            ]
            
        )
    ]
)

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
