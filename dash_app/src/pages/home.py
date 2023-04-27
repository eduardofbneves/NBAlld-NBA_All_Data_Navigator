# package imports
from dash import html, dcc, callback, Input, Output, register_page

from utils.loader import load_dataframe

register_page(__name__, path='/')



layout = html.Div(
    [
        html.H1('Home page!'),
        html.Div(
            html.A('Go to Atalanta Hawks.', href='/teams/Atalanta')
        ),  
        html.A('/page2', href='/page2'),
        dcc.RadioItems(
            id='radios',
            options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
            value='Orange',
        ),
        html.Div(id='content')
    ]
)

@callback(Output('content', 'children'), Input('radios', 'value'))
def home_radios(value):
    return f'You have selected {value}'
