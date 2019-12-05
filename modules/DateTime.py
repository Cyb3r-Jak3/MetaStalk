"""Makes a table that plots gps timestamp"""
from exif import Image
import plotly.graph_objects as go


def DateTime(photos, log):
    """Makes a table with gps timestamp of photos"""
    datetime = []
    datetime_org = []
    datetime_dig = []

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            try:
                if my_image.datetime:
                    datetime.append(my_image.datetime)
                    log.debug("%s has datetime data", each)
            except KeyError:
                log.debug("%s has no datetime data ", each)
            except AttributeError:
                log.debug("%s has no datetime data ", each)
            try:
                if my_image.datetime_original:
                    datetime_org.append(my_image.datetime_original)
                    log.debug("%s has datetime_original data", each)
            except KeyError:
                log.debug("%s has no datetime_original data ", each)
            except AttributeError:
                log.debug("%s has no datetime_original data ", each)
            try:
                if my_image.datetime_digitized:
                    datetime_dig.append(my_image.datetime_digitized)
                    log.debug("%s has datetime_digitized data", each)
            except KeyError:
                log.debug("%s has no datetime_digitized data ", each)
            except AttributeError:
                log.debug("%s has no datetime_digitized data ", each)

    fig = go.Figure(
        data=[go.Table(
            header=dict(values=[
                "Photos",
                "Time Stamp",
                "Date time Original",
                "Date time Digitized"
                ]),
            cells=dict(values=[photos, datetime, datetime_org, datetime_dig]))]
        )

    return fig
