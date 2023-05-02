from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output
import pandas as pd


def dropdown_stats(data: pd.DataFrame, title: str,
                  drop_id: str, out_id: str) -> html.Div:
    @callback(
            Output(drop_id, 'value')
    )
    def select_team_stats(stat):
        return stat

    return html.Div(
        children=[
            html.H6(title),
            dcc.Dropdown(
                id=drop_id,
                options = [{"label": stat, "value": stat}for stat in data.columns[2:]],
                #options=[{"label": year, "value": year} for year in all_nations],
                value=data.columns,
                multi=True,
            ),
        ]
    )
