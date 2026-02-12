from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd

def list_top_players_teams(
        stats: pd.DataFrame, 
        player: pd.DataFrame, 
        condition: str, 
        title: str
    ) -> html.Div:
    array = []
    filtered_df = stats[[
        'player_id', 
        condition
    ]]
    filtered_df = filtered_df.groupby(['player_id'], as_index=False).sum().sort_values(by=[condition], ascending=False)
    player_list = player[
        player['id'].isin(filtered_df['player_id'].to_list()[:5])
    ] 
    array.append(html.H4(title))
    for ind in range(player_list.shape[0]):
        array.append(html.P(player_list.iloc[ind]['full_name'] + ' - ' + \
                            str(filtered_df.iloc[ind][condition])))
    return array
