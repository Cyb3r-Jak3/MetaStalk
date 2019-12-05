"""Module that makes a bar chart that contains focal length information"""
from exif import Image
import plotly.graph_objects as go


def Focal_Chart(photos, log):
    """Gets Focal information and makes a bar chart"""
    log.info("Starting Focal")
    focal = []

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            try:
                if my_image.focal_length:
                    focal.append(my_image.focal_length)
                    log.debug("%s has focal data", each)
            except KeyError:
                log.debug("%s has no focal data ", each)
            except AttributeError:
                log.debug("%s has no attribute focal data ", each)

    freq = {}
    for item in focal:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    labels = []
    values = []
    for key, value in freq.items():
        labels.append("Length: {}".format(key))
        values.append(value)

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title_text="Focal Length")

    return fig
