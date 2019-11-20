"""Module that makes a pie chart that contains model information"""
from exif import Image
import plotly.graph_objects as go


def Model_Chart(photos, log):
    """Get model information and make a pie chart"""
    log.info("Staring Model Chart")
    models = []

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            try:
                if my_image.model:
                    models.append(my_image.model)
                    log.debug("%s has model data", each)
            except KeyError:
                log.debug("%s has no model data ", each)
            except AttributeError:
                log.debug("%s has no model data ", each)

    freq = {}
    for item in models:
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
    fig.update_layout(title="Model Information")

    return fig
