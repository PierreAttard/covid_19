import pandas as pd
import numpy as np
import src.constantes as ct
from sklearn.linear_model import LinearRegression

def sigmoid(K, r, t, t0):
    """

    :param K: Limite de la cumulative
    :param r: taux d'acroissement
    :param t: temps
    :param t0: pas de temps du point d'inflexion
    :return: float or list of float
    """
    return K/(1 + np.exp(-r*(t-t0)))


class HubbertCountry:

    def __init__(self, df, country):
        self._df = df.loc[df.loc[:, ct.COUNTRY] == country, :]
        self._country = country
        self._treatment()
        self._set_t0()
        self._make_data_hist()

    def _treatment(self):
        cond = (self._df.loc[:, ct.CUMUL] > 0) & (self._df.loc[:, ct.DP_DQ] < 1) & (self._df.loc[:,  ct.DP_DQ] > 0)
        X = self._df.loc[cond, ct.CUMUL].values.reshape(-1, 1)
        y = self._df.loc[cond, ct.DP_DQ]
        lm_log = LinearRegression()
        lm_log.fit(X, y)
        intercept = lm_log.intercept_
        coefs = lm_log.coef_[0]
        k = intercept
        urr = -k / coefs
        print("Coef : {}, intercept : {}, k = {}, urr : {}".format(coefs, intercept, k, urr))
        self._K = urr
        self._r = k

    def _set_t0(self):
        ix = (self._df.loc[:, ct.CUMUL] - sigmoid(K=self._K, r=self._r, t=0, t0=0)).abs().idxmin()
        self._t0 = self._df.loc[:ix, :].shape[0]
        print("t0 : {}".format(self._t0))

    def _make_data_hist(self):
        self._df_proj = self._df.copy()
        self._df_proj[ct.N] = np.arange(1, self._df.shape[0] + 1)
        self._df_proj[ct.PREV] = sigmoid(K=self._K, r=self._r, t=self._df_proj.loc[:, ct.N], t0=self._t0)

    def get_data(self):
        return self._df_proj

    def get_country(self):
        return self._country



class PrevHubbertCountry:

    def __init__(self, hubbertCountry, nb_days):
        self._hc = hubbertCountry
        self._country = self._hc.get_country()
        self._K = self._hc._K
        self._r = self._hc._r
        self._t0 = self._hc._t0
        self._nb_days = nb_days
        self._make_prevision()

    def _make_prevision(self):
        df_hist = self._hc.get_data()
        df_proj = pd.DataFrame(columns=df_hist.columns,
                               index=np.arange(df_hist.index.max(), df_hist.index.max() + self._nb_days))
        df_proj[ct.COUNTRY] = self._country
        df_proj[ct.N] = np.arange(df_hist.loc[:, ct.N].max()+1, df_hist.loc[:, ct.N].max()+1 + self._nb_days)
        df_proj[ct.DATES] = pd.date_range(df_hist.loc[:, ct.DATES].max(), freq="D", periods=self._nb_days+1)[1:]
        df_proj[ct.PREV] = sigmoid(K=self._K, r=self._r, t=df_proj.loc[:, ct.N], t0=self._t0)
        df_proj[ct.LAT] = df_hist.loc[:, ct.LAT].min()
        df_proj[ct.LONG] = df_hist.loc[:, ct.LONG].min()
        df_hist_proj = pd.concat([df_hist, df_proj])
        self._df_prev = df_hist_proj

    def get_prev(self):
        return self._df_prev



