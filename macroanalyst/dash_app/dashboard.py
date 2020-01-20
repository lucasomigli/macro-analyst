# =============================
#  Dash app
# =============================

import os
import dash
from dash import Dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from .layouts.base import html_layout
from .layouts.navbar import navbar
from .layouts.indicator import indicators
from .layouts.stocks import securities

"""
Due to application architecture, page vars must currently be defined
outside of function scope of init_callbacks. Will restructure when I can.
"""

index_page = html.Div([
    dcc.Link('Chart economic indicators', href='/analyze/indicators'),
    html.Br(),
    dcc.Link('Chart securities', href='/analyze/securities'),
    html.Br(),
    html.P('or,'),
    html.Br(),
    dcc.Link('Go here for help', href='/analyze/help'),
])

indicators_page = html.Div([
    indicators,        
])

securities_page = html.Div([
    securities,
])

help_page = html.Div([
    html.H1('No time. Help yourself.'),
])


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
    external_stylesheets = [dbc.themes.LUX,
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/js/main.js']

    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    external_scripts=external_scripts,
                    # Establish domain hierarchy
                    routes_pathname_prefix='/analyze/')

    # Silence exception to elements not existing until callback execution
    dash_app.config.suppress_callback_exceptions = True

    # =============================
    #  Front-End SPA Instantiation
    # =============================
    
    # Override the underlying HTML template
    dash_app.index_string = html_layout

    # Initialize callbacks before the application has finished loading
    init_callbacks(dash_app)

    dash_app.layout = html.Div([
    
        # Represents the URL bar. Doesn't render anything
        dcc.Location(id='url', refresh=False),

        # The following elements render in every case
        navbar,

        # Content is rendered in this element
        html.Div(id='page-content')
    ])

    # Launch Application
    return dash_app.server


# =============================
#  Callbacks
# =============================

def init_callbacks(dash_app):
    """
    This module contains various callback and nested functions.
    """
    @dash_app.callback(dash.dependencies.Output('page-content', 'children'),
                        [dash.dependencies.Input('url', 'pathname')])
    
    def display_page(pathname):
        """
        Essentially serves as the Dash application's routing function

        Args: pathname passed from href link objects
        Returns: Page render that correlates to respective arg parameter
        """
        if pathname == '/analyze/indicators':
            return indicators_page
        elif pathname == '/analyze/securities':
            return securities_page
        elif pathname == '/analyze/help':
            return help_page
        else:
            return index_page

            # return html.Div([
            #     html.h1('404 - PAGE NOT FOUND')
            # ])

    @dash_app.callback(dash.dependencies.Output('page-1-content', 'children'),
                [dash.dependencies.Input('page-1-dropdown', 'value')])
    def page_1_dropdown(value):
        return 'You have selected "{}"'.format(value)

    
    @dash_app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
    def page_2_radios(value):
        return 'You have selected "{}"'.format(value) 


    # Pertains to navbar collapse on small viewports
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
