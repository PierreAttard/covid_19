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
        className="six columns")
    ])
    return lay


def graphe_country():

    lay = \
        [
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2],
                         'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5],
                         'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )
        ]
    return lay