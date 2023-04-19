from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from ..data.loader import load_dataframe, path_to_data
from . import ids


def render(app: Dash, team: pd.DataFrame) -> html.Div:
    '''
    @app.callback(
        Output("dropdown", "value"),
        #Input(ids.SELECT_ALL_NATIONS_BUTTON, "n_clicks"),
    )
    def select_team_id():
        return options
    '''

    return html.Div(
        children=[
            html.H6("Team"),
            dcc.Dropdown(
                id='dropdown',
                options = [{"label": team, "value": team}for team in team['full_name'].to_list()],
                #options=[{"label": year, "value": year} for year in all_nations],
                #value=all_nations,
                multi=True,
            ),
        ]
    )
