import dash


app = dash.Dash(__name__, url_base_pathname="/apps/main/")
server = app.server
app.title = "Analyse Covid-19"

app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True