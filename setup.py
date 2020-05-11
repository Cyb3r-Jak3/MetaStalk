"""Sets up PyStalk to be installed"""
import os
from setuptools import setup, find_packages
from MetaStalk import __version__, __author__


def read(fname) -> str:
    """Reads the fname file.
    Used to read the README.MD file"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="MetaStalk",
    version=__version__,
    author=__author__,
    author_email="jake@jwhite.network",
    install_requires=[
        "exifreader >= 0.1.1",
        "plotly >= 4.6.0",
        "pandas >= 1.0.3",
        "dash >= 1.11.0"],
    description="Metadata analyzer and visualizer",
    license="MPL 2.0",
    python_requires=">=3.6",
    packages=find_packages(exclude=["tests"]),
    package_data={
        'MetaStalk': ['utils/assets/*'],
        },
    include_package_data=True,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    entry_points={
        "console_scripts": ["metastalk=MetaStalk.main:start"]
    },
    keywords="exif image metadata photo plotly dash pyheif",
    url="https://gitlab.com/Cyb3r-Jak3/MetaStalk",
    project_urls={
        "Issues": "https://gitlab.com/Cyb3r-Jak3/MetaStalk/issues",
        "Source": "https://gitlab.com/Cyb3r-Jak3/MetaStalk/-/tree/master",
        "CI": "https://gitlab.com/Cyb3r-Jak3/MetaStalk/pipelines",
        "Releases": "https://github.com/Cyb3r-Jak3/MetaStalk/releases"
    },
    classifiers=[
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Utilities"
    ]
)
