from http import server
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app1 = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server=app1.server

df = pd.read_csv('covid_brasil.csv')

app1.layout = html.Div([
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
    app1.run_server(debug=True)