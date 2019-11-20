"""Module that makes a bar chart that contains flash information"""
from exif import Image
import plotly.graph_objects as go


def Flash_Chart(photos, log):
    """Gets Flash information and makes a bar chart"""
    log.info("Starting Flash")
    flash = []

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            try:
                if my_image.flash:
                    flash.append(my_image.flash)
                    log.debug("%s has flash data", each)
            except KeyError:
                log.debug("%s has no flash data ", each)
            except AttributeError:
                log.debug("%s has no flash data ", each)

    fig = go.Figure([go.Bar(x=photos, y=flash)])
    fig.update_layout(title_text="Flash Level")

    return fig
