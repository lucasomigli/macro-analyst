import dash
import charts
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import codecs

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])

nav = dbc.Nav([
    dbc.NavItem((dbc.NavLink("Macro-Analyst", active=True, href="#"))),
    dbc.NavItem(dbc.NavLink("Home", active=True, href="#")),
    dbc.NavItem(dbc.NavLink("About", href="#")),
    dbc.NavItem(dbc.NavLink("Features", href="#")),
    dbc.NavItem(dbc.NavLink("Contact", href="#")),
    dbc.DropdownMenu(
        [dbc.DropdownMenuItem("United States"),
         dbc.DropdownMenuItem("United Kindom"),
         dbc.DropdownMenuItem("Canada"),
         dbc.DropdownMenuItem("Europe"),
         ],
        label="Country",
        nav=True,
    ),
    dbc.DropdownMenu(
        [dbc.DropdownMenuItem("GDP"),
         dbc.DropdownMenuItem("Stock Market"),
         dbc.DropdownMenuItem("Balance Of Payments"),
         dbc.DropdownMenuItem("Trades"),
         dbc.DropdownMenuItem("Commodities"),
         dbc.DropdownMenuItem("COT Report"),
         dbc.DropdownMenuItem("PMI & NMI"),
         dbc.DropdownMenuItem("Building Permits"),
         ],
        label="Indicator",
        nav=True,
    )
]
)

section1 = html.Div(
    [
        dbc.Row([
            dbc.Col([
                charts.main_chart,
                html.Table([
                    html.Thead(html.Tr(html.Th("Main Statistics"))),
                    html.Tbody(
                        [html.Tr([
                            html.Td(x),
                            html.Td(round(charts.main_chart_stats[x], 5))
                        ]) for x in charts.main_chart_stats]
                    )
                ])
            ]),
            dbc.Col([
                charts.side_chart,
                html.Table([
                    html.Thead(html.Tr(html.Th("% Change Statistics"))),
                    html.Tbody(
                        [html.Tr([
                            html.Td(x),
                            html.Td(round(charts.side_chart_stats[x], 5))
                        ]) for x in charts.side_chart_stats]
                    )
                ])
            ]),
        ])
    ])

footer = html.Div([
    html.P(children="Footer here.")
])

app.layout = html.Div([
    nav,
    section1,
    footer
])


if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
