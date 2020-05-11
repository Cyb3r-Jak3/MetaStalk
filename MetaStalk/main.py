# -*- coding: utf-8 -*-
"""Main function of MetaStalk.
Run get any metadata from photos
and creates graphs from the metadata using MetaStalk.Modules"""
import argparse
from collections import OrderedDict
import os
import logging
import timeit
import exifreader
import MetaStalk.utils as utils
import MetaStalk.modules as modules


class MetaStalk():
    """MetaStalk.
    ---

    Main Class for all MetaStalk work
    """
    def __init__(self):
        self.log = logging.getLogger("MetaStalk")
        self.t_start = timeit.default_timer()
        self.valid, self.invalid = [], []
        self.plots = {}

    def run(self, args):
        """Run

        Process files and generates graphs

        Arguments:
            args {argparse.Namespace} -- The arguments from start()
            log {logging.Logger} -- Logger
        """
        self.parse_files(args.files)

        self.plots = {
            "Stats": modules.stats(self.valid, self.invalid),
            "GPS": modules.gps_check(self.valid),
            "Timestamp": modules.date_time(self.valid),
            "Model": modules.pie_chart(self.valid, "Image Model"),
            "Manufacturer": modules.pie_chart(self.valid, "Image Make"),
            "Focal": modules.pie_chart(self.valid, "EXIF FocalLength"),
            "Producer": modules.pie_chart(self.valid, "Image Software")
        }
        if args.alphabetic:
            self.plots = OrderedDict(sorted(self.plots.items()))
        if args.export:
            utils.export(args.export, args.output, self.plots)

        utils.graph(self.plots, self.t_start, args.test, args.no_open)

    def parse_files(self, path_list: list):
        """parse_files
        ---

        Use to complete the direcotry parsing and file adding.

        Arguments:
            files {list} -- The list of paths to search for files
        """
        for path in path_list:
            if os.path.isdir(path):
                self.log.debug("Detected path as a directory")
                for root, _, files in os.walk(path):
                    for item in files:
                        item_path = os.path.join(root, item)
                        self.file_search(item_path)
            else:
                self.file_search(path)

    def file_search(self, parse_file: str):
        """file_search

        Used to append files if the path is not a directory.

        Arguments
            parse_files {str} -- Name of the file to parse.
        """
        with open(parse_file, "rb") as f:
            tags = exifreader.process_file(f)
            f.close()
        if tags:
            tags["item"] = parse_file
            self.valid.append(tags)
            self.log.debug("%s has metadata", parse_file)
        else:
            self.invalid.append(parse_file)
            self.log.debug("%s has no metadata data", parse_file)


def start():
    """ start
    ---

    Function needed to start MetaStalk. Does all the argument parsing.
    """
    parser = argparse.ArgumentParser(prog="MetaStalk",
                                     description="Tool to graph "
                                                 "image metadata.")
    parser.add_argument('files', nargs='*', default=None,
                        help='Path of photos to check.')
    parser.add_argument("-a", "--alphabetic", help="Sorts charts in alphabetical order rather than"
                        " the default order", default=False, action="store_true")
    parser.add_argument('-d', '--debug', help="Sets logging level to DEBUG.",
                        action="store_const", dest="loglevel",
                        const=logging.DEBUG, default=logging.WARNING)
    parser.add_argument("-e", "--export", choices=["pdf", "svg", "webp", "jpeg", "png",
                                                   "html", "html_offline"],
                        help="Exports the graphs rather than all on one webpage")
    parser.add_argument("--no-open", help="Will only start the server and not open the browser"
                        " to view it", default=False, action="store_true")
    parser.add_argument("-o", "--output", default="metastalk_exports",
                        help="The name of the directory to output exports to. "
                             "Will be created if it does not exist. "
                             "Defaults to metastalk_exports.")
    parser.add_argument('-t', '--test', default=False, action="store_true",
                        help='Does not show the graphs at the end.')
    parser.add_argument("-v", "--verbose", help="Sets logging level to INFO",
                        action="store_const", dest="loglevel",
                        const=logging.INFO)
    args = parser.parse_args()
    log = utils.make_logger("MetaStalk", args.loglevel)
    log.info("MetaStalk starting")
    if not args.files:
        log.error("ERROR: No path was inputted.")
        raise FileNotFoundError("No path was inputted.")
    metastalk = MetaStalk()  # pragma: no cover
    metastalk.run(args)  # pragma: no cover
