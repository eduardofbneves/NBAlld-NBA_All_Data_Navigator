from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils.check_nan_players import check_nan_players

def season_stats(team, team_stats, player, player_stats) -> html.Div:
    team_list = team[team['id'].isin(
        team_stats.sort_values(by=['pts'], ascending=False)['team_id'].tolist()[:5])]
    sorted_teams = team_stats.sort_values(by=['pts'], ascending=False)
    bar_fig = go.Figure()
    bar_fig.add_trace(go.Bar(x=team_list['full_name'], 
                           y=sorted_teams['fgm'].tolist()[:5], 
                           name='field goals made'))
    bar_fig.add_trace(go.Bar(x=team_list['full_name'], 
                           y=sorted_teams['fg3m'].tolist()[:5], 
                           name='three pointers made'))
    bar_fig.add_trace(go.Bar(x=team_list['full_name'], 
                           y=sorted_teams['ftm'].tolist()[:5], 
                           name='free thorws made'))
    
    '''
       line_fig = go.Scatter(
        x=team_list['full_name'], y=sorted_teams['fg_pct'].tolist()[:5],
        mode='lines+markers',
        line_color='rgb(128, 0, 128)',
        name='Percentage of each bucker',
    )
    bar_fig.add_trace(go.Bar(x=team_list, 
                         y=np.subtract(team_stats['fgm'].tolist()[:6],team_stats['fgm'].tolist()[:6]), 
                         name='field goals attempted'))
    '''
    bar_fig.update_layout(barmode='group')

    sub_fig = make_subplots(rows=1, cols=3,
                            specs=[[{"type": "pie"}, {"type": "pie"},{"type": "pie"}]],
                            subplot_titles=("Blocks", "Steals", "Defensive Rebounds"))
    team_list = team[team['id'].isin(
        team_stats.sort_values(by=['stl'], ascending=False)['team_id'].tolist()[:6])]['full_name'].tolist()
    sub_fig.add_trace(go.Pie(values=team_stats.sort_values(by=['blk'], ascending=False)['dreb'].iloc[:6], 
                            labels=team_list, hole=.2),
                    row=1, col=1)
    team_list = team[team['id'].isin(
        team_stats.sort_values(by=['blk'], ascending=False)['team_id'].tolist()[:6])]['full_name'].tolist()                 
    sub_fig.add_trace(go.Pie(
                            values=team_stats.sort_values(by=['stl'], ascending=False)['dreb'].iloc[:6], 
                            labels=team_list, hole=.2),
                    row=1, col=2)
    team_list = team[team['id'].isin(
        team_stats.sort_values(by=['dreb'], ascending=False)['team_id'].tolist()[:6])]['full_name'].tolist()
    sub_fig.add_trace(go.Pie(
                            values=team_stats.sort_values(by=['dreb'], ascending=False)['dreb'].iloc[:6], 
                            labels=team_list, hole=.2),
                    row=1, col=3)
    
    sub_fig.update_layout(height=400, width=1000, title_text="Defensive profile")
    sub_fig.update_traces(textposition='inside', textinfo='value+label')
    
    return html.Div(
        [

    html.Div([
        dbc.Row([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Col([
                            html.P('Buckets made by top 5 pointers each window'),
                            dcc.Graph(figure=bar_fig)
                        ])
                        
                    ], className='text-center')
                ]),
    ], className='p-2 align-items-stretch'),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.P('Field goals per seasons selected'),
                        dcc.Graph(figure=bar_fig)
                    ], className='text-center')
                ]),
            ], xs=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(figure=sub_fig)
                    ])
                ], className='h-100 text-center')
            ], xs=8),
        ], className='p-2 align-items-stretch'),
        # content
    
])
    
    ]
)

'''
dict(
                                        r=player_stats[['pts_home','ast_home', 'miss', 'blk_home', 'reb_home']].sum(axis=0).tolist(),
                                        theta=['pts_home','ast_home', 'miss', 'blk_home', 'reb_home']
                                    ),
                                    '''