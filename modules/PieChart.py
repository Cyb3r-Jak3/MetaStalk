"""Module that makes a pie chart."""
from exif import Image
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
        if pietype == "Focal":
            labels.append("Length: {}".format(key))
        elif pietype == "Flash":
            labels.append("Level: {}".format(key))
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
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            if pietype == "Focal":
                pietype = "focal_length"
            try:
                table.append(getattr(my_image, pietype.lower()))
            except KeyError as ke:
                log.debug("%s has no %s data. Error: %s ", each, pietype, ke)
            except AttributeError as ae:
                log.debug("%s has no %s data. Error: %s", each, pietype, ae)
    if pietype == "focal_length":
        pietype = "Focal"

    return create_chart(table, pietype)
