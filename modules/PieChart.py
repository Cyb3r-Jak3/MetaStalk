"""Module that makes a pie chart."""
from exif import Image
import plotly.graph_objects as go


def Pi_Chart(photos, pitype, log):  # pylint: disable=too-many-branches
    """Get model information and make a pie chart"""
    log.info("Staring %s Chart", pitype)
    table = []

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            if pitype == "Model":
                try:
                    if my_image.model:
                        table.append(my_image.model)
                        log.debug("%s has %s data", each, pitype)
                except KeyError:
                    log.debug("%s has no %s data ", each, pitype)
                except AttributeError:
                    log.debug("%s has no %s data ", each, pitype)
            elif pitype == "Software":
                try:
                    if my_image.software:
                        table.append(my_image.software)
                        log.debug("%s has %s data", each, pitype)
                except KeyError:
                    log.debug("%s has no %s data ", each, pitype)
                except AttributeError:
                    log.debug("%s has no %s data ", each, pitype)

    freq = {}
    for item in table:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    labels = []
    values = []
    for key, value in freq.items():
        labels.append(key)
        values.append(value)

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title="{} Information".format(pitype))

    return fig
