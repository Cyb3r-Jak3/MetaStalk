"""Test suite for MetaStalk
Currently unused but planned.
"""
import pytest
import MetaStalk


def empty_directory_test():
    """Shows result for empty directory"""
    with pytest.raises(FileNotFoundError):
        MetaStalk.run()
