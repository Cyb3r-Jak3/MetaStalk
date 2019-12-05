"""Module that makes a bar chart that contains software information"""
from exif import Image
import plotly.graph_objects as go


def Software_Chart(photos, log):
    """Gets Software information and makes a bar chart"""
    log.info("Starting Software")
    software = []

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            try:
                if my_image.software:
                    software.append(my_image.software)
                    log.debug("%s has software data", each)
            except KeyError:
                log.debug("%s has no software data ", each)
            except AttributeError:
                log.debug("%s has no software data ", each)

    freq = {}
    for item in software:
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
    fig.update_layout(title_text="Software")

    return fig
