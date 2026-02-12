from dash import html, dcc, register_page, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from utils.loader import load_dataframe
from components.player_profile import player_profile
from components.dropdown_list import dropdown_list
from components.player_stats_view import player_stats_view

register_page(__name__, path='/players')

player_info = load_dataframe('player')
team = load_dataframe('team')
player_season_stats = load_dataframe('player_season_stats')
season_ind = load_dataframe('season_ind')

layout = html.Div([
    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dropdown_list(team['full_name'].to_list(), 'player-pick-team', 'Pick by team',
                    #value='Los Angeles Lakers'
                    ),
                ]),
                dbc.Col([
                    dropdown_list(player_info['position'].unique(), 'player-pick-position', 'Pick by postition',
                    #value='Forward'
                    ),
                ]),
            ]),
            dbc.Row([
                dcc.Dropdown(
                        id='player-drop',
                        options=[{'label':player, 'value':player} for player in player_info['full_name'].to_list()],
                        value='LeBron James'
                        ),
            ]),
        ])
    ]),
        
    html.Div(id='player-header'),
    dcc.Store(id='player-store'),
    dcc.RangeSlider(season_ind.iloc[0, 0]-20000, 
                        season_ind.iloc[-2, 0]-20000, 1,
                        value=[season_ind.iloc[0, 0]-20000, 
                            season_ind.iloc[-2, 0]-20000],
                        marks=dict(zip(list(range(season_ind.iloc[0, 0]-20000,
                                                season_ind.iloc[-1, 0]-20000)), 
                                    season_ind['season_str'].tolist())), 
                        allowCross=False, 
                        id='season-picker'),
    html.Div(id='player-graphs')
        
])

@callback(
    Output('player-drop', 'options'),
    Input('player-pick-team', 'value'),
    Input('player-pick-position', 'value'),
)
def update_page(
    team_name = team['full_name'].to_list(), 
    position = team['full_name'].to_list()
):
    # TODO players with nan vals
    players_picked = player_info.copy()
    if team_name == None and position == None:
        return [{'label': i, 'value': i} for i in players_picked['full_name'].to_list()]
    if team_name == [] and position == []:
        return [{'label': i, 'value': i} for i in players_picked['full_name'].to_list()]
    if type(team_name) != list or len(team_name) == 0:
        team_name = team['full_name'].to_list()
    if type(position) != list or len(position) == 0:
        position = player_info['position'].unique()
    team_name = team.loc[team['full_name'].isin(team_name)]['abbreviation'].to_list()
    players_picked = players_picked[players_picked['team_abbreviation'].isin(team_name)]
    players_picked = players_picked[players_picked['position'].isin(position)]
    return [{'label': i, 'value': i} for i in players_picked['full_name'].to_list()]

@callback(
    Output('player-header', 'children'),
    #Output('player-graphs', 'children'),
    Output('player-store', 'data'),
    Input('player-drop', 'value')
)
def update_page(player_name):
    if player_name == None:
        return html.Div(html.H1('Choose a player'))
    player = player_info[player_info['full_name'] == player_name]
    return player_profile(player), player.iloc[0,:].to_list()
#, player_stats_view(player, player_stats, season_ind)


@callback(
    Output('season-picker', 'min'),
    Output('season-picker', 'max'),
    Input('player-store', 'data')
)
def update_seasons(player_picked):
    player_seasons = player_season_stats[
        player_season_stats['player_id'] == player_picked[0]]
    return player_seasons['season_id'].min()-20000, player_seasons['season_id'].max()-20000


@callback(
    Output('player-graphs', 'children'),
    Input('season-picker', 'value'),
    Input('player-store', 'data')
)
def player_graphs(seasons, player_list):
    if seasons is None:
        player_stats = player_season_stats[player_season_stats['player_id'] == 
                                       player_list[0]]
        return player_stats_view(player_list, player_stats)
    seasons = list(range(seasons[0]+20000, seasons[1]+20001))
    player_stats = player_season_stats[player_season_stats['player_id'] ==  player_list[0]]
    player_stats = player_stats[player_stats['season_id'].isin(seasons)]
    return player_stats_view(player_list, player_stats)