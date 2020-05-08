"""utils.parse
---
Parse needed to make exifread dictionaries easier"""


def gps_parse(tags: dict):
    """Returns GPS degrees"""
    latitude = tags["GPS GPSLatitude"]
    latitude_ref = tags["GPS GPSLatitudeRef"]
    longitude = tags["GPS GPSLongitude"]
    longitude_ref = tags["GPS GPSLongitudeRef"]
    if latitude:
        lat_value = _convert_to_degrees(latitude)
        if latitude_ref.values != 'N':
            lat_value = -lat_value
    if longitude:
        lon_value = _convert_to_degrees(longitude)
        if longitude_ref.values != 'E':
            lon_value = -lon_value
    return {'latitude': lat_value, 'longitude': lon_value}


def _convert_to_degrees(value) -> float:
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degrees in float format
    :param value:
    :type value: exifread.utils.Ratio
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)
