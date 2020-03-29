import constantes as ct
import matplotlib.pyplot as plt
import base64
import io
import dash_html_components as html

def print_hubbert_formula(df):
    K = df.iloc[0, :].loc[ct.K]
    r = df.iloc[0, :].loc[ct.r]
    nul = "{}{:.0f}{}".format("{", K, "}")
    den = "{}{:.2f}t{}".format("{", r, "}")
    denc = "{}1+e^{}{}".format("{", den, "}")
    s = "$\\frac{}{}$".format(nul, denc)
    plt.figure(figsize=(2, 1))
    plt.text(0.3, 0.5, s, fontdict={"size":20})
    plt.axis('off')
    fig = plt.gcf()
    imgdata = io.BytesIO()
    a=fig.savefig(imgdata, format='png')
    imgdata.seek(0)

    a = imgdata.read()
    encoded_image = base64.b64encode(a)

    return html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))