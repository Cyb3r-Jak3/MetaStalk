"""Module that makes a pie chart."""
import logging
import plotly.graph_objects as go

log = logging.getLogger("MetaStalk")


def create_chart(table: list, pielabel: str) -> go.Figure():
    """create_chart

    Creates the pie chart by frequency of items in a dictionary.

    Arguments:
        table {list} -- [description]
        pielabel {str} -- The label of the pie chart.

    Returns:
        go.Figure -- A plotly PieChart
    """
    freq = {}
    for item in table:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    (labels, values) = ([], [])
    for key, value in freq.items():
        if pielabel == "Camera focal":
            labels.append("Length: {}".format(key))
        else:
            labels.append(key)
        values.append(value)

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title="{} Information".format(pielabel))

    return fig


def PieChart(photos: list, pietype: str) -> go.Figure():
    """PieChart

    Parses information and returns a pie chart

    Arguments:
        photos {list} -- A list of dictionaries with phot information.
        pietype {str} -- The type of metadata for the pie chart

    Returns:
        go.Figure -- A plotly PieChart
    """
    log.info("Staring %s Chart", pietype)
    table = []

    for each in photos:
        try:
            table.append(each[pietype])
        except KeyError:
            log.debug("%s has no %s data", each["item"], pietype)

    return create_chart(table, pietype)
