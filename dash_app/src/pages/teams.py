from dash import register_page, html

from utils.loader import load_dataframe

register_page(__name__, path_template='/<team_id>')

def layout(team_id = None):
    return html.Div(
        children = [
            f"The user requested report ID: {team_id}."
        ]
    )