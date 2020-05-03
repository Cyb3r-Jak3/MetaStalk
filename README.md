# MetaStalk

[![GitHub](https://img.shields.io/github/license/Cyb3r-Jak3/MetaStalk?style=flat)](https://github.com/Cyb3r-Jak3/MetaStalk/blob/master/LICENSE) ![Gitlab pipeline status (branch)](https://img.shields.io/gitlab/pipeline/Cyb3r-Jak3/MetaStalk/master?label=Build&style=flat)  

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/metastalk) ![PyPI](https://img.shields.io/pypi/v/metastalk)

[![Maintainability](https://api.codeclimate.com/v1/badges/9b95ea5f0c8a77eab0ed/maintainability)](https://codeclimate.com/github/Cyb3r-Jak3/MetaStalk/maintainability) ![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/metastalk)  
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Cyb3r-Jak3/MetaStalk/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Cyb3r-Jak3/MetaStalk/?branch=master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Cyb3r-Jak3/MetaStalk.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Cyb3r-Jak3/MetaStalk/context:python)

## About

MetaStalk is a tool that can be used to generate graphs from the metadata of JPEG, TIFF images. More formats are supported but untested.
It currently creates graphs for:

- GPS coordinates (map)
- Focal Length, Camera model, Camera manufacturer, Producer information (Pie Chart)
- Timestamp information (Chart)

Examples photos from [ianare/exif-samples](https://github.com/ianare/exif-samples/tree/master/jpg/gps), [exiftool](https://owl.phy.queensu.ca/~phil/exiftool/sample_images.html), [drewmpales/metadata-extractor-images](https://github.com/drewnoakes/metadata-extractor-images).

All development is done on GitLab and pushed to GitHub. Please read [contributing.md](CONTRIBUTING.md) for development.

Python 3.6 and up.

## How to use

MetaStalk is available as a package on pypi.org or you can do a source install.

### PyPi Install

```bash
pip install metastalk
metastalk <Path to files>
#i.e. metastalk ./ExamplePhotos/
```

### Source Install

```bash
git clone https://gitlab.com/Cyb3r-Jak3/metastalk
cd metastalk
setup.py install
metastalk <Path to files>
#i.e. metastalk ./ExamplePhotos/
```

This project also use Pipfile and Pipfile.lock if you would rather pipenv over requirements.txt

## Disclaimer

This is for educational/proof of concept purposes only. What you do with this program is **your** responsibility.

[![DeepSource](https://static.deepsource.io/deepsource-badge-light.svg)](https://deepsource.io/gl/Cyb3r-Jak3/PyStalk/?ref=repository-badge)
