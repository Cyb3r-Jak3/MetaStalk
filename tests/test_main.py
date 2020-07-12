"""Tests for MetaStalk.
"""
import unittest
from argparse import Namespace
import os
from distutils.spawn import find_executable

from MetaStalk import main


def check_orca() -> bool:
    """checks to see if orca is available

    Returns:
        bool: If orca executable is found
    """
    return find_executable("orca") is not None


class MetaStalkTests(unittest.TestCase):
    """MetStalkTests.

    Test Suite for MetaStalk

    """
    def __init__(self, *args, **kwargs):
        super(MetaStalkTests, self).__init__(*args, **kwargs)
        self.filenames = ["Focal", "GPS", "Manufacturer", "Model", "Producer", "Stats", "Timestamp"]

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
            loglevel=30,
            test=True,
            export_only=False,
            no_open=True,
            export=None)
        metastalk = main.MetaStalk()
        self.assertEqual(metastalk.run(arguments), None)

    def test_files(self):
        """Results for files."""
        arguments = Namespace(
            files=['./ExamplePhotos/22-canon_tags.jpg', './ExamplePhotos/32-lens_data.jpeg'],
            alphabetic=True,
            no_open=True,
            export_only=False,
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
            export_only=False,
            test=True,
            export="html",
            output="metastalk_exports")
        metastalk = main.MetaStalk()
        metastalk.run(arguments)
        test_passed = True
        for required_file in self.filenames:
            if not os.path.isfile(f"metastalk_exports/{required_file}.html"):
                print(f"missing file {required_file}")
                test_passed = False
        self.assertTrue(test_passed)

    def test_html_size(self):
        """Test to see html that the offline html files are bigger"""
        arguments = Namespace(
            files=['./ExamplePhotos/22-canon_tags.jpg', './ExamplePhotos/32-lens_data.jpeg'],
            loglevel=20,
            alphabetic=False,
            no_open=True,
            export_only=False,
            test=True,
            export="html_offline",
            output="metastalk_exports_offline")
        metastalk = main.MetaStalk()
        metastalk.run(arguments)
        test_passed = True
        for required_file in self.filenames:
            file_size_normal = os.stat(f"metastalk_exports/{required_file}.html").st_size
            file_size_offline = os.stat(f"metastalk_exports_offline/{required_file}.html").st_size
            if file_size_normal > file_size_offline:
                print(f"Wrong File Size for: {required_file}")
                test_passed = False
        self.assertTrue(test_passed)

    @unittest.skipUnless(check_orca(), "Test not needed if orca executable is missing")
    def test_orca_export(self):
        """Test for export fail."""
        test_passed = True
        arguments = Namespace(
            files=['./ExamplePhotos/'],
            loglevel=30,
            test=True,
            alphabetic=False,
            export_only=False,
            no_open=True,
            export="pdf",
            output="metastalk_exports")
        metastalk = main.MetaStalk()
        metastalk.run(arguments)
        for required_file in self.filenames:
            if not os.path.isfile(f"metastalk_exports/{required_file}.pdf"):
                print(f"missing file {required_file}")
                test_passed = False
        self.assertTrue(test_passed)

    @unittest.skipUnless(check_orca(), "Test not needed if orca executable is missing")
    def test_export_only(self):
        """Test to show that only export option works"""
        arguments = Namespace(
            files=['./ExamplePhotos/32-lens_data.jpeg'],
            loglevel=30,
            alphabetic=False,
            no_open=True,
            export_only=True,
            test=True,
            export="png",
            output="metastalk_exports")
        metastalk = main.MetaStalk()
        metastalk.run(arguments)
        test_passed = True
        for required_file in self.filenames:
            if not os.path.isfile(f"metastalk_exports/{required_file}.png"):
                print(f"missing file {required_file}")
                test_passed = False
        self.assertTrue(test_passed)
