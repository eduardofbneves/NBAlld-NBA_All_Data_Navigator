from dash import Dash, dcc, html
import pandas as pd

def list_teams_home(data: pd.DataFrame, condition = None) -> html.Div:
    array = [condition]
    if condition == None:
        for ind, item in data.iterrows():
            array.append(html.Div(html.A(item.loc['full_name'], 
                                     href='/team_view/'+str(item['id']))))
    else:
        for ind, item in data[data['team_division'] == condition].iterrows():
            array.append(html.Div(html.A(item.loc['full_name'], 
                                        href='/team_view/'+str(item['id']))))
    return array
