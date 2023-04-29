from dash import register_page, html
import dash_core_components as dcc
import pandas as pd

from utils.loader import load_dataframe
from components.dropdown_stats import dropdown_stats

register_page(__name__, path_template='/teams/<team_id>')

'''
team = load_dataframe('team')
ids = team['id'].to_list()
'''

def layout(team_id = None):
    team = load_dataframe('team')
    ids = team['id'].to_list()
    team_id = int(team_id)
    if team_id not in ids:
        return dcc.Location(pathname="/not_found_404")
        # TODO ver se os ids na team devem estar em str para nao dar erro
    team = team[team['id'] == team_id]
    return html.Div(
        children = [
            dropdown_stats(team, 'Dropdown test', 'drop_test', 'some')
        ]
    )