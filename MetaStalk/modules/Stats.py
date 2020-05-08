"""Creates a table figure that shows
 photos that did and did not have exif"""
import logging
import plotly.graph_objects as go

log = logging.getLogger("MetaStalk")


def stats(photos: list, invalid: list) -> go.Figure():
    """Stats

    Creates the table of photos showing ones with metadata and ones without

    Arguments:
        photos {list} -- List of photos with metadata.
        invalid {list} -- List of photos without metadata.

    Returns:
        go.Figure() -- A plotly table
    """
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
            cells=dict(values=[simple_photos,
                               invalid]))])
    fig.update_layout(title="Photos With and Without Metadata.",
                      title_x=0.5)
    return fig
