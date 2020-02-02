# -*- coding: utf-8 -*-
"""This script get the exif data from photos
and creates graphs from the metadata"""
import argparse
import os
import logging
import sys
import timeit
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import utils
import modules


t_start = timeit.default_timer()


def start():
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


def run(args, log: logging.Logger):
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
        "Model": modules.PieChart(photos, "Camera model", log),
        "Manufacturer": modules.PieChart(photos, "Camera manufacturer", log),
        "Focal": modules.PieChart(photos, "Camera focal", log),
        "Producer": modules.PieChart(photos, "Producer", log)
        }

    utils.graph(plots, log, t_start, args.test)


def directory_search(files: list, log: logging.Logger):
    """ Used to append all file in a directory """
    valid, invalid = [], []
    for item in os.listdir(files):
        item_path = os.path.join(files, item)
        log.debug(item_path)
        parser = createParser(item_path)
        metadata = extractMetadata(parser).exportDictionary()["Metadata"]
        if metadata:
            metadata["item"] = item_path
            valid.append(metadata)
            log.debug("%s has metadata", item)
        else:
            metadata["item"] = item_path
            invalid.append(metadata)
            log.debug("%s has no metadata", item)
    return valid, invalid


def file_search(files: list, log: logging.Logger):
    """ Used to append files if the path is not a directory """
    valid, invalid = [], []
    for x, item in enumerate(files):
        parser = createParser(item)
        metadata = extractMetadata(parser).exportDictionary()["Metadata"]
        if metadata:
            valid.append(files[x])
            log.debug("%s has metadata", item)
        else:
            invalid.append(files[x])
            log.debug("%s has no metadata data", item)
    return valid, invalid


if __name__ == "__main__":
    start()
