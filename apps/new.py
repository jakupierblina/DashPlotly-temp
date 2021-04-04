import dash_html_components as html
import dash_core_components as dcc



layout = html.Div([
    html.Div([
        html.Div([
            # col 1
            html.Div([
                html.P('item1'),
                html.P('item2'),
                html.P('item3'),
            ], className='col'),

            # col 2
            html.Div([
                html.Div([html.P('Table here'), ], className='row'),
                html.Div([html.Button('Submit', id='submit-val', n_clicks=0, style={'margin-top': '3%', 'background-color': '#091c2f','color':'white', 'width': 110, 'height': 60, ' border': 'none','text-decoration':'none','display':'inline-block' ,'padding': '15px 32px','text-align': 'center',},) ], className='row'),

            ], className='col'),

            # col 3
            html.Div([
                html.Div([html.P('Graph here'), ], className='row'),
                html.Div([html.P('Graph here'), ], className='row'),

            ], className='col'),

        ], className='row'),


]),
])

