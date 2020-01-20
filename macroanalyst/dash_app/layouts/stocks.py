import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from fredapi import Fred

# ==============================
#  Securities Charting Template
# ==============================

# def get_data():
#     import plotly.graph_objects as go
#     import pandas as pd

#     sp = pd.read_csv(r'C:\dev\macro-analyst\data\sp500.csv')
#     sp.drop(['Settle', 'Change', 'Volume', 'Previous Day Open Interest'], axis=1, inplace=True)

#     fig = go.Figure()

#     fig.add_trace(go.Scatter(x=sp.Date, y=sp.Open, name="S&P Open",
#                     line_color='darkslategrey'))

#     # fig.add_trace(go.Scatter(x=sp500.Date, y=sp500.Last, name="S&P Close",
#     #                  line_color='red'))

#     fig.update_layout(title_text='S&P 500 Time Series',
#                     xaxis_rangeslider_visible=True)

#     return fig.show()

def get_data(series_name):
    import pandas as pd
    import plotly.express as px
    fred = Fred(api_key='822de9da06f6edc31bc1422870dfad80')
    series = fred.get_series(series_name)

    data = pd.DataFrame({'date':series.index, 'price':series.values})
    fig = px.line(data, x="date", y="price", title="Closing price of S&P 500")
    display = fig.show(config={'scrollZoom': True})

    return display

result = get_data('SP500')

securities = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Filters"),
                        dbc.Form([
                            dbc.FormGroup(
                                [
                                    dbc.Label("Stock", html_for="country"),
                                    dcc.Dropdown(
                                        id="country",
                                        options=[
                                            {"label": "Option 1", "value": 1},
                                            {"label": "Option 2", "value": 2},
                                        ],
                                    ),
                                ],
                                className="mt-4"
                            )
                        ])       
                    ],
                    lg=4,
                ),
                html.Hr(className="my-2"),
                dbc.Col(
                    [   
                        # Rock this chart
                        result
                    ]
                ),
            ]
        )
    ],
    className="mt-4"
)