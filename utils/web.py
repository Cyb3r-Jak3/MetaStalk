"""Uses dash to create a webpage that contain all the graphs"""
import webbrowser
import dash
import dash_html_components as html
import dash_core_components as dcc


def graph(plots, log, test=False):
    """Creates the graphs"""
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    graphs = []
    for name, chart in plots.items():
        graphs.append(dcc.Graph(id="graph-{}".format(name), figure=chart))
    app.layout = html.Div([
        html.H1("PyStalk", style={"textAlign": "center"}),
        html.H6("By Jacob White", style={"textAlign": "center"}),
        html.Div(children=graphs),
        ])
    if not test:
        webbrowser.open("http://localhost:8052", new=2)
        try:
            app.run_server(port=8052)
        except KeyboardInterrupt:
            log.info("Interput received. Exiting.")
    else:
        log.info("Test flag was set. No webpage will be shown.")
