import src.constantes as ct
import plotly.graph_objects as go
import dash_core_components as dcc

def make_graphe(df, country, data_type):
    """

    :param df:
    :param country:
    :return:
    """
    if df is None or country is None:
        return go.Figure()

    df = df.groupby([ct.COUNTRY, ct.DATES]).sum().reset_index()
    df = df.loc[df.loc[:, ct.COUNTRY] == country, :]
    df = df.reset_index()

    df.sort_values(ct.DATES, inplace=True)
    dates = df.loc[:, ct.DATES]
    values = df.loc[:, ct.VAL]

    fig = go.Figure()
    g1 = go.Scatter(
        x=dates,
        y=values,
        mode="lines+markers",
        name="cumul {} number for {}".format(data_type, country)
    )
    fig.add_trace(g1)

    return dcc.Graph(figure=fig)
