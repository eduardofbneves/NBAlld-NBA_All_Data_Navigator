from dash import Dash, dcc, html
import pandas as pd

def list_top_players(stats: pd.DataFrame, player: pd.DataFrame, 
                     condition: str, season: list[int]) -> html.Div:
    array = []
    filtered_df = stats[['season_id','player_id', condition]].sort_values(by=[condition], ascending=False)
    filtered_df = filtered_df[filtered_df['season_id'].isin(season)]
    filtered_df = player[player['id'].isin(filtered_df['player_id'].to_list()[:6])]
    for ind in range(5):
        array.append(html.Div(filtered_df.iloc[ind]['full_name']))
    return array
