# PyStalk

[![GitHub](https://img.shields.io/github/license/jwhite1st/pystalk?style=flat)](https://github.com/jwhite1st/PyStalk/blob/master/LICENSE)

Master Branch  
![Gitlab pipeline status (branch)](https://img.shields.io/gitlab/pipeline/jwhite1st/pystalk/master?label=Master%20Build&style=flat) [![coverage report](https://gitlab.com/jwhite1st/pystalk/badges/master/coverage.svg)](https://gitlab.com/jwhite1st/pystalk/commits/master)  
Develop Branch  
![Gitlab pipeline status (branch)](https://img.shields.io/gitlab/pipeline/jwhite1st/pystalk/develop?label=Develop%20Build&style=flat) [![coverage report](https://gitlab.com/jwhite1st/pystalk/badges/develop/coverage.svg)](https://gitlab.com/jwhite1st/pystalk/commits/develop)

## About

PyStalk is a tool that can be used to generate graphs from the meta data of JPG and Tiff images. It currently creates graphs for gps coordinates and a pie chart for mode information.

Examples photos from [ianare/exif-samples](https://github.com/ianare/exif-samples/tree/master/jpg/gps), [exiftool](https://owl.phy.queensu.ca/~phil/exiftool/sample_images.html), [drewmpales/metadata-extractor-images](https://github.com/drewnoakes/metadata-extractor-images).

Please open issues on [GitLab](https://gitlab.com/jwhite1st/PyStalk/issues) or if you do not have a GitLab account, send me an email and I will open an issue.

All development is done on GitLab and pushed to GitHub.

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
  - ~~Timestamps~~
  - Camera information
    - focal_length
    - flash
    - etc
- Better web layout
  - Better sized graphs
  - Ability to select a photo
  - Maybe Responsiveness
- Ability to choose the graphs used
- Possible PyPi package (??)
- Possible web scrapper for images
  - Or import from a current one

## Disclaimer

This is for educational/proof of concept purposes only. What you do with this program is **your** responsibility.
