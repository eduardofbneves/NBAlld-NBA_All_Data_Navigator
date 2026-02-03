# package imports
from dash import html, dcc, callback, Input, Output, State, register_page
import dash_bootstrap_components as dbc


register_page(__name__, path='/')

layout = html.Div(
    [
        html.Div(),
        html.P('Statistics for teams and spectators'),
        html.H1('Navigate in the bar above')
    ], 
    className='home-text'
)
