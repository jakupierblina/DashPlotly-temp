import dash_html_components as html
import dash_core_components as dcc
import pandas as pd


data = {'Pos 1': ['Pos 1'], 'Pos 2': ['Pos 2'], 'Pos X': ['Pos X'], 'Pos Y': ['Pos Y'], 'Pos ..': ['Pos ..'], 'Pos NEW': ['Pos NEW'] }
df = pd.DataFrame(data)

def generate_table(dataframe, max_rows=26):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns], style={'textAlign': 'center', 'padding': 10, 'border': 'solid 2px black',}) ] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col],style={'textAlign': 'center', 'padding': 10, 'border': 'solid 2px black',}) for col in dataframe.columns
        ],style={'textAlign': 'center', 'padding': 10, 'border': 'solid 2px black',}) for i in range(min(len(dataframe), max_rows)) ], style={'textAlign': 'center', 'padding': 10, 'border': 'solid 2px black',},
    )

layout = html.Div([
    html.Div([
        html.Div([
            generate_table(df)
        ], className='row', style={'position': 'center', 'margin-bottom': '2%',}),

        html.Div([
            html.Div([html.H3('Pos 1 - Description'), ], style={'textAlign': 'center', 'margin': '20px 0', 'background-color':'lightpink', 'padding': 15,}, className='col'),
        ], className='row'),

        html.Div([

            # col 1
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='demo-dropdown',
                            options=[
                                {'label': 'item1', 'value': 'item1'},
                                {'label': 'item2', 'value': 'item2'},
                                {'label': 'item3', 'value': 'item3'}
                            ], style={'font-size': 15, 'width': 100, 'height':30, },
                            value='item1'
                        ),
                        html.Div(id='dd-output-container')

                ], className='row'),
                ],style={'margin': 'auto', }),



                html.Div([html.Div([html.Button('Submit',style={'margin-top': '3%', 'background-color': '#091c2f','color':'white', 'width': 110, 'height': 60, ' border': 'none','text-decoration':'none','display':'inline-block' ,'padding': '15px 32px','text-align': 'center',}, id='submit-val', n_clicks=0), ], className='row'),]),

            ], className='col'),

            # col 2
            html.Div([
                html.Div([
                    html.Div([html.P('Graph here'), ], className='row'),
                    ]),
            ], className='col',),

        ], className='row',)
    ])

])

