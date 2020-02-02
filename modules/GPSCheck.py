"""Makes geo chart with plots of gps data"""
import plotly.express as px


def GPS_Check(photos, log):
    """Takes a list of photos and creates a geo plot of them"""
    log.info("Starting GPS Check")
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
