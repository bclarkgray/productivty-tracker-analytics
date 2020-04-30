import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px

# reads csv into 2 dataframes one for mouseclicks and the other for keypresses filtering out null rows
# returns a list of figures
def process_data(dataFile):
    df = pd.read_csv(dataFile)
    
    mClickFilter = df['ACTION'] == 'mouse_click'
    kPressFilter = df['ACTION'] == 'key_press'
    
    mClickDf = df.where(mClickFilter)
    mClickDf.dropna(inplace=True)
    
    kPressDf = df.where(kPressFilter)
    kPressDf.dropna(inplace=True)

    figures = []
    figures.append(px.pie(mClickDf, names='APPLICATION', title='Activity measured by mouse clicks'))
    figures.append(px.pie(kPressDf, names='APPLICATION', title='Activity measured by keyboard presses'))
    for fig in figures:
        fig.update_traces(textposition='inside')
        fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

    return figures

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def serve_layout():
    figures = []
    figures = process_data(dataFile)
    
    return html.Div(children = [
        html.H1('Application Activity',
        style = {
            'textAlign': 'center',
            #'color': colors['text']
        }),

        #html.Button('Refresh Data', id='refresh-data'),

        dcc.Graph(id='mClick-pie-chart', figure=figures[0]),

        dcc.Graph(id='kPress-pie-chart', figure=figures[1])
    ])

# layout and CSS stuff from https://dash.plotly.com/layout
def run_dashboard(figures):
    '''colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }
'''
    app.layout = html.Div(children=[
        html.H1('Application Activity',
        style = {
            'textAlign': 'center',
            #'color': colors['text']
        }),

        html.Button('Refresh Data', id='refresh-data'),

        dcc.Graph(id='mClick-pie-chart', figure=figures[0]),

        dcc.Graph(id='kPress-pie-chart', figure=figures[1])
    ])
'''
@app.callback(
    dash.dependencies.Output('refresh-data')


)
'''
if __name__ == '__main__':
    dataFile = 'activity_data.csv'
    app.layout = serve_layout
    #figures = []
    #figures = process_data(dataFile)
    #run_dashboard(figures)

    app.run_server(debug=True)