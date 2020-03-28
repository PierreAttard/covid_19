import dash_core_components as dcc
import dash_html_components as html

def make_dropdown(id, options, default="France", multi=False):
    lay = \
        dcc.Dropdown(
            id=id,
            options=options,
            value=default,
            multi=multi
        )
    return lay

def choice_data():
    lay = \
    html.Div([
        html.Div([
            html.Div(
                children=[
                    make_dropdown(id="choice-main-country",
                                  options=[{"label": "France", "value" : "France"}],
                                  default="France")
                ],
                className="graphCadre"
            )
        ],
        className="six columns"),
        html.Div([
           html.Div(
               children=[
                   html.Div(id="main-graphe")
               ],
               className="graphCadre"
           )
        ],
        className="six columns")
    ],
    )
    return lay

