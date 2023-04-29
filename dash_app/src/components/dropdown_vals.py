from dash import dcc, html, callback
from dash.dependencies import Input, Output
import pandas as pd



def dropdown_vals(data: pd.DataFrame, title: str,
                  drop_id: str, out_id: str) -> html.Div:
    @callback(
        Output(out_id, "value"),
    )
    def select_team_id():
        return options
    
    return html.Div(
        children=[
            html.H6(title),
            dcc.Dropdown(
                id=drop_id,
                options = [{"label": data, "value": data}for data in data.to_list()],
                multi=True,
            ),
        ]
    )
