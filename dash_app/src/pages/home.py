# package imports
from dash import html, dcc, callback, Input, Output, State, register_page
import dash_bootstrap_components as dbc


register_page(__name__, path='/')

layout = html.Div([
    html.H1('Statistics for teams and spectators'),
    html.H2('Navigate in the bar above'),
    html.P('Multi-page app about NBA from the 1980s until 2020')
    ], className='home-text')

