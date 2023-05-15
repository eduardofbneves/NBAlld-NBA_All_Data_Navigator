from .loader import load_dataframe

PLAYER_STATS_INDEXES = load_dataframe('player_season_stats')[[
    'pts_home','ast_home', 'miss', 'blk_home', 'reb_home'
    ]].mean(axis=0).tolist()

ALL_SEASONS = load_dataframe('season_ind')['season_id'].unique()

