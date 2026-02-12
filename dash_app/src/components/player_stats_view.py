from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

from utils.check_nan_players import check_nan_players
from utils.global_vars import PLAYER_STATS_INDEXES

def player_stats_view(player, player_stats) -> html.Div:
    years = np.subtract(player_stats['season_id'].tolist(),20000)
    line_fig = go.Figure()
    line_fig.add_trace(go.Scatter(x=years,
                                  y=player_stats['nmr_games'].tolist(),
                                  mode='lines+markers'))
    line_fig.update_layout(
        xaxis=dict(
            title=dict(
                text="Seasons played"
            )
        ),
        yaxis=dict(
            title=dict(
                text="Number of games played",
            ),
            range=[0, 90],
            autorange=False,
            fixedrange=False  
        ),
    )
    
    stats = player_stats[['pts_home','ast_home', 'miss', 'blk_home', 'reb_home']].mean(axis=0).tolist()
    stats_index = []
    for i in range(len(stats)):
        stats_index.append(stats[i]/PLAYER_STATS_INDEXES[i])
    
    radial_fig = go.Figure()
    radial_fig.add_trace(go.Scatterpolar(
        r = stats_index,
        theta=['pts_home','ast_home', 'miss', 'blk_home', 'reb_home'],                   
        fill='toself')
    )
    radial_fig.update_layout(
        polar=dict(
            angularaxis=dict(
                tickmode='array',
                tickvals=['pts_home','ast_home','miss','blk_home','reb_home'],
                ticktext=['Points', 'Assists', 'Misses', 'Blocks', 'Rebounds'],
                ticks='outside'
            ),
            radialaxis=dict(
                range=[0, 6],   # fixed radial scale
                tick0=0,
                dtick=1,
                showticklabels=True
            )
        ),
        showlegend=False
    )



    sun_data = dict(
        character=["Buckets", "fg2", "fg3", "ft", "fg2 - home", "fg2 - away", "fg3 - home", "fg3 - away", "ft - home", "ft - away"],
        parent=["", "Buckets", "Buckets", "Buckets", "fg2", "fg2", "fg3", "fg3", "ft", "ft" ],
        value=[0,0,0,0] + player_stats[["fg2_pts_home", "fg2_pts_away", "fg3_pts_home", "fg3_pts_away", "ft_home", "ft_away"]].sum(axis=0).tolist()
    )
    sun_fig = px.sunburst(
        sun_data,
        names='character',
        parents='parent',
        values='value',
    )
    sun_fig.update_layout(
        showlegend=True
    )

    return html.Div([
        html.Div([
            dcc.Link(
                html.Button(
                    "Compare",
                    className='compare-player-button'), 
                href="/compare_players/"+str(player[0]), 
                refresh=True)
            ], 
            className='compare-player-button-div',
        ),
        

        html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H3('Games per seasons'),
                        dcc.Graph(figure = line_fig)
                    ], className='text-center')
                ]),
            ], xs=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H3('Player radial profile'),
                        dcc.Graph(
                            figure=radial_fig
                        )
                    ], className='text-center')
                ])
            ], xs=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H3('Buckets made home/away'),
                        dcc.Graph(figure = sun_fig),
                    ])
                ], className='text-center')
            ], xs=4)
        ]),
    ])

        ]
    )
    
