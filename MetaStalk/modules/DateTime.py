"""Makes a table that plots GPS timestamp or other timestamp metadata."""
import logging
import plotly.graph_objects as go

log = logging.getLogger("MetaStalk")


def date_time(photos: list) -> go.Figure():
    """date_time

    Makes a table with timestamp of photos.
    There are three name that DateTime data can be under `Creation date`,
    `Date-time original`, `Date-time digitized` and a column in made
    for each type.

    Arguments:
        photos {list} -- A list of dictionaries with phot information.

    Returns:
        go.Figure -- A plotly Table with the DateTime data.
    """
    log.info("Starting DateTime Charts")
    datetime, datetime_original, datetime_digitized = [], [], []
    types = [datetime,
             datetime_original,
             datetime_digitized]
    types_str = ["Image DateTime",
                 "EXIF DateTimeOriginal",
                 "EXIF DateTimeDigitized",
                 "GPS GPSDate"]

    simple_photos = []
    for i, _ in enumerate(photos):
        simple_photos.append(photos[i]["item"])

    for each in photos:
        for i, _ in enumerate(types):
            try:
                date_type = str(each[types_str[i]]).replace(":", "/", 2)
                types[i].append(date_type)
                log.debug("%s has %s data", each["item"], types_str[i])
            except KeyError:
                log.info("%s has no %s data ", each["item"], types_str[i])

    fig = go.Figure(
        data=[go.Table(
            header=dict(values=[
                "Photo",
                "Image DateTime",
                "Date Time Original",
                "Date Time Digitized"
            ]),
            cells=dict(values=[simple_photos,
                               datetime,
                               datetime_original,
                               datetime_digitized]))]
    )
    fig.update_layout(title="Timestamp Information",
                      title_x=0.5)
    return fig
