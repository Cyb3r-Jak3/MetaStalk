"""Creates a table figure that shows
 photos that did and did not have exif"""
import plotly.graph_objects as go


def Stats(photos, invalid, log):
    """Creates the table of photos"""
    log.info("There are {} photos with metadata and {} without"
             .format(len(photos), len(invalid)))
    fig = go.Figure(
        data=[go.Table(
            header=dict(values=[
                "Photos with Exif Data",
                "Photos without Exif Data"]),
            cells=dict(values=[photos, invalid]))])
    return fig
