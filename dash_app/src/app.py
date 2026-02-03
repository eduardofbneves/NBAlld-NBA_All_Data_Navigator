from dash import Dash, html, page_container
import dash_bootstrap_components as dbc
from components.navbar import navbar

def main() -> None:
    app = Dash(
        __name__, 
        use_pages=True, 
        external_stylesheets=[dbc.themes.UNITED]
        )
    app.title = "NBAll'd"

    app.layout = html.Div([
        html.Div(
            html.H1(
                'NBA Stats Visualization',
                id='main-title'
            ),
            id='main-title-div'
        ),
        html.Div([
            html.Div(
                navbar,
                id='navbar-div'
            ),
            page_container,
            ],
            id='navbar-container-app'),
    ],
    id='navbar-title-card'
    )
    app.run()


if __name__ == "__main__":
    main()
