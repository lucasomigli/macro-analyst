import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

link_style = {
    'font-weight': 'bold',
    'font-size': '1.2em',
    'color': 'white',
    'font-color': 'white',
    'margin': '0em 0.5em 0em',
    'list-style-type': 'none',
    'text-decoration': 'none',
}

dropdown_style = {
    'font-size': '1em',
}

nav_links = dbc.Row(
    [
        dbc.Col(
            dcc.Link(
                'Indicators', href='/analyze/indicators', style=link_style)),
        dbc.Col(
            dcc.Link(
                'Securities', href='/analyze/securities', style=link_style)),
        dbc.Col(
            dcc.Link('Government',
                     href='/analyze/government-finance',
                     style=link_style)),
        dbc.Col(dcc.Link('BOP', href='/analyze/bop', style=link_style)),
        dbc.Col(dcc.Link('Trades', href='/analyze/trades', style=link_style)),
    ],
    className="ml-auto flex mt-3 mt-md-0",
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
        dbc.Collapse(nav_links, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
)