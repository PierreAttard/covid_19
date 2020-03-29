import pandas as pd
from apps.layout_maker import main_layout as lyt
from apps.graph_maker import main_graph, formule_maker
from apps.data_managment import load_data
from app import app
import constantes as ct
import models.previsision as proj
from dash.dependencies import Input, Output, State

layout = lyt.main_lyt()

@app.callback(
    Output("choice-main-country", "options"),
    [Input(ct.ID_DF_CCASES, "children")])
def fill_options(data_death):
    return load_data.make_options(data_death)

@app.callback(
    Output("choice-comparison-country", "options"),
    [Input(ct.ID_DF_CCASES, "children")])
def fill_options(data_death):
    return load_data.make_options(data_death)

@app.callback(
    Output("choice-prev-country", "options"),
    [Input(ct.ID_DF_CCASES, "children")])
def fill_options(data_death):
    return load_data.make_options(data_death)


@app.callback(
    Output("main-graphe", "children"),
    [Input("choice-main-country", "value"),
     Input("data-type-radio", "value")],
    [State(ct.ID_DF_CCASES, "children"),
     State(ct.ID_DF_DEATH, "children"),
     State(ct.ID_DF_RECOVERD, "children")]
)
def print_cases(country, data_type, data_ccase, data_death, data_rec):
    data = data_ccase
    if data_type is not None and data_type == ct.DEATH:
        data = data_death
    elif data_type is not None and data_type == ct.RECOVERD:
        data = data_rec

    df = pd.read_json(data, orient="split")
    return main_graph.make_graphe(df, country, data_type)

@app.callback(
    Output("main-graphe-comparison", "children"),
    [Input("choice-comparison-country", "value"),
     Input("data-type-radio-comparison", "value")],
    [State(ct.ID_DF_CCASES, "children"),
     State(ct.ID_DF_DEATH, "children"),
     State(ct.ID_DF_RECOVERD, "children")]
)
def print_cases(country, data_type, data_ccase, data_death, data_rec):
    data = data_ccase
    if data_type is not None and data_type == ct.DEATH:
        data = data_death
    elif data_type is not None and data_type == ct.RECOVERD:
        data = data_rec

    df = pd.read_json(data, orient="split")
    return main_graph.make_graphe(df, country, data_type)

@app.callback(
    Output("prev-country", "children"),
    [Input("choice-prev-country", "value"),
     Input("data-type-radio-prev", "value")],
    [State(ct.ID_DF_CCASES_COMPLETE, "children"),
     State(ct.ID_DF_DEATH_COMPLETE, "children"),
     State(ct.ID_DF_RECOVERD_COMPLETE, "children")]
)
def prev_cumul(country, data_type, data_ccase, data_death, data_rec):
    data = data_ccase
    if data_type is not None and data_type == ct.DEATH:
        data = data_death
    elif data_type is not None and data_type == ct.RECOVERD:
        data = data_rec

    df = pd.read_json(data, orient="split")
    hubbert_country = proj.HubbertCountry(df, country)
    prev_hubbert_country = proj.PrevHubbertCountry(hubbert_country, 50)
    return prev_hubbert_country.get_prev().to_json(orient='split', date_format='iso')

@app.callback(
    [Output("prev-graphe", "children"),
     Output("formule-prev-cumul", "children"),
     Output("confiance-prev-cumul", "children"),
     Output("score-prev", "value")],
    [Input("prev-country", "children")]
)
def prev_cumul(data):
    df = pd.read_json(data, orient="split")
    country = df.iloc[0, :].loc[ct.COUNTRY]
    score = df.iloc[0, :].loc[ct.SCORE]
    score = "{:.2f}".format(score)

    return main_graph.make_proj_graphe(df, country), \
           formule_maker.print_hubbert_formula(df), \
           score, \
           float(score)