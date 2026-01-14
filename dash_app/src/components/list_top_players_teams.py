from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd

def list_top_players_teams(stats: pd.DataFrame, player: pd.DataFrame, 
                     condition: str, season: list[int], title: str) -> html.Div:
    array = []
    filtered_df = stats[['season_id','player_id', condition]].sort_values(by=[condition], ascending=False)
    filtered_df = filtered_df[filtered_df['season_id'].isin(season)]
    player_list = player[player['id'].isin(filtered_df['player_id'].to_list()[:6])] 
    array.append(html.H4(title))
    for ind in range(player_list.shape[0]):
        array.append(html.P(player_list.iloc[ind]['full_name']))
    return array
