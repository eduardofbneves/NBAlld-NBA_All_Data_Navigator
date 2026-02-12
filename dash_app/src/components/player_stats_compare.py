from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np

from utils.global_vars import PLAYER_STATS_INDEXES

def player_stats_compare(player_stats) -> html.Div:
    years = np.subtract(player_stats['season_id'].tolist(),20000)
    line_fig = go.Figure()
    line_fig.add_trace(go.Scatter(x=years,
                                  y=player_stats['nmr_games'].tolist(),
                                  mode='lines+markers'))
    line_fig.update_layout(
        height=240,
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
        height=240,
        polar=dict(
            angularaxis=dict(
                tickmode='array',
                tickvals=['pts_home','ast_home','miss','blk_home','reb_home'],
                ticktext=['Points', 'Assists', 'Misses', 'Blocks', 'Rebounds'],
                ticks='outside'
            ),
            radialaxis=dict(
                range=[0, 6],
                tick0=0,
                dtick=1,
                showticklabels=True
            )
        ),
        showlegend=False
    )

    return html.Div([
        dbc.Row([
            dbc.Card([
                dbc.CardBody([
                    html.H3('Games per seasons'),
                    dcc.Graph(figure = line_fig)
                ], className='text-center')
            ]),
        ]),
        dbc.Row([
            dbc.Card([
                dbc.CardBody([
                    html.H3('Player radial profile'),
                    dcc.Graph(figure=radial_fig)
                ], className='text-center')
            ])
        ]),
    ])
    