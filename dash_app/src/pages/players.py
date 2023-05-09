from dash import html, dcc, register_page, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from utils.loader import load_dataframe
from components.player_profile import player_profile
from components.dropdown_list import dropdown_list
from components.dropdown_vals import dropdown_vals

register_page(__name__, path='/players')

player_info = load_dataframe('player')
team = load_dataframe('team')
player_season_stats = load_dataframe('team_season_stats')
#player = player_info.loc[player_info['id'] == 51]
print(player_info.info())

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dropdown_list(team['full_name'].to_list(), 'player-pick-team', 'Pick by team'),
        ]),
        dbc.Col([
            dropdown_list(player_info['position'].unique(), 'player-pick-position', 'Pick by postition'),
        ]),
    ]),
   dbc.Row([
       dcc.Dropdown(
            id='player-drop',
            options=[{'label':player, 'value':player} for player in player_info['full_name'].to_list()],
            value = []
            ),
   ]),
    #player_profile(player)
    html.Div(id='player-header'),
    html.Div(id='player-graphs')
    
])

@callback(
    Output('player-drop', 'options'),
    Input('player-pick-team', 'value'),
    Input('player-pick-position', 'value'),
)
def update_page(team_name = team['full_name'].to_list(), position = team['full_name'].to_list()):
    players_picked = player_info.copy()
    if type(team_name) != list or len(team_name) == 0:
        team_name = team['full_name'].to_list()
    if type(position) != list:
        position = player_info['position'].unique()
    print(team_name, )
    team_name = team.loc[team['full_name'].isin(team_name)]['abbreviation'].to_list()
    players_picked = players_picked[players_picked['team_abbreviation'].isin(team_name)]
    print(team_name, team_name, position)
    players_picked = players_picked[players_picked['position'].isin(position)]
    print(players_picked.head())
    return [{'label': i, 'value': i} for i in players_picked['full_name'].to_list()]

@callback(
    Output('player-header', 'children'),
    Input('player-drop', 'value')
)
def update_page(player_name):
    player = player_info[player_info['full_name'] == player_name]
    return player_profile(player)