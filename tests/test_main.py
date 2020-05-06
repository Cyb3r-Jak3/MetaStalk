"""Tests for MetaStalk.
"""
import unittest
from argparse import Namespace
import os

from MetaStalk import main


class MetaStalkTests(unittest.TestCase):
    """MetStalkTests.

    Test Suite for MetaStalk

    """

    def test_empty_path(self):
        """Shows result for no path input."""
        with self.assertRaises(FileNotFoundError):
            main.start()

    def test_directory(self):
        """Results for a directory.
        """
        arguments = Namespace(
            files=['./ExamplePhotos/'],
            alphabetic=False,
            loglevel=30, test=True, no_open=True,
            export=None)
        metastalk = main.MetaStalk()
        self.assertEqual(metastalk.run(arguments), None)

    def test_files(self):
        """Results for files."""
        arguments = Namespace(
            files=['./ExamplePhotos/22-canon_tags.jpg', './ExamplePhotos/32-lens_data.jpeg'],
            alphabetic=True,
            no_open=True,
            loglevel=30,
            test=True,
            export=None)
        metastalk = main.MetaStalk()
        self.assertEqual(metastalk.run(arguments), None)

    def test_html_export(self):
        """Test to see html files got exported."""
        arguments = Namespace(
            files=['./ExamplePhotos/22-canon_tags.jpg', './ExamplePhotos/32-lens_data.jpeg'],
            loglevel=30,
            alphabetic=False,
            no_open=True,
            test=True,
            export="html",
            output="metastalk_exports")
        metastalk = main.MetaStalk()
        metastalk.run(arguments)
        test_passed = True
        filenames = ["Focal", "GPS", "Manufacturer", "Model", "Producer", "Stats", "Timestamp"]
        for required_file in filenames:
            if not os.path.isfile(f"metastalk_exports/{required_file}.html"):
                print(f"missing file {required_file}")
                test_passed = False
        self.assertTrue(test_passed)

    def test_failed_export(self):
        """Test for export fail."""
        arguments = Namespace(
            files=['./ExamplePhotos/'], loglevel=30, test=True,
            alphabetic=False,
            no_open=True,
            export="pdf",
            output="metastalk_exports")
        metastalk = main.MetaStalk()
        with self.assertRaises(EnvironmentError):
            metastalk.run(arguments)
