# -*- coding: utf-8 -*-
"""This script get the exif data from photos
and creates graphs from the metadata"""

import argparse
import os
import logging
import sys
import timeit
from exif import Image
import utils
import modules

start = timeit.default_timer()


def setup():
    """ Sets up PyStalk and parses arguments"""
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
    log.info("Starting up")
    if not args.files:
        log.error("ERROR: No path was inputted.")
        sys.exit(1)
    run(args, log)


def run(args, log):
    """Process files and generates graphs"""

    for path in args.files:
        isdir = os.path.isdir(path)
        log.debug("Detected path as a directory")

    if isdir:
        photos, invalid_photos = directory_search(args.files[0], log)
    else:
        photos, invalid_photos = file_search(args.files, log)

    plots = {
        "STATS": modules.Stats(photos, invalid_photos, log),
        "GPS": modules.GPS_Check(photos, log),
        "Timestamp": modules.date_time(photos, log),
        "Model": modules.PieChart(photos, "Model", log),
        "Flash": modules.PieChart(photos, "Flash", log),
        "Focal": modules.PieChart(photos, "Focal", log),
        "Software": modules.PieChart(photos, "Software", log)
        }

    utils.graph(plots, log, start, args.test)


def directory_search(files: list, log):
    """
    Used to append all file in a directory
    """
    valid, invalid = [], []
    for item in os.listdir(files):
        with open(os.path.join(files, item), 'rb') as raw_photo:
            try:
                exif_image = Image(raw_photo)
                if exif_image.has_exif:
                    valid.append(os.path.join(files, item))
                    log.debug("%s has exif data", item)
                else:
                    invalid.append(os.path.join(files, item))
            except AssertionError:
                log.warning("Error with %s", raw_photo)
    return valid, invalid


def file_search(files: list, log):
    """
    Used to append files if the path is not a directory
    """
    valid, invalid = [], []
    for x, item in enumerate(files):
        with open(item, 'rb') as raw_photo:
            try:
                exif_image = Image(raw_photo)
                if exif_image.has_exif:
                    valid.append(files[x])
                    log.debug("%s has exif data", item)
                else:
                    invalid.append(files[x])
            except AssertionError:
                log.warning("Error with %s", raw_photo)
    return valid, invalid


if __name__ == "__main__":
    setup()
