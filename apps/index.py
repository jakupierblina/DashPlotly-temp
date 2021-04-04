import dash_html_components as html
import pandas as pd

# table
data = {'Tab 1' : ['A', 'B', 'C', ], 'Tab 2' : ['a', 'b', 'c', ]}
df = pd.DataFrame(data)


def generate_table(dataframe, max_rows=26):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns]) ] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([html.P("Table here")], className='col'),
            html.Div([
                html.Div([
                    html.Div([html.P("Data")], className='row'),
                    html.Div([html.P("Data")], className='row'),
                    html.Div([html.P("Graph")], className='row'),
                    html.Div([html.P("Data")], className='row'),
                    html.Div([html.P("Data")], className='row'),
                ], style={'margin': 10, 'font-size': 20,}, className='col')
            ], className='col'),
        ], className='row')
    ])


])


