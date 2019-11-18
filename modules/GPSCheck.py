"""Make geo chart with plots of gps data"""
from exif import Image
import plotly.express as px


def dms2dd(degrees, minutes, seconds):
    """Takes DMS input and creates decimal degrees"""
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    return dd


def GPS_Check(photos, log):
    """Takes a list of photos and creates a geo plot of them"""
    log.info("Starting GPS Check")
    lats = []
    longs = []
    gps_photos = []

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            try:
                if my_image.gps_latitude:
                    gps_photos.append(each)
                    lats.append(dms2dd(*my_image.gps_latitude))
                    longs.append(dms2dd(*my_image.gps_longitude))
                    log.debug("%s has gps data", each)
            except KeyError:
                log.debug("%s has no gps data ", each)
            except AttributeError:
                log.debug("%s has no gps data ", each)
    points = []
    for x in range(len(lats)):  # pylint: disable=consider-using-enumerate
        points.append((lats[x], longs[x]))

    fig = px.scatter_mapbox(lon=longs, lat=lats, hover_name=gps_photos,
                            title="Geo Locations")
    fig.update_layout(mapbox_style="open-street-map")

    return fig
