"""Module that makes a pie chart."""
import plotly.graph_objects as go


def create_chart(table, pietype):
    """Creates the pie chart"""
    freq = {}
    for item in table:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    (labels, values) = ([], [])
    for key, value in freq.items():
        if pietype == "Camera focal":
            labels.append("Length: {}".format(key))
        else:
            labels.append(key)
        values.append(value)

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title="{} Information".format(pietype))

    return fig


def PieChart(photos, pietype, log):
    """Gets information and makes a pie chart"""
    log.info("Staring %s Chart", pietype)
    table = []

    for each in photos:
        try:
            table.append(each[pietype])
        except KeyError:
            log.info("%s has not %s data", each["item"], pietype)

    return create_chart(table, pietype)
