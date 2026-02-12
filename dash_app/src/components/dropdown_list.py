from dash import dcc, html


def dropdown_list(
    list: list[str], 
    chart_id: str, 
    title: str, 
    value: str = None,
) -> html.Div:
    if value == None:
        return html.Div(
        children=[
            html.H6(title),
            dcc.Dropdown(
                id=chart_id,
                options = [{"label": data, "value": data} for data in list],
                multi=True,
            ),
        ]
    )
    return html.Div(
        children=[
            html.H6(title),
            dcc.Dropdown(
                id=chart_id,
                options = [{"label": data, "value": data} for data in list],
                multi=True,
                value=value
            ),
        ]
    )
