import dash_core_components as dcc
import dash_html_components as html
import src.constantes as ct

def make_dropdown(id, options, default="France", multi=False):
    lay = \
        dcc.Dropdown(
            id=id,
            options=options,
            value=default,
            multi=multi
        )
    return lay

def radio_buttons(id):
    lay = \
        html.Div([
            html.Div(children="Choix du type de données : ", style={"display": "inline-block"}),
            dcc.RadioItems(
                id=id,
                options=[
                    {'label': "Cas confirmes", 'value': ct.CONFIRMED_CASE},
                    {'label': "Morts", 'value': ct.DEATH},
                    {'label': "Guerison", 'value': ct.RECOVERD}
                ],
                value=ct.DEATH,
                labelStyle={'display': 'inline-block'},
                style={'display': 'inline-block'}
            )
        ])
    return lay

def choice_data():
    lay = \
    html.Div([
        html.Div([
            html.Div(
                children=[
                    make_dropdown(id="choice-main-country",
                                  options=[{"label": "France", "value" : "France"}],
                                  default="France"),
                    html.Div(style={"margin-top": "20px"}),
                    radio_buttons(id="data-type-radio")
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

def comparaison_data():
    lay = \
    html.Div([
        html.Div([
            html.Div(
                children=[
                    make_dropdown(id="choice-comparison-country",
                                  options=[{"label": "France", "value" : "France"}],
                                  default=["France", "Germany"],
                                  multi=True),
                    html.Div(style={"margin-top": "20px"}),
                    radio_buttons(id="data-type-radio-comparison")
                ],
                className="graphCadre"
            )
        ],
        className="six columns"),
        html.Div([
           html.Div(
               children=[
                   html.Div(id="main-graphe-comparison")
               ],
               className="graphCadre"
           )
        ],
        className="six columns")
    ],
    )
    return lay

def proj_data():
    lay = \
    html.Div([
        html.Div([
            html.Div(
                children=[
                    make_dropdown(id="choice-prev-country",
                                  options=[{"label": "France", "value" : "France"}],
                                  default="France"),
                    html.Div(style={"margin-top": "20px"}),
                    radio_buttons(id="data-type-radio-prev"),
                    html.Div(style={"margin-top": "20px"}),
                    html.Div([
                        html.Div(children="Formule : ", style={"display":"inline-block"}),
                        html.Div(id="formule-prev-cumul", style={"display":"inline-block"})
                    ]),
                    html.Div(style={"margin-top": "20px"}),
                    html.Div([
                        html.Div(children="confiance : ", style={"display": "inline-block"}),
                        html.Div(id="confiance-prev-cumul", style={"display": "inline-block"})
                    ])


                ],
                className="graphCadre"
            )
        ],
        className="six columns"),
        html.Div([
           html.Div(
               children=[
                   html.Div(id="prev-graphe")
               ],
               className="graphCadre"
           )
        ],
        className="six columns"),

        html.Div(id="prev-country", children="{}", style={'display': 'none'})
    ],
    )
    return lay
