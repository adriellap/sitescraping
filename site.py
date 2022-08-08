from http import server
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server

df = pd.read_csv('covid_brasil.csv')
obitos = df["Óbitos"]
casos = df['Casos']
app.layout = html.Div([
    html.H2(['Covid-19.'],
    style = {'textAlign':'center', 'font-weight':'bold', 'backgroundColor': '#778899' }
    ),
    html.Hr(),
    dcc.Graph(
    figure={
        'data': [
            {'x': df['Região'], 'y': df['Casos'], 'type': 'bar', 'name': 'Casos'},
            {'x': df['Região'], 'y':  df["Óbitos"], 'type': 'bar', 'name': u'Óbitos'},
        ],
        'layout': {
            'title': 'Casos e Óbitos por Região'
        }
    }
)

])

if __name__ == '__main__':
    app.run_server(debug=True)