import dash_core_components as dcc
import dash_html_components as html
import src.apps.layout_maker.main_data_lay as lyt_grp
import src.constantes as ct
from src.apps.data_managment import load_data

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

def main_lyt():

    df_death = load_data.get_data_url(ct.DEATH)
    df_ccase = load_data.get_data_url(ct.CONFIRMED_CASE)
    df_recoverd = load_data.get_data_url(ct.RECOVERD)

    # complete data
    df_death_hist = load_data.get_daily_data(df_death)
    df_ccase_hist = load_data.get_daily_data(df_ccase)
    df_recoverd_hist = load_data.get_daily_data(df_recoverd)

    lay = html.Div([
        html.H1('Analyse COVID-19'),
        dcc.Tabs(id="tabs-main", value='tab-1-example', children=[
            dcc.Tab(label='Cumulative view',
                    children=[lyt_grp.choice_data(),lyt_grp.comparaison_data(), lyt_grp.proj_data()],
                    style=tab_style,
                    selected_style=tab_selected_style),
            dcc.Tab(label='Daily view', children='tab-2-example', style=tab_style, selected_style=tab_selected_style),
        ]),
        html.Div(id='tabs-content-example'),
        html.Div(id=ct.ID_DF_DEATH, children=df_death.to_json(orient='split', date_format='iso'), style={'display': 'none'}),
        html.Div(id=ct.ID_DF_CCASES, children=df_ccase.to_json(orient='split', date_format='iso'), style={'display': 'none'}),
        html.Div(id=ct.ID_DF_RECOVERD, children=df_recoverd.to_json(orient='split', date_format='iso'), style={'display': 'none'}),
        html.Div(id=ct.ID_DF_DEATH_COMPLETE, children=df_death_hist.to_json(orient='split', date_format='iso'),
                 style={'display': 'none'}),
        html.Div(id=ct.ID_DF_CCASES_COMPLETE, children=df_ccase_hist.to_json(orient='split', date_format='iso'),
                 style={'display': 'none'}),
        html.Div(id=ct.ID_DF_RECOVERD_COMPLETE, children=df_recoverd_hist.to_json(orient='split', date_format='iso'),
                 style={'display': 'none'})
    ])
    return lay
