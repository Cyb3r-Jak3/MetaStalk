# -*- coding: utf-8 -*-
"""Main function of MetaStalk.
Run get any metadata from photos
and creates graphs from the metadata using MetaStalk.Modules"""
import argparse
from collections import OrderedDict
import os
import logging
import timeit
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from hachoir.core import config as hachoirconfig
import MetaStalk.utils as utils
import MetaStalk.modules as modules

hachoirconfig.quiet = True


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
        for path in args.files:
            if os.path.isdir(path):
                self.log.debug("Detected path as a directory")
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    self.file_search(item_path)
            else:
                self.file_search(path)

        self.plots = {
            "Stats": modules.stats(self.valid, self.invalid),
            "GPS": modules.gps_check(self.valid),
            "Timestamp": modules.date_time(self.valid),
            "Model": modules.pie_chart(self.valid, "Camera model"),
            "Manufacturer": modules.pie_chart(self.valid, "Camera manufacturer"),
            "Focal": modules.pie_chart(self.valid, "Camera focal"),
            "Producer": modules.pie_chart(self.valid, "Producer")
        }
        if args.alphabetic:
            self.plots = OrderedDict(sorted(self.plots.items()))
        if args.export:
            utils.export(args.export, args.output, self.plots)
        utils.graph(self.plots, self.t_start, args.test, args.no_open)

    def file_search(self, parse_file: str):
        """file_search

        Used to append files if the path is not a directory.

        Arguments
            files {str} -- Name of the file to parse.
        """
        parser = createParser(parse_file)
        try:
            metadata = extractMetadata(parser).exportDictionary()["Metadata"]
            metadata["item"] = parse_file
            self.valid.append(metadata)
            self.log.debug("%s has metadata", parse_file)
        except AttributeError:
            self.invalid.append(parse_file)
            self.log.debug("%s has no metadata data", parse_file)


def start():
    """
    Function needed to start MetaStalk
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
    parser.add_argument("-e", "--export", choices=["pdf", "svg", "png", "html"],
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
    metastalk = MetaStalk()
    metastalk.run(args)
