"""Test suite for PyStalk"""
import pytest
import PyStalk


def empty_directory_test():
    """Shows result for empty directory"""
    with pytest.raises(FileNotFoundError):
        PyStalk.run()
