from dash import register_page, html, dcc

from utils.loader import load_dataframe
from components.list_teams_home import list_teams_home
from components.team_profile import team_profile
from components.team_stats_view import team_stats_view

register_page(__name__, path_template='/team_view/<team_id>')

teams = load_dataframe('team')
team_season_stats = load_dataframe('team_season_stats')
ids = teams['id'].to_list()
player = load_dataframe('player')
player_season_stats = load_dataframe('player_season_stats')

def layout(team_id=None):
    if team_id == None:
        return html.Div([])
    team_id = int(team_id)
    if team_id==None:
        return list_teams_home(teams)
    elif team_id not in ids:
        return dcc.Location(pathname="/not_found_404")
    team = teams[teams['id'] == team_id]
    team_stats = team_season_stats[team_season_stats['team_id'] == team_id]
    return html.Div(
        children = [
            team_profile(team),
            team_stats_view(team, team_stats, player, player_season_stats)
        ]
    )
