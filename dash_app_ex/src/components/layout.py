import dash
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from . import dropdown_example, dropdown_stats, line_graph


def create_layout(app: Dash, data: list[pd.DataFrame]) -> html.Div:
    return html.Div(
        className="app-div",
        
        children=[
            html.H1(app.title),
            html.Div(
                [
                    html.Div(
                        dcc.Link(
                            f"{page['name']} - {page['path']}", href=page["relative_path"]
                        )
                    )
                    for page in dash.page_registry.values()
                ]
            ),
            html.Hr(),
            html.Div(
                className="dropdown",
                children=[
                    dropdown_example.render(app, data[0]),
                ],
            ),
            html.Div(
                className="stats_dropdown",
                children=[
                    dropdown_stats.render(app, data[1]),   
                ],
            ),
            html.H4('stats per season'),
            line_graph.render(app, data),
            
            
        ],
    )
