import dash_html_components as html
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
        ], className='row'),

        html.Div([
            html.Div([html.H3('Pos 1 - Description'), ], style={'textAlign': 'center', 'margin': '20px 0', 'background-color':'#FFFFF0', 'padding': 15,}, className='col'),
        ], className='row'),

        html.Div([

            # col 1
            html.Div([
                html.Div([html.Div([html.P('Data here'), ], className='row'),]),
                html.Div([html.Div([html.P('Data here'), ], className='row'),]),
                html.Div([html.Div([html.P('Data here'), ], className='row'),]),
                html.Div([html.Div([html.P('Data here'), ], className='row'),]),
                html.Div([html.Div([html.Button('Submit', id='submit-val', n_clicks=0, style={'margin-top': '3%', 'background-color': '#091c2f','color':'white', 'width': 110, 'height': 60, ' border': 'none','text-decoration':'none','display':'inline-block' ,'padding': '15px 32px','text-align': 'center',},), ], className='row'),]),

            ], className='col'),

            # col 2
            html.Div([
                html.Div([html.Div([html.P('Graph here'), ], className='row'),]),
                html.Div([
                    html.Div([html.P('Data here'), ], className='col'),
                    html.Div([html.P('Data here'), ], className='col'),

                ], className='row'),
                # can add here a row

            ], className='col'),

        ], className='row')
    ])

])

