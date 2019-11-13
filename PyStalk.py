# -*- coding: utf-8 -*-
"""This script get the exif data from photos
     and plots the gps coordinates on a map """

import argparse
import os
import logging
import sys
from exif import Image
import plotly.express as px
import plotly.graph_objects as go
import utils


def dms2dd(degrees, minutes, seconds):
    """Takes DMS input and creates decimal degrees"""
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    return dd


def GPS_Check(photos, log):
    """Takes a list of photos and creates a geo plot of them"""
    lats = []
    longs = []
    gps_photos = []

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            try:
                if my_image.gps_datestamp:
                    gps_photos.append(each)
                    lats.append(dms2dd(*my_image.gps_latitude))
                    longs.append(dms2dd(*my_image.gps_longitude))
                    log.debug("%s has gps data", each)
            except KeyError:
                log.debug("%s has no gps data ", each)
    points = []
    for x in range(len(lats)):  # pylint: disable=consider-using-enumerate
        points.append((lats[x], longs[x]))

    fig = px.scatter_mapbox(lon=longs, lat=lats, hover_name=gps_photos,
                            title="Geo Locations")
    fig.update_layout(mapbox_style="open-street-map")

    return fig


def Model_Chart(photos, log):
    """Get model information and make a pie chart"""
    models = []

    for each in photos:
        with open(each, 'rb') as image_file:
            my_image = Image(image_file)
            try:
                if my_image.model:
                    models.append(my_image.model)
                    log.debug("%s has model data", each)
            except KeyError:
                log.debug("%s has no model data ", each)

    freq = {}
    for item in models:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    labels = []
    values = []
    for key, value in freq.items():
        labels.append(key)
        values.append(value)

    fig = go.Figure(data=[go.Pie(labels=labels, values=values,
                                 title="Model Information")])
    return fig


def main():
    """ This main function"""
    parser = argparse.ArgumentParser(prog="PyStalk",
                                     description="Tool to graph "
                                                 "image metadata.")
    parser.add_argument('files', nargs='*', default=None,
                        help='Path of photos to check.')
    parser.add_argument('-t', '--test', default=False, action="store_true",
                        help='Does not show the graphs at the end.')
# Logging function from https://stackoverflow.com/a/20663028
    parser.add_argument('-d', '--debug', help="Sets logging level to DEBUG.",
                        action="store_const", dest="loglevel",
                        const=logging.DEBUG, default=logging.WARNING)
    parser.add_argument("-v", "--verbose", help="Sets logging level to INFO",
                        action="store_const", dest="loglevel",
                        const=logging.INFO)
    args = parser.parse_args()

    log = utils.make_logger("PyStalk", args.loglevel)

    if not args.files:
        log.exception("WARNING: No path was inputted. "
                      "This will cause the script to break")
        sys.exit(1)

    for path in args.files:
        isdir = os.path.isdir(path)
        print(isdir)

    photos = []
    invaid_photos = []

    if isdir:
        for file in os.listdir(args.files[0]):
            with open(os.path.join(args.files[0], file), 'rb') as exif:
                exif_image = Image(exif)
                if exif_image.has_exif:
                    photos.append(os.path.join(args.files[0], file))
                else:
                    invaid_photos.append(os.path.join(args.files[0], file))
    else:
        for x, item in enumerate(args.files):
            with open(file, 'rb') as exif:
                exif_image = Image(exif)
                if exif_image.has_exif:
                    photos.append(args.files[x])
                    log.debug("%s has exif data", item)
                else:
                    invaid_photos.append(args.files[x])

    plots = {"gps": GPS_Check(photos, log), "model": Model_Chart(photos, log)}

    utils.graph(plots, log, args.test)


if __name__ == "__main__":
    main()
