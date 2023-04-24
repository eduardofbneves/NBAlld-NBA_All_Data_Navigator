from dash import Dash, html, dcc, page_registry, page_container


def main() -> None:
    app = Dash(__name__, use_pages=True)
    app.title = "Test"
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
    app.run()


if __name__ == "__main__":
    main()
