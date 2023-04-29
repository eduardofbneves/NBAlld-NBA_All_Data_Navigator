from dash import Dash, dcc, html
import pandas as pd

def list_teams_home(data: pd.DataFrame, condition: str) -> html.Div:
    array = []
    for ind, item in data[data['team_division'] == condition].iterrows():
        array.append(html.Div(html.A(item.loc['full_name'], 
                                     href='/teams/'+str(item['id']))))
    return array
