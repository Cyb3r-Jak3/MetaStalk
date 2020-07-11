"""Script to check for available MetaStalk updates"""

from distutils.version import LooseVersion
import requests


def check_update(current_version: str) -> bool:
    """Check version against pypi.org information"""
    latest = LooseVersion(
        requests.get("https://pypi.org/pypi/MetaStalk/json").json()["info"]["version"]
    )
    return latest > current_version
