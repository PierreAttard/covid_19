import pandas as pd
from src.apps.layout_maker import main_layout as lyt
from src.app import app
import src.constantes as ct
from dash.dependencies import Input, Output, State

layout = lyt.main_lyt()

@app.callback(
    Output("choice-main-country", "options"),
    [Input(ct.ID_DF_CCASES, "children")])
def fill_options(data_death):
    options = [{"label": "France", "value" : "France"}]
    if data_death is None:
        return options
    countries = pd.read_json(data_death, orient='split').loc[:, ct.COUNTRY]
    options = [{"label" : c, "value": c} for c in countries.drop_duplicates()]
    return options


# @app.callback(
#     Output("main-graphe", "children"),
#     [Input("choice-main-country", "value")],
#     [State]
# )