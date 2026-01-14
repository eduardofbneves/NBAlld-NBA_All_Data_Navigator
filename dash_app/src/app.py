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
    '''
    app.layout = html.Div([
        html.H1('Multi-page app with Dash Pages'),

        html.Div(
            [
                html.Div(
                    dcc.Link(
                        f"{page['name']} - {page['path']}", href=page["relative_path"]
                    )
                )
                for page in page_registry.values()
            ]
        ),
        page_container
    ])
    '''

    app.layout = html.Div([
        html.Div(
            html.H1(
                'NBA Stats Visualization',
                id='main-title'
            ),
            id='main-title-div'
        ),
        html.Div(
            [
            navbar,
            page_container,
            ]
        ),
    ])
    app.run()


if __name__ == "__main__":
    main()
