import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px

# reads csv into 2 dataframes one for mouseclicks and the other for keypresses
def handle_data():
    df = pd.read_csv('activity_data.csv')
    
    mClickFilter = df['ACTION'] == 'mouse_click'
    kPressFilter = df['ACTION'] == 'keypress'
    
    mClickDf = df.where(mClickFilter)
    mClickDf.dropna(inplace=True)
    
    kPressDf = df.where(kPressFilter)
    kPressDf.dropna(inplace=True)

mClickFig = px.pie(mClickDf, names='APPLICATION', title='Activity measured by mouse clicks')
kPressFig = px.pie(kPressDf, names='APPLICATION', title='Activity measured by keyboard presses')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# layout and CSS stuff from https://dash.plotly.com/layout
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1('Application Activity',
    style = {
        'textAlign': 'center',
        #'color': colors['text']
    }),

    dcc.Graph(id='mClick-pie-chart', figure=mClickFig),

    dcc.Graph(id='kPress-pie-chart', figure=kPressFig)
])

if __name__ == '__main__':
    app.run_server(debug=True)