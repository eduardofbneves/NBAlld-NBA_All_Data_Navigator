from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from ..data.loader import load_dataframe, path_to_data
from . import ids


def render(app: Dash, team_season_stats: pd.DataFrame) -> html.Div:
    
    def select_team_stats():
        return options

    return html.Div(
        children=[
            html.H6("Stats"),
            dcc.Dropdown(
                id='stats_dropdown',
                options = [{"label": stat, "value": stat}for stat in team_season_stats.columns[2:]],
                #options=[{"label": year, "value": year} for year in all_nations],
                value=team_season_stats.columns,
                multi=True,
            ),
        ]
    )
