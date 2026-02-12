from dash import html
import pandas as pd

def list_top_players(
        stats: pd.DataFrame, 
        player: pd.DataFrame, 
        condition: str, 
        seasons: list[int], 
        title: str
    ) -> list:
    """List top players on average per season for doubles, triples and assists given home/away and the seasons selected

    Args:
        stats (pd.DataFrame): player stats per season
        player (pd.DataFrame): dataframe with the player characteristics
        condition (str): column name to compare
        seasons (list[int]): seasons bound selected
        title (str): Title of the column

    Returns:
        list: html elemnts list to present
    """    
    array = []
    filtered_df = stats[[
        'season_id',
        'player_id', 
        condition]].sort_values(
            by=[condition], 
            ascending=False
        )
    filtered_df = filtered_df[filtered_df['season_id'].isin(seasons)]
    player = player.rename(columns={'id': 'player_id'})
    filtered_df = pd.merge(filtered_df, player[['player_id','full_name']], on = 'player_id', how = 'left')
    array.append(html.H4(title))
    for ind in range(5):
        array.append(html.P(
            str(filtered_df.iloc[ind]['season_id']-20000) + ' - ' + \
            filtered_df.iloc[ind]['full_name'] + ' - ' + \
            str(round(filtered_df.iloc[ind][condition]))
        ))
    return array
