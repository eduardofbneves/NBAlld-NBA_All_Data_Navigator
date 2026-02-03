from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils.check_nan_players import check_nan_players

def season_stats(
        team, 
        team_stats, 
        player, 
        player_stats
    ) -> html.Div:
    team_list = team[team['id'].isin(
        team_stats.sort_values(by=['pts'], ascending=False)['team_id'].tolist()[:5])]
    sorted_teams = team_stats.sort_values(by=['pts'], ascending=False)
    bar_fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                    shared_yaxes=False, vertical_spacing=0.001)
    bar_fig.append_trace(go.Bar(y=team_list['full_name'], 
                           x=sorted_teams['fgm'].tolist()[:5], 
                           name='field goals made',
                           orientation='h'), 1, 1)
    bar_fig.append_trace(go.Bar(y=team_list['full_name'], 
                           x=sorted_teams['fg3m'].tolist()[:5], 
                           name='three pointers made',
                           orientation='h'), 1, 1)
    bar_fig.append_trace(go.Bar(y=team_list['full_name'], 
                           x=sorted_teams['ftm'].tolist()[:5], 
                           name='free throws made',
                           orientation='h'), 1, 1)
    
    bar_fig.append_trace(go.Scatter(
        y=team_list['full_name'], 
        x=sorted_teams['fg_pct'].tolist()[:5],
        mode='lines+markers',
        line_color='rgb(128, 0, 128)',
        name='Buckets made per season',
    ), 1, 2)
    
    bar_fig.update_layout(
    title='Buckets made per season and accuracy',
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
    ),
    yaxis2=dict(
        showgrid=False,
        showline=True,
        showticklabels=False,
        linecolor='rgba(102, 102, 102, 0.8)',
        linewidth=2,
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
    ),
    xaxis2=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        side='top',
    ),
    legend=dict(
    yanchor="middle",
    xanchor="center",
    ),
    margin=dict(l=100, r=20, t=70, b=70),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    )

    bar_fig.update_layout(barmode='group')
    '''
    sub_fig = make_subplots(rows=1, cols=3,
                            specs=[[{"type": "bar"}, {"type": "bar"},{"type": "bar"}]],
                            subplot_titles=("Blocks", "Steals", "Defensive Rebounds"))
    team_list = team[team['id'].isin(
        team_stats.sort_values(by=['stl'], ascending=False)['team_id'].tolist()[:5])]['full_name'].tolist()
    sub_fig.add_trace(go.Bar(values=team_stats.sort_values(by=['blk'], ascending=False)['dreb'].iloc[:5], labels=team_list, hole=.2),
                    row=1, col=1)
    team_list = team[team['id'].isin(
        team_stats.sort_values(by=['blk'], ascending=False)['team_id'].tolist()[:5])]['full_name'].tolist()                 
    sub_fig.add_trace(go.Bar(
                            values=team_stats.sort_values(by=['stl'], ascending=False)['dreb'].iloc[:5], 
                            labels=team_list, hole=.2),
                    row=1, col=2)
    team_list = team[team['id'].isin(
        team_stats.sort_values(by=['dreb'], ascending=False)['team_id'].tolist()[:5])]['full_name'].tolist()
    sub_fig.add_trace(go.Bar(
                            values=team_stats.sort_values(by=['dreb'], ascending=False)['dreb'].iloc[:5], 
                            labels=team_list, hole=.2),
                    row=1, col=3)
    
    sub_fig.update_layout(height=400, width=1000, title_text="Defensive profile")
    sub_fig.update_traces(textposition='inside', textinfo='value+label')
    '''
    return html.Div([
        html.Div([
            dbc.Row([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Col([
                                dcc.Graph(figure=bar_fig)
                            ])
                            
                        ], className='text-center')
                    ]),
        ], className='p-2 align-items-stretch'),
            '''dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.P('Field goals per seasons selected'),
                            dcc.Graph()
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
            # content'''
        
        ])
        
    ])