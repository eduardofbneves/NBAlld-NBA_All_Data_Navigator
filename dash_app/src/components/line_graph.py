import plotly.express as px
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import pandas as pd



def line_graph(data: list[pd.DataFrame], stats: list[str],
               options_id: str, graph_id: str) -> px.line():
    
    if len(data) == 0:
        return html.Div("No data selected.", id=graph_id)
    #filtered_data = data[stats]
    fig = px.line(data, 
                    x="season_id",
                    y=stats)

    return fig

