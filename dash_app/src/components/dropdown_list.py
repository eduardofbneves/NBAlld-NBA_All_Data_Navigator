from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from utils.loader import load_dataframe


def dropdown_vals(list: list[str], chart_id: str, title: str) -> html.Div:
    return html.Div(
        children=[
            html.H6(title),
            dcc.Dropdown(
                id=chart_id,
                options = [{"label": data, "value": data}for data in list],
                multi=True,
            ),
        ]
    )
