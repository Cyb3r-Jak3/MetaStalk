"""Makes a table that plots gps timestamp"""
from exif import Image
import plotly.graph_objects as go


def date_time(photos, log):
    """Makes a table with gps timestamp of photos"""
    datetime = []
    datetime_original = []
    datetime_digitized = []
    types = [datetime, datetime_original, datetime_digitized]
    types_str = ["datetime", "datetime_original", "datetime_digitized"]

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            for i, _ in enumerate(types):
                log.debug(i)
                try:
                    types[i].append(getattr(my_image, types_str[i]))
                    log.debug("%s has %s data", each, types_str[i])
                except AttributeError:
                    log.debug("%s has no %s data ", each, types_str[i])

    fig = go.Figure(
        data=[go.Table(
            header=dict(values=[
                "Photos",
                "Time Stamp",
                "Date time Original",
                "Date time Digitized"
                ]),
            cells=dict(values=[photos, datetime, datetime_original,
                               datetime_digitized]))]
        )

    return fig
