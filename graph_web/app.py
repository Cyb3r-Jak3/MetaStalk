"""Uses dash to create a webpage that contain all the graphs"""
import dash
import dash_html_components as html
import dash_core_components as dcc
# pylint: disable=invalid-name


def graph(plots):
    """Creates the graphs"""
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    graphs = []
    for x in plots:
        graphs.append(dcc.Graph(id="graph", figure=x))
    print(graphs)
    app.layout = html.Div(children=graphs)
    app.run_server(port=8052)
