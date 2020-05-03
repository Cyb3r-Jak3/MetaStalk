# MetaStalk

[![GitHub](https://img.shields.io/github/license/Cyb3r-Jak3/pystalk?style=flat)](https://github.com/Cyb3r-Jak3/PyStalk/blob/master/LICENSE) ![Gitlab pipeline status (branch)](https://img.shields.io/gitlab/pipeline/Cyb3r-Jak3/metastalk/master?label=Build&style=flat)  

[![Test Coverage](https://api.codeclimate.com/v1/badges/896b338971314c13a56e/test_coverage)](https://codeclimate.com/github/Cyb3r-Jak3/PyStalk/test_coverage) [![Maintainability](https://api.codeclimate.com/v1/badges/896b338971314c13a56e/maintainability)](https://codeclimate.com/github/Cyb3r-Jak3/PyStalk/maintainability)  
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Cyb3r-Jak3/PyStalk/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Cyb3r-Jak3/PyStalk/?branch=master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Cyb3r-Jak3/PyStalk.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Cyb3r-Jak3/PyStalk/context:python)

## About

PyStalk is a tool that can be used to generate graphs from the metadata of JPEG, TIFF images. More formats are supported but untested.
It currently creates graphs for:

- GPS coordinates (map)
- Focal Length, Camera model, Camera manufacturer, Producer information (Pie Chart)
- Timestamp information (Chart)

Examples photos from [ianare/exif-samples](https://github.com/ianare/exif-samples/tree/master/jpg/gps), [exiftool](https://owl.phy.queensu.ca/~phil/exiftool/sample_images.html), [drewmpales/metadata-extractor-images](https://github.com/drewnoakes/metadata-extractor-images).

All development is done on GitLab and pushed to GitHub. Please read [contributing.md](CONTRIBUTING.md) for development.

Python 3.6 and up.

## How to use

```bash
git clone https://gitlab.com/Cyb3r-Jak3/metastalk
cd metastalk
pip install -r requirements.txt
python ./MetaStalk/main.py <Path to files>
#i.e. python ./MetaStalk/main.py ./ExamplePhotos/
```

This project also use Pipfile and Pipfile.lock if you would rather pipenv over requirements.txt

## Disclaimer

This is for educational/proof of concept purposes only. What you do with this program is **your** responsibility.

[![DeepSource](https://static.deepsource.io/deepsource-badge-light.svg)](https://deepsource.io/gl/Cyb3r-Jak3/PyStalk/?ref=repository-badge)
