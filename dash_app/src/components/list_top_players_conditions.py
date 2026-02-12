from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

def list_top_players_conditions(
        stats: pd.DataFrame, 
        player: pd.DataFrame, 
        condition: list[str], 
        season: list[int], 
        title: str
    ) -> list:
    array = []
    summed = stats[[condition[0], condition[1]]].sum(axis=1).tolist()
    filtered_df = stats[['season_id', 'player_id']]
    filtered_df.insert(2, 'col', summed)
    filtered_df = filtered_df.sort_values(by=['col'], ascending=False)
    filtered_df = filtered_df[filtered_df['season_id'].isin(season)].reset_index()
    player = player.rename(columns={'id': 'player_id'})
    filtered_df = pd.merge(filtered_df, player[['player_id','full_name']], on = 'player_id', how = 'left')
    array.append(html.H4(title))
    for ind in range(5):
        array.append(html.P(
            str(filtered_df.iloc[ind]['season_id']-20000) + ' - ' + \
            filtered_df.iloc[ind]['full_name'] + ' - ' + \
            str(round(filtered_df.iloc[ind]['col']))
        ))
    return array

