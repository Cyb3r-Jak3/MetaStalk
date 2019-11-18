# -*- coding: utf-8 -*-
"""This script get the exif data from photos
     and creates graphs from the metadata"""

import argparse
import os
import logging
import sys
from exif import Image
import utils
import modules


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
    log.info("Starting up")

    if not args.files:
        log.error("WARNING: No path was inputted. "
                  "This will cause the script to break")
        sys.exit(1)

    for path in args.files:
        isdir = os.path.isdir(path)
        log.debug("Detected path as a directory")

    photos = []
    invalid_photos = []

    if isdir:
        for file in os.listdir(args.files[0]):
            with open(os.path.join(args.files[0], file), 'rb') as exif:
                exif_image = Image(exif)
                if exif_image.has_exif:
                    photos.append(os.path.join(args.files[0], file))
                else:
                    invalid_photos.append(os.path.join(args.files[0], file))
    else:
        for x, item in enumerate(args.files):
            with open(item, 'rb') as exif:
                exif_image = Image(exif)
                if exif_image.has_exif:
                    photos.append(args.files[x])
                    log.debug("%s has exif data", item)
                else:
                    invalid_photos.append(args.files[x])

    plots = {
        "STATS": modules.Stats(photos, invalid_photos, log),
        "GPS": modules.GPS_Check(photos, log),
        "Model": modules.Model_Chart(photos, log),
        "Timestamp": modules.DateTime(photos, log),
        }

    utils.graph(plots, log, args.test)


if __name__ == "__main__":
    main()
