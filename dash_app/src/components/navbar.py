# notes


# package imports
import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, State, html, dcc, page_registry, page_container
from dash_bootstrap_components._components.Container import Container

'''
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
'''


navbar = dbc.Navbar(
            dbc.Container(
                [

                    dbc.Row([
                        dbc.Col([
                            dbc.Nav([
                                dbc.NavItem(dbc.NavLink("Home", href="/")),
                                #dbc.NavItem(dbc.NavLink("Fundamentals", href="/fundamentals")),
                                dbc.NavItem(dbc.NavLink("Seasons", href='/seasons')),
                                dbc.NavItem(dbc.NavLink("Players", href='/players')),
                                dbc.NavItem(dbc.NavLink("Teams", href='/teams')),
                                
                            ],
                            navbar=True
                            )
                        ],
                        width={"size":"auto"})
                    ],
                    align="center"),
                    dbc.Col(dbc.NavbarToggler(id="navbar-toggler", n_clicks=0)),
                ],
            fluid=True
            ),
    color="primary",
    dark=True
)


@dash.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
