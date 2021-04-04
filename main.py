"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server

from apps import analysis, new, positions, index

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 100,
    "bottom": 0,
    "width": "16rem",
    "padding": 15,
    "font-size": 20,
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
    html.Div([
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/index", active="exact"),
                dbc.NavLink("Positions", href="/positions", active="exact"),
                dbc.NavLink("Analysis", href="/analysis", active="exact"),
                dbc.NavLink("New", href="/new", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),], className='row'),
        html.Div([
            html.Div([html.P("Data")], className='row'),
            html.Div([html.P("Data")], className='row'),
             ], style={'margin': 5, 'font-size': 20}, className='col')
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div(
    [
        # first row with title
        dbc.Row(dbc.Col(
            html.H1('Hello webapp', style={'color': '#191970', 'fontSize': 50, 'padding': 20, 'textAlign': 'center', 'background-color':'#F0F8FF',}), )),

        # second row - main content
        dbc.Row(
            # col 1 - side bar menu
            dbc.Col(
            html.Div(
                [dcc.Location(id="url"), sidebar, content], className='col') ,),

            # col 2 - main content
        ),

    ])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/index" or pathname =='/':
        return index.layout
    elif pathname == "/positions":
        return positions.layout
    elif pathname == "/analysis":
        return analysis.layout
    elif pathname == "/new":
        return new.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)