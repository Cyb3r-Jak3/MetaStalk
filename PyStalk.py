# -*- coding: utf-8 -*-
"""This script get the exif data from photos
     and plots the gps coordinates on a map """
# pylint: disable=invalid-name
import argparse
import os
import logging
import sys
from exif import Image
import plotly.express as px
import plotly.graph_objects as go
import graph_web


log = logging.getLogger(__name__)


def dms2dd(degrees, minutes, seconds):
    """Takes DMS input and creates decimal degrees"""
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    return dd


def GPS_Check(photos):
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
                    log.debug("%s has exif gps data", each)
            except KeyError:
                log.info("%s has no exif data ", each)
    points = []
    for x, item in enumerate(lats):
        points.append((lats[x], longs[x]))
        log.debug("%s added", item)

    fig = px.scatter_mapbox(lon=longs, lat=lats, hover_name=gps_photos)
    fig.update_layout(mapbox_style="open-street-map",
                      title="Geo Locations")

    return fig


def Model_Chart(photos):
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
                log.info("%s has no model data ", each)
                models.append("No Model Data")

    freq = {}
    for item in models:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    labels = []
    values = []
    for key, value in freq.items():
        # print("% s : % d" % (key, value))
        labels.append(key)
        values.append(value)

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    # fig.show()
    return fig


def main():
    """ This main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*', default=None,
                        help='Path of photos to check')
    parser.add_argument('-test', default=False, action="store_true",
                        help='True or false. Set to true to hide the figure.')
    args = parser.parse_args()

    if not args.files:
        log.exception("WARNING: No path was inputted. "
                      "This will cause the script to break")
        sys.exit(1)

    for path in args.files:
        isdir = os.path.isdir(path)

    photos = []

    if isdir:
        for file in os.listdir(args.files[0]):
            photos.append(os.path.join(args.files[0], file))
    else:
        for x, item in enumerate(args.files):
            photos.append(args.files[x])
            log.debug("Adding %s", item)

    plots = [GPS_Check(photos), Model_Chart(photos)]

    graph_web.graph(plots, args.test)


if __name__ == "__main__":
    main()
