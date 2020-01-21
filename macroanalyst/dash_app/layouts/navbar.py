import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

search_bar = dbc.Row(
        [
            dbc.Col(dcc.Link('Econ', href='/analyze/indicators')),
            dbc.Col(dcc.Link('Stocks', href='/analyze/securities')),
            dbc.Col(dcc.Link('Help', href='/help')),
            # dbc.Col(dbc.Input(type="search", placeholder="Search")),
            # dbc.Col(
            #     dbc.Button("Search", color="secondary"),
            # ),
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