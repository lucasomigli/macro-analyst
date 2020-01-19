# =============================
#  Dash app
# =============================

from dash import Dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from .base_layout import html_layout


def Add_Dash(server):
    """
    Creates a Dash app (using Flask at its core)
    ========================================================
    A function is used instead of global var in order to pass
    the top-level Flask app into Dash as 'server'.

    routes_pathname_prefix establishes a domain hierarchy.
    Everything below '/dashboard/' is served by Dash.
    Everything above it is served up with Flask.
    """
    external_stylesheets = [dbc.themes.BOOTSTRAP,
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/js/main.js']

    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    external_scripts=external_scripts,
                    # Establish domain hierarchy
                    routes_pathname_prefix='/dashboard/')

    # =============================
    #  Variable Declarations
    # =============================
    
    # Override the underlying HTML template
    dash_app.index_string = html_layout
    
    PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

    search_bar = dbc.Row(
        [
            dbc.Col(dbc.Input(type="search", placeholder="Search")),
            dbc.Col(
                dbc.Button("Search", color="secondary", className="ml-2"),
                width="auto",
            ),
        ],
        no_gutters=True,
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )

    navbar = dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("MacroAnalyst", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
        ],
        color="dark",
        dark=True,
    )

    body = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2("Heading"),
                            html.P(
                                """\
                                Donec id elit non mi porta gravida at eget metus.
                                Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
                                nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
                                malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non
                                mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
                                commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
                                amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed
                                odio dui."""
                            ),
                            dbc.Button("View details", color="secondary"),
                        ],
                        md=4,
                    ),
                    dbc.Col(
                        [
                            html.H2("Graph"),
                            dcc.Graph(
                                figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                            ),
                        ]
                    ),
                ]
            )
        ],
        className="mt-4",
    )
    dash_app.layout = html.Div([navbar, body])

    # Initialize callbacks after the application is loaded
    init_callbacks(dash_app)

    # Launch Application
    return dash_app.server


def init_callbacks(dash_app):

    @dash_app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        """Preserves navbar collapse state"""
        if n:
            return not is_open
        return is_open

#    def get_datasets():
#     """Return previews of all CSVs saved in /data directory."""
#     p = Path('.')
#     data_filepath = list(p.glob('data/*.csv'))
#     arr = ['This is an example Plot.ly Dash App.']
#     for index, csv in enumerate(data_filepath):
#         df = pd.read_csv(data_filepath[index]).head(10)
#         table_preview = dash_table.DataTable(
#             id='table_' + str(index),
#             columns=[{"name": i, "id": i} for i in df.columns],
#             data=df.to_dict("rows"),
#             sort_action="native",
#             sort_mode='single'
#         )
#         arr.append(table_preview)
#     return arr



# # =============================
# # Dash app
# # =============================
# app.app_context().push()

# select = dbc.Row([
#     dbc.Col(
#         dbc.Nav([
#             dcc.Dropdown(
#                 id='dropdown-countries',
#                 options=[{'label': item, 'value': item}
#                          for item in [x.country for x in Country.query.all()]],
#                 value='Australia',
#                 style={"width": 500}
#             ),
#             dcc.Dropdown(
#                 id='dropdown-indicators',
#                 value='Indicators',
#                 style={"width": 500}
#             ),
#             dcc.Dropdown(
#                 id='dropdown-charts',
#                 options=[{'label': i, 'value': i}
#                          for i in ("Candlesticks", "Line Chart", "Area Chart")],
#                 value='Line Chart',
#                 style={"width": 500}
#             ),
#         ], id="navbar-charts"
#         ), width={"size": 12, "offset": 2})
# ])

# body = html.Div(
#     dbc.Row([
#             dbc.Col(
#                 children=[charts.main_chart],
#                 id="main-chart-container",
#             ), dbc.Col(
#                 children=[charts.side_chart],
#                 id="side-chart-container",
#                 className="canvas",
#             )
#             ],
#             id="charts-container",
#             className="container"
#             ),
#     style={'marginBottom': 50, 'marginTop': 25}
# )

# dash_app = dash.Dash(
#     __name__,
#     server=app,
#     routes_pathname_prefix='/dash/',
#     meta_tags=[{"name": "viewport", "content": "width=device-width"}]
# )

# dash_app.layout = html.Div([
#     select,
#     body
# ])

# charts.initialise_charts()


# @dash_app.callback(
#     dash.dependencies.Output('dropdown-indicators', 'options'),
#     [dash.dependencies.Input('dropdown-countries', 'value')]
# )
# def update_indicator_dropdown(country_name):
#     return [{'label': item.code, 'value': item.code} for item in Indicator.query.filter_by(country_id=Country.query.filter_by(country=country_name).first().id).all()]


# @dash_app.callback(
#     [Output('main_chart', 'figure'),
#      Output('side_chart', 'figure')],
#     [Input('dropdown-charts', 'value'),
#      Input('dropdown-countries', 'value'),
#      Input('dropdown-indicators', 'value')
#      ])
# def update_figure(chart_type, country_name, code_name):

#     country = Country.query.filter_by(country=country_name).first()
#     indicator = Indicator.query.filter_by(code=code_name)

#     chart = indicator.filter_by(country_id=country.id).first()
#     dataframe = pd.DataFrame()

#     # Load API Keys
#     with open('macroanalyst/keys.json', 'r+') as f:
#         api_keys = json.load(f)

#     if 'stlouis' in chart.source:
#         key = api_keys['fred']

#         series_id = re.search('series_id=(.*)&ap', chart.source).group(1)
#         fred = Fred(api_key=key)

#         dataframe = pd.DataFrame(fred.get_series(series_id))

#     else:
#         key = api_keys['quandl']
#         link = str(chart.source).replace('API_KEY', key)
#         r = requests.get(link)

#         dataframe = pd.read_csv(io.StringIO(r.content.decode('utf-8')))

#     if len(dataframe.columns) > 1:
#         print(dataframe)
#         charts.df = dataframe
#         charts.set_stats(chart.indicator, charts.df.columns[1])

#     if chart_type == "Candlesticks" and ("Low" or "High" or "Open" or "Last") in charts.df:

#         charts.main_trace['type'] = "candlestick"
#         charts.main_trace['fill'] = "none"

#         ohlc = {
#             "low": charts.df['Low'],
#             "high": charts.df['High'],
#             "open": charts.df['Open'],
#             "close": charts.df['Last'],
#         }

#         for val in ohlc:
#             charts.main_trace[val] = ohlc[val]

#     elif chart_type == "Area Chart":

#         charts.main_trace['type'] = "lines"
#         charts.main_trace['fill'] = "tozeroy"

#     else:

#         charts.main_trace['type'] = "lines"
#         charts.main_trace['fill'] = "none"

#     return [{
#         'data': charts.traces,
#         'layout': charts.main_layout
#     }, {
#         'data': charts.side_traces,
#         'layout': charts.main_layout
#     }]
