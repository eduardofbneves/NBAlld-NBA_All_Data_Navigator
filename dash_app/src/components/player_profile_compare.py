from dash import html
import dash_bootstrap_components as dbc

from utils.check_nan_players import check_nan_players

def player_profile_compare(player) -> html.Div:
    return html.Div([
        dbc.Col([
            dbc.Row([
                html.H1(player['full_name']),
                html.H4('#' + check_nan_players(player.iloc[0,9]) 
                            + ' ' + check_nan_players(player.iloc[0,10]))
            ], className='header-title'),
        ], className='header-compare'),
    ])