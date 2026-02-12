from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

from components.list_top_players_teams import list_top_players_teams


def team_stats_view(
        team, 
        team_stats, 
        player, 
        player_season_stats
    ) -> html.Div:
    players = player[player['team_id']==team.iloc[0,0]]
    player_stats = player_season_stats[player_season_stats['player_id'].isin(players['id'].tolist())]

    bubble_fig = go.Figure(data=[go.Scatter(
        x=team_stats['fg_pct'].tolist(),
        y=team_stats['fg3_pct'].tolist(),
        mode='markers',
        marker=dict(
            color=np.subtract(team_stats['season_id'].tolist(),20000),
            size=np.divide(team_stats['pts'].tolist(),2.5),
            showscale=True
        ),
        #hoverinfo=np.subtract(team_stats['season_id'].tolist(),20000),
        hovertext=np.subtract(team_stats['season_id'].tolist(),20000),
    )])

    '''bubble_fig.update_traces(
        customdata=['Season'],
        hovertemplate="<br>".join([
            "Year: %{custom_data[0]}",
        ])
    )'''
    
    bubble_fig.update_layout(
        title="Field goal percentage distribution and points by year",
        xaxis_title="2 pointers (fg)",
        yaxis_title="3 pointers (fg)",
        legend_title="season",
    )
    sun_data = dict(
        character=["Actions", "Ofensive", "Defensive", "Field Goals", "Triples", "Free Throws", "Defensive Rebs", "Steals", "Turnovers"],
        parent=["", "Actions", "Actions", "Ofensive", "Ofensive", "Ofensive", "Defensive", "Defensive", "Defensive" ],
        value=[0,0,0] + team_stats[["fg_pct", "fg3_pct", "ft_pct", "dreb", "stl", "tov"]].sum(axis=0).tolist()
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
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Div(list_top_players_teams(
                            player_stats, 
                            player,
                            'nmr_games',
                            'Most appearences for the team'
                        ))
                    ])
                ], className='url-support-page-div')
            ], xs=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(figure=bubble_fig)
                    ])
                ], className='url-support-page-div')
            ], xs=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(figure=sun_fig)
                    ])
                ], className='h-100 text-center')
            ], xs=4)
        ], className='url-support-page-div'),
    ])