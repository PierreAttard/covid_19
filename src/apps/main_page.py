from src.apps.layout_maker import main_layout as lyt
from src.app import app
from dash.dependencies import Input, Output

layout = lyt.main_lyt()

@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)