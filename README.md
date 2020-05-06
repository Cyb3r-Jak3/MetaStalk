# MetaStalk

[![GitHub](https://img.shields.io/github/license/Cyb3r-Jak3/MetaStalk?style=flat)](https://github.com/Cyb3r-Jak3/MetaStalk/blob/master/LICENSE) ![Gitlab pipeline status (branch)](https://img.shields.io/gitlab/pipeline/Cyb3r-Jak3/MetaStalk/master?label=Build&style=flat)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/metastalk) ![PyPI](https://img.shields.io/pypi/v/metastalk)

[![Maintainability](https://api.codeclimate.com/v1/badges/9b95ea5f0c8a77eab0ed/maintainability)](https://codeclimate.com/github/Cyb3r-Jak3/MetaStalk/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/9b95ea5f0c8a77eab0ed/test_coverage)](https://codeclimate.com/github/Cyb3r-Jak3/MetaStalk/test_coverage)

[![codecov](https://codecov.io/gl/Cyb3r-Jak3/metastalk/branch/master/graph/badge.svg)](https://codecov.io/gl/Cyb3r-Jak3/metastalk) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/d3ed4a583afc4d27bbca4c8eb4b51e78)](https://www.codacy.com/manual/Cyb3r_Jak3/metastalk?utm_source=gitlab.com&amp;utm_medium=referral&amp;utm_content=Cyb3r-Jak3/metastalk&amp;utm_campaign=Badge_Grade)

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Cyb3r-Jak3/MetaStalk/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Cyb3r-Jak3/MetaStalk/?branch=master) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Cyb3r-Jak3/MetaStalk.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Cyb3r-Jak3/MetaStalk/context:python)

## About

MetaStalk is a tool that can be used to generate graphs from the metadata of JPEG, TIFF images. More formats are supported but untested.
It currently creates graphs for:

- GPS coordinates (map)
- Focal Length, Camera model, Camera manufacturer, Producer information (Pie Chart)
- Timestamp information (Chart)

Examples photos from [ianare/exif-samples](https://github.com/ianare/exif-samples/tree/master/jpg/gps), [exiftool](https://owl.phy.queensu.ca/~phil/exiftool/sample_images.html), [drewmpales/metadata-extractor-images](https://github.com/drewnoakes/metadata-extractor-images).

All development is done on GitLab and mirrored to GitHub. Please read [contributing.md](CONTRIBUTING.md) for development.

Python 3.6 and up.

## How to use

MetaStalk is available as a package on pypi.org or you can do a source install.

```bash
usage: MetaStalk [-h] [-a] [-d] [-e {pdf,svg,png,html}] [--no-open]
                 [-o OUTPUT] [-t] [-v]
                 [files [files ...]]

Tool to graph image metadata.

positional arguments:
  files                 Path of photos to check.

optional arguments:
  -h, --help            show this help message and exit
  -a, --alphabetic      Sorts charts in alphabetical order rather than the
                        default order
  -d, --debug           Sets logging level to DEBUG.
  -e {pdf,svg,png,html}, --export {pdf,svg,png,html}
                        Exports the graphs rather than all on one webpage
  --no-open             Will only start the server and not open the browser to
                        view it
  -o OUTPUT, --output OUTPUT
                        The name of the directory to output exports to. Will
                        be created if it does not exist. Defaults to
                        metastalk_exports.
  -t, --test            Does not show the graphs at the end.
  -v, --verbose         Sets logging level to INFO
```

If you want to have the export image option then you need to have [orca](https://github.com/plotly/orca) installed and install metastalk with `pip install metastalk[image]`.

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

## Disclaimer

This is for educational/proof of concept purposes only. What you do with this program is **your** responsibility.

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gl/Cyb3r-Jak3/MetaStalk/?ref=repository-badge)
