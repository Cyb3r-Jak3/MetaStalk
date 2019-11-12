"""Uses dash to create a webpage that contain all the graphs"""
import webbrowser
import dash
import dash_html_components as html
import dash_core_components as dcc
# pylint: disable=invalid-name


def graph(plots, test=False):
    """Creates the graphs"""
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    graphs = []
    for x in plots:
        graphs.append(dcc.Graph(id="graph{}".format(x), figure=x))
    app.layout = html.Div(children=graphs)
    if not test:
        webbrowser.open("http://127.0.0.1:8052", new=2)
        app.run_server(port=8052)
