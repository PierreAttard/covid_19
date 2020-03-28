import pandas as pd
import numpy as np
import datetime
import requests
import io
import src.constantes as ct



def get_data_url(choice):

    url_base = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
    url_confirmed = "{}{}".format(url_base, "time_series_covid19_confirmed_global.csv")
    url_deaths = "{}{}".format(url_base, "time_series_covid19_deaths_global.csv")
    url_recoverd = "{}{}".format(url_base, "time_series_covid19_recovered_global.csv")

    url = url_confirmed
    if choice not in [ct.CONFIRMED_CASE, ct.DEATH, ct.RECOVERD]:
        raise ValueError("{} not in {}".format(choice, ",".join([ct.CONFIRMED_CASE, ct.DEATH, ct.RECOVERD])))

    if choice == ct.DEATH:
        url = url_deaths
    elif choice == ct.RECOVERD:
        url = url_recoverd

    return get_data(url)

def get_data(url):

    data_web = requests.get(url)
    df = pd.read_csv(io.BytesIO(data_web.content))

    columns = df.columns
    first_columns = [ct.PROV, ct.COUNTRY, ct.LAT, ct.LONG]
    dates_col = columns[4:].tolist()
    new_columns = first_columns + columns[4:].tolist()
    df.columns = new_columns

    df[ct.ID] = \
        df.loc[:, [ct.COUNTRY, ct.PROV]]\
            .apply(lambda x : x.loc[ct.COUNTRY] if isinstance(x.loc[ct.PROV], float) and np.isnan(x.loc["prov"])
                                                    else "{} {}".format(x.loc[ct.COUNTRY], x.loc["prov"]), axis=1)
    dfl = pd.melt(df, id_vars=[ct.ID], value_vars=dates_col)\
            .merge(df.loc[:, [ct.ID] + first_columns], on=ct.ID, how="left")
    dfl = dfl.loc[:, [ct.ID, ct.PROV, ct.COUNTRY, ct.LAT, ct.LONG, "variable", ct.VAL]]
    dfl.columns = [ct.ID, ct.PROV, ct.COUNTRY, ct.LAT, ct.LONG, ct.DATES, ct.VAL]
    dfl.loc[:, ct.DATES] = dfl.loc[:, ct.DATES].apply(lambda x : datetime.datetime.strptime(x, "%m/%d/%y"))

    return dfl
