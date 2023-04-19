from dash import Dash, html
import pandas as pd
import plotly.express as px
from . import dropdown_example, dropdown_stats, line_graph


def create_layout(app: Dash, data: list[pd.DataFrame]) -> html.Div:
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    return html.Div(
        className="app-div",
        
        children=[
            html.H1(app.title),
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
            html.Div(
                className="line",
                children=[
                    line_graph.render(app, data),   
                ],
            ),
            #line_graph.render(app, data),
            
            
            
        ],
    )
