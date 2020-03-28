import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from src.app import app
from src.apps import main_page

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/apps/main/':
         return main_page.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)