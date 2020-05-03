"""Makes geo chart with plots of gps data"""
import logging
import plotly.express as px

log = logging.getLogger("MetaStalk")


def GPS_Check(photos: list) -> px.scatter_mapbox:
    """GPS_Check

    Takes a list of photos and creates a geo plot of them

    Arguments:
        photos {list} -- A list of dictionaries with phot information.

    Returns:
        px.scatter_mapbox -- Map plot with photos plotted.
    """
    log.info("Starting GPS Chart")
    lats = []
    longs = []
    gps_photos = []

    for each in photos:
        if "Longitude" in each.keys():
            gps_photos.append(each["item"])
            lats.append(float(each["Latitude"]))
            longs.append(float(each["Longitude"]))
            log.debug("%s has gps data", each["item"])

    points = []
    for x, _ in enumerate(gps_photos):
        points.append((lats[x], longs[x]))

    fig = px.scatter_mapbox(lon=longs, lat=lats, hover_name=gps_photos,
                            title="Geo Locations")
    fig.update_layout(mapbox_style="open-street-map")

    return fig
