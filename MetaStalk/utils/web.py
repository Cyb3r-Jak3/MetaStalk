"""Uses dash to create a webpage that contain all the graphs"""
import timeit
import logging
import webbrowser
import dash
import dash_html_components as html
import dash_core_components as dcc


log = logging.getLogger("MetaStalk")


def graph(plots: dict, t_start: float, test=False):
    """graph

    Displays all the plots that are passed to it.

    Arguments:
        plots {dict} -- All the plot that get displayed
        t_start {float} -- The start time of MetaStalk

    Keyword Arguments:
        test {bool} -- Whether or not to show the web page (default: {False})
    """
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.title = "MetaStalk"
    graphs = []
    for name, chart in plots.items():
        graphs.append(dcc.Graph(id="graph-{}".format(name), figure=chart))
    t_stop = timeit.default_timer()
    app.layout = html.Div([
        html.H1("MetaStalk", style={"textAlign": "center"}),
        html.H6(html.A('Cyber Jake', href="https://twitter.com/Cyb3r_Jak3"),
                style={"textAlign": "center"}),
        html.Div(children=graphs),
        html.P("Time Taken = {0:.2f} seconds".format(t_stop - t_start),
               style={"textAlign": "center"})
    ])
    if not test:
        webbrowser.open("http://localhost:8052", new=2)
        app.run_server(port=8052)
    else:
        log.info("Test flag was set. No webpage will be shown.")
        log.info("Time Taken = {0:.2f} seconds".format(t_stop - t_start))
