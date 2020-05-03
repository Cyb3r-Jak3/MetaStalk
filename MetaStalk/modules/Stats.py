"""Creates a table figure that shows
 photos that did and did not have exif"""
import logging
import plotly.graph_objects as go

log = logging.getLogger("MetaStalk")


def Stats(photos: list, invalid: list):
    """Creates the table of photos"""
    log.info("Staring Stats")
    log.debug("There are %s photos with metadata and %s without",
              len(photos), len(invalid))
    simple_photos = []
    for i, _ in enumerate(photos):
        simple_photos.append(photos[i]["item"])
    fig = go.Figure(
        data=[go.Table(
            header=dict(values=[
                "Photos with Metadata",
                "Photos without Metadata"]),
            cells=dict(values=[simple_photos, invalid]))])
    return fig
