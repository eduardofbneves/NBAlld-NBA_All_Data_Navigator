from dash import register_page, html, dcc
import pandas as pd

from utils.loader import load_dataframe
from components.list_teams_home import list_teams_home
from components.team_profile import team_profile
from components.team_stats_view import team_stats_view

register_page(__name__, path_template='/team_view/<team_id>')

team = load_dataframe('team')
team_season_stats = load_dataframe('team_season_stats')
ids = team['id'].to_list()

def layout(team_id=None, **kwargs):
    if team_id == None:
        return html.Div([])
    team = load_dataframe('team')
    team_season_stats = load_dataframe('team_season_stats')
    player = load_dataframe('player')
    player_season_stats = load_dataframe('player_season_stats')
    ids = team['id'].to_list()
    team_id = int(team_id)
    if team_id==None:
        return list_teams_home(team)
    elif team_id not in ids:
        return dcc.Location(pathname="/not_found_404")
        # TODO ver se os ids na team devem estar em str para nao dar erro
    team = team[team['id'] == team_id]
    team_stats = team_season_stats[team_season_stats['team_id'] == team_id]
    return html.Div(
        children = [
            team_profile(team),
            team_stats_view(team, team_stats, player, player_season_stats)
        ]
    )
