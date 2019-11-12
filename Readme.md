# PyStalk

![Gitlab pipeline status (branch)](https://img.shields.io/gitlab/pipeline/jwhite1st/pystalk/master?label=Master%20Build&style=flat-plastic) ![Gitlab pipeline status (branch)](https://img.shields.io/gitlab/pipeline/jwhite1st/pystalk/develop?label=Develop%20Build&style=flat-plastic)
[![GitHub](https://img.shields.io/github/license/jwhite1st/pystalk?style=plastic)](https://github.com/jwhite1st/PyStalk/blob/master/LICENSE)

[![coverage report](https://gitlab.com/jwhite1st/pystalk/badges/develop/coverage.svg)](https://gitlab.com/jwhite1st/pystalk/commits/develop)

## About

PyStalk is a tool that can be used to generate graphs from the meta data of images. It currently creates graphs for gps coordinates and a pie chart for mode information.

Examples photos from [here](https://github.com/ianare/exif-samples/tree/master/jpg/gps)

Please open issues on [Github](https://github.com/jwhite1st/PyStalk/issues)

## How to use

```bash
git clone https://github.com/jwhite1st/pystalk
cd pystalk
pip install -r requirements
python PyStalk.py <Path to files>
#i.e. python PyStalk.py tests/ExamplePhotos/
```

## TODO

- New Graphs
  - Timestamps
  - Camera information
    - focal_length
    - flash
    - etc
- Better web layout
  - Better sized graphs
  - Ability to select a photo
  - Maybe Responsiveness
- Possible PyPi package (??)
- Possible web scrapper for images
  - Or import for a current one

## Disclaimer

This is for educational/proof of concept purposes only. What you do with this program is **your** responsibility.
