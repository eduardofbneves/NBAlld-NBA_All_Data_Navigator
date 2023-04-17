from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import load_dataframe
from . import ids


def render(app: Dash) -> html.Div:
    path = "../data/team_season_stats.csv"
    df = load_dataframe(path)

    '''
    @app.callback(
        Output(ids.NATION_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_NATIONS_BUTTON, "n_clicks"),
    )
    '''

    return html.Div(
        children=[
            html.H6("Team"),
            dcc.Dropdown(
                id='team_dropdown',
                options = [{"label": team, "value": team}for team in df['team_id'].to_list()],
                #options=[{"label": year, "value": year} for year in all_nations],
                #value=all_nations,
                multi=True,
            ),
        ]
    )
