import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd



def render(app: Dash, data: list[pd.DataFrame]) -> px.line():
    fig = px.line()
    @app.callback(
        Output("line_graph", "children"),
        Input("dropdown", "value"),
        Input("stats_dropdown", "value"),
    )
    def update_bar_chart(full_name: list[str], stats: list[str]) -> px.line():
        print(full_name, stats)
        if len(data) == 0:
            return html.Div("No data selected.", id="line_chart")
        table = data[1]
        team_id = data[0].loc[data[0]['full_name'].isin(full_name)]
        filtered_data = table.loc[table['team_id'].isin(team_id['id'].tolist())]
        fig = px.line(filtered_data, 
                      x="season_id", 
                      y=stats)

        return html.Div(dcc.Graph(figure=fig), id="line_graph")

    return html.Div(id="line_graph")
