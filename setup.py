"""Sets up PyStalk to be installed"""
import os
from setuptools import setup, find_packages
from MetaStalk import __version__


def read(fname):
    """Reads README.md as long description"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="MetaStalk",
    version=__version__,
    author="Cyb3r Jak3",
    author_email="jake@jwhite.network",
    install_requires=[
        "hachoir >= 3.1.1",
        "plotly >= 4.6.0",
        "pandas >= 1.0.3",
        "dash >= 1.11.0"],
    description="Metadata analyzer",
    license="MPL 2.0",
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 1 - Planning"
    ],
    packages=find_packages(),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    entry_points={
        "console_scripts": ["metastalk=MetaStalk.main:start"]
    },
    url="https://gitlab.com/Cyb3r-Jak3/MetaStalk",
    project_urls={
        "Issues": "https://gitlab.com/Cyb3r-Jak3/MetaStalk/issues",
        "Source": "https://gitlab.com/Cyb3r-Jak3/MetaStalk/-/tree/master",
        "CI": "https://gitlab.com/Cyb3r-Jak3/MetaStalk/pipelines"
    },

)
