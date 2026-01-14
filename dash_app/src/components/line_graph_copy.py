import plotly.express as px
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import pandas as pd



def line_graph(data: pd.DataFrame, title: str,
               options_id: str, graph_id: str) -> px.line():
    @callback(
        Output(graph_id, "figure"),
        [Input(options_id, "value")],
    )
    def update_bar_chart(stats: list[str]) -> px.line():
        if len(data) == 0:
            return None
        #filtered_data = data[stats]
        fig = px.line(data, 
                      x="season_id", 
                      y=stats)

        return fig

    return None
