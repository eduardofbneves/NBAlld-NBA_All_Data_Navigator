from dash import register_page, html, dcc, callback
from dash.dependencies import Input, Output
import pandas as pd

from utils.loader import load_dataframe
from components.dropdown_stats import dropdown_stats
#from components.line_graph import line_graph
from components.line_graph_copy import line_graph

register_page(__name__, path_template='/teams/<team_id>')


team = load_dataframe('team')
team_season_stats = load_dataframe('team_season_stats')
ids = team['id'].to_list()

def layout(team_id = None):
    #team = load_dataframe('team')
    #team_season_stats = load_dataframe('team_season_stats')
    #ids = team['id'].to_list()
    team_id = int(team_id)
    if team_id not in ids:
        return dcc.Location(pathname="/not_found_404")
        # TODO ver se os ids na team devem estar em str para nao dar erro
    team = team[team['id'] == team_id]
    team_season_stats = team_season_stats[team_season_stats['team_id'] == team_id]
    return html.Div(
        children = [
            dropdown_stats(team_season_stats, 'Dropdown test', 'drop_test', 'some'),
            #line_graph(team_season_stats, '', 'drop_test', 'line_graph'),
            dcc.Graph(id='line_graph')
            #dcc.Graph(figure=line_graph(),
            #          id="line_graph")
        ]
    )


@callback(
        Output("line_graph", "figure"),
        [Input('drop_test', "value")],
    )
def update_bar_chart(stats: list[str], team_id):
    filt = team_season_stats = team_season_stats[team_season_stats['team_id'] == team_id]
    return line_graph(filt, stats,
                       'drop_test', 'line')

