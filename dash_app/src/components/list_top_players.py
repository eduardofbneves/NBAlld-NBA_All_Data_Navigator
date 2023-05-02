from dash import Dash, dcc, html
import pandas as pd

def list_top_players(stats: pd.DataFrame, player: pd.DataFrame, 
                     condition: str, season: list[int]) -> html.Div:
    array = []
    filtered_df = stats[['season_id','player_id', condition]].sort_values(by=[condition])
    filtered_df = filtered_df[filtered_df['season_id'] == season]
    filtered_df = player[filtered_df['player_id']]
    for ind in range(5):
        array.append(html.Div(html(filtered_df.iloc[ind]['full_name'])))
    return array
