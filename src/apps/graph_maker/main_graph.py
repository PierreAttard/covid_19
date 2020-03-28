import src.constantes as ct
import plotly.graph_objects as go
import dash_core_components as dcc

def make_graphe(df, countries, data_type):
    """

    :param df:
    :param country:
    :return:
    """
    if df is None or countries is None:
        return go.Figure()

    if isinstance(countries, str):
        countries = [countries]

    title = "cumul {} number for {}".format(data_type, countries[0])
    if len(countries) > 1:
        title = "comparison between countries for {}".format(data_type)

    df = df.groupby([ct.COUNTRY, ct.DATES]).sum().reset_index()
    df = df.loc[df.loc[:, ct.COUNTRY].isin(countries), :]
    dff = df.reset_index()

    fig = go.Figure()
    for country in countries:
        df = dff.loc[dff.loc[:, ct.COUNTRY] == country, :]
        df.sort_values(ct.DATES, inplace=True)
        dates = df.loc[:, ct.DATES]
        values = df.loc[:, ct.VAL]


        g = go.Scatter(
            x=dates,
            y=values,
            mode="lines+markers",
            name="cumul {} number for {}".format(data_type, country)
        )
        fig.add_trace(g)

    fig.update_layout(
        title_text=title,
        xaxis=dict(title_text=ct.DATES),
        yaxis=dict(title_text=data_type),
        legend=dict(x=0, y=1)
    )

    return dcc.Graph(figure=fig)
