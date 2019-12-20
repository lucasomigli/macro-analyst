import dash
import charts
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import codecs

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

select = dbc.Row([
    dbc.Col(
        dbc.Nav([
            dcc.Dropdown(
                id='dropdown-countries',
                options=[{'label': i, 'value': i}
                         for i in ("United States", "United Kindom", "Australia", "Europe")],
                value='Australia',
                style={"width": 150}
            ),
            dcc.Dropdown(
                id='dropdown-indicators',
                options=[{'label': i, 'value': i}
                         for i in ("GDP", "Stock Market", "Balance Of Payments",
                                   "Trades", "Commodities", "COT Report", "PMI & NMI", "Building Permits")],
                value='GDP',
                style={"width": 150}
            ),
            dcc.Dropdown(
                id='dropdown-charts',
                options=[{'label': i, 'value': i}
                         for i in ("Candlesticks", "Line Chart", "Area Chart")],
                value='Line Chart',
                style={"width": 150}
            ),
        ], id="navbar-charts"
        ), width={"size": 12, "offset": 2})
])


body = html.Div(
    dbc.Row([
            dbc.Col(
                children=[charts.main_chart],
                id="main-chart-container",
            ), dbc.Col(
                children=[charts.side_chart],
                id="side-chart-container",
                className="canvas",
            )
            ],
            id="charts-container",
            className="container"
            ),
    style={'marginBottom': 50, 'marginTop': 25}
)

app.layout = html.Div([
    select,
    body
])


@app.callback(
    Output('main_chart', 'figure'),
    [Input('dropdown-charts', 'value'),
     ])
def update_figure(chart_type):

    if chart_type == "Candlesticks":

        charts.main_trace['type'] = "candlestick"
        charts.main_trace['fill'] = "none"

    elif chart_type == "Area Chart":

        charts.main_trace['type'] = "lines"
        charts.main_trace['fill'] = "tozeroy"

    else:

        charts.main_trace['type'] = "lines"
        charts.main_trace['fill'] = "none"

    return {
        'data': charts.traces,
        'layout': charts.main_layout
    }


if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
