import os
from utils.loader import load_dataframe
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from utils.global_vars import ALL_SEASONS

def main() -> None:
    player_season_stats = load_dataframe('player_season_stats')
    player = load_dataframe('player')
    team_season_stats = load_dataframe('team_season_stats')
    season_ind = load_dataframe('season_ind')
    
    drena = dict(zip(list(range(season_ind.iloc[0, 0]-20000,
                                                  season_ind.iloc[-1, 0]-20000)), 
                                       season_ind['season_str'].tolist()))
    print(drena)
    '''
    player_stats = player_season_stats[player_season_stats.isin(season_range)]
    player_stats = player_stats.groupby(['player_id']).mean()
    print(player[player['last_name']=='Bryant'])
    print(player_season_stats[player_season_stats['player_id']==977])
    '''
    


if __name__ == "__main__":
    main()