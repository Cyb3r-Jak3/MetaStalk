"""Makes a table that plots gps timestamp"""
from exif import Image
import plotly.graph_objects as go


def DateTime(photos, log):
    """Makes a table with gps timestamp of photos"""
    gps_datetime = []

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            try:
                if my_image.gps_datestamp:
                    gps_datetime.append(my_image.datetime)
                    log.debug("%s has gps datetime data", each)
            except KeyError:
                log.debug("%s has no gps datetime data ", each)

    fig = go.Figure(
        data=[go.Table(
            header=dict(values=[
                "Photos",
                "GPS Time Stamp"]),
            cells=dict(values=[photos, gps_datetime]))])

    return fig
