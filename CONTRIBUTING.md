# How to contribute

Thanks for reading this because I am always looking to collaborate with other people to see their ideas.

If you are looking to submit a pull request then please do so on [GitLab](https://gitlab.com/Cyb3r-Jak3/MetaStalk) because all development is done there. Any pull request that is opened on GitHub will be closed and I mirror it on GitLab.  

Please open issues on [GitLab](https://gitlab.com/Cyb3r-Jak3/MetaStalk/issues). If you do not have a GitLab account, send then please email service desk( [incoming+cyb3r-jak3-metastalk-15263483-issue-@incoming.gitlab.com](mailto:incoming+cyb3r-jak3-metastalk-15263483-issue-@incoming.gitlab.com)).

## Getting starting

I recommend checking out the project at [SourceGraph](https://sourcegraph.com/gitlab.com/Cyb3r-Jak3/metastalk) to get a good overview of the code.

To get started clone the repo and install with development tools needed.

```bash
git clone https://gitlab.com/Cyb3r-Jak3/metastalk.git

cd metastalk
# Recommended to use a virtualenv
pip install .[dev]
```

## Testing

Currently the tests at [tests](tests/) cover all the necessary items to make sure the it works. If you add a new feature then please write a test for it as well. Testing that involves [orca](https://github.com/plotly/orca) is done during the CI process using a custom [docker image](https://gitlab.com/Cyb3r-Jak3/orca-test-image) that I wrote. Tests that need orca are skipped locally if orca is not found.

To run the tests:

```bash
python -m unittest
# or
tox -e coverage
```

additionally before pushing, run:

```bash
tox -e [py36,py37,py38]
```

This will check the files with black, bandit, pylint and flake8.

## Modules

If you are looking to write a new module for a new metadata graph here is they are currently written.

- Each module is written in the [modules](MetaStalk/modules/) directory and is added to the [\_\_init__.py](MetaStalk/modules/__init__.py) in the directory.
- A list is passed to the modules called `photos` which containing dictionaries with all the metadata points for each photo.
- The module will find the key that is using and return a figure using plotly.
- A dictionary of all the plots will be passed to [web.py](utils/web.py) which will use Dash to display them.

### Example image dictionary

#### Old < 2.2.0

```python
{'Image width': '640 pixels', 'Image height': '480 pixels', 'Image orientation': 'Horizontal (normal)', 'Bits/pixel': '24', 'Pixel format': 'YCbCr', 'Creation date': '2008-10-23 14:27:07', 'Latitude': '43.46744833333333', 'Longitude': '11.885126666663888', 'Camera aperture': '2.9', 'Camera focal': '5.9', 'Camera exposure': '1/75', 'Camera model': 'COOLPIX P6000', 'Camera manufacturer': 'NIKON', 'Compression': 'JPEG (Baseline)', 'Thumbnail size': '6702 bytes', 'ISO speed rating': '64', 'EXIF version': '0220', 'Date-time original': '2008-10-22 16:28:39', 'Date-time digitized': '2008-10-22 16:28:39', 'Exposure bias': '0', 'Focal length': '24', 'Flashpix version': '0100', 'Focal length in 35mm film': '112', 'Producer': 'Nikon Transfer 1.1 W', 'Comment': 'JPEG quality: 75% (approximate)', 'MIME type': 'image/jpeg', 'Endianness': 'Big endian', 'item': 'item': ".\\ExamplePhotos\\DSCN0010.jpg"}
```

#### New 2.2.0+

```python
{'Image ImageDescription': (0x010E) ASCII=                                @ 158, 'Image Make': (0x010F) ASCII=NIKON @ 190, 'Image Model': (0x0110) ASCII=COOLPIX P6000 @ 196, 'Image Orientation': (0x0112) Short=Horizontal (normal) @ 54, 'Image XResolution': (0x011A) Ratio=300 @ 210, 'Image YResolution': (0x011B) Ratio=300 @ 218, 'Image ResolutionUnit': (0x0128) Short=Pixels/Inch @ 90, 'Image Software': (0x0131) ASCII=Nikon Transfer 1.1 W @ 226, 'Image DateTime': (0x0132) ASCII=2008:11:01 21:15:07 @ 248, 'Image YCbCrPositioning': (0x0213) Short=Centered @ 126, 'Image ExifOffset': (0x8769) Long=268 @ 138, 'GPS GPSLatitudeRef': (0x0001) ASCII=N @ 936, 'GPS GPSLatitude': (0x0002) Ratio=[43, 28, 1407/500] @ 1052, 'GPS GPSLongitudeRef': (0x0003) ASCII=E @ 960, 'GPS GPSLongitude': (0x0004) Ratio=[11, 53, 645599999/100000000] @ 1076, 'GPS GPSAltitudeRef': (0x0005) Byte=0 @ 984, 'GPS GPSTimeStamp': (0x0007) Ratio=[14, 27, 181/25] @ 1100, 'GPS GPSSatellites': (0x0008) ASCII=06 @ 1008, 'GPS GPSImgDirectionRef': (0x0010) ASCII= @ 1020, 'GPS GPSMapDatum': (0x0012) ASCII=WGS-84    @ 1124, 'GPS GPSDate': (0x001D) ASCII=2008:10:23 @ 1134, 'Image GPSInfo': (0x8825) Long=926 @ 150, 'Thumbnail Compression': (0x0103) Short=JPEG (old-style) @ 4464, 'Thumbnail XResolution': (0x011A) Ratio=72 @ 4532, 'Thumbnail YResolution': (0x011B) Ratio=72 @ 4540, 'Thumbnail ResolutionUnit': (0x0128) Short=Pixels/Inch @ 4500, 'Thumbnail JPEGInterchangeFormat': (0x0201) Long=4548 @ 4512, 'Thumbnail JPEGInterchangeFormatLength': (0x0202) Long=6702 @ 4524, 'EXIF ExposureTime': (0x829A) Ratio=1/75 @ 682, 'EXIF FNumber': (0x829D) Ratio=59/10 @ 690, 'EXIF ExposureProgram': (0x8822) Short=Program Normal @ 302, 'EXIF ISOSpeedRatings': (0x8827) Short=64 @ 314, 'EXIF ExifVersion': (0x9000) Undefined=0220 @ 326, 'EXIF DateTimeOriginal': (0x9003) ASCII=2008:10:22 16:28:39 @ 698, 'EXIF DateTimeDigitized': (0x9004) ASCII=2008:10:22 16:28:39 @ 718, 'EXIF ComponentsConfiguration': (0x9101) Undefined=YCbCr @ 362, 'EXIF ExposureBiasValue': (0x9204) Signed Ratio=0 @ 738, 'EXIF MaxApertureValue': (0x9205) Ratio=29/10 @ 746, 'EXIF MeteringMode': (0x9207) Short=Pattern @ 398, 'EXIF LightSource': (0x9208) Short=Unknown @ 410, 'EXIF Flash': (0x9209) Short=Flash did not fire, compulsory flash mode @ 422, 'EXIF FocalLength': (0x920A) Ratio=24 @ 754, 'EXIF FlashPixVersion': (0xA000) Undefined=0100 @ 470, 'EXIF ColorSpace': (0xA001) Short=sRGB @ 482, 'EXIF ExifImageWidth': (0xA002) Long=640 @ 494, 'EXIF ExifImageLength': (0xA003) Long=480 @ 506, 'Interoperability InteroperabilityIndex': (0x0001) ASCII=R98 @ 906, 'Interoperability InteroperabilityVersion': (0x0002) Undefined=[48, 49, 48, 48] @ 918, 'EXIF InteroperabilityOffset': (0xA005) Long=896 @ 518, 'EXIF FileSource': (0xA300) Undefined=Digital Camera @ 530, 'EXIF SceneType': (0xA301) Undefined=Directly Photographed @ 542, 'EXIF CustomRendered': (0xA401) Short=Normal @ 554, 'EXIF ExposureMode': (0xA402) Short=Auto Exposure @ 566, 'EXIF WhiteBalance': (0xA403) Short=Auto @ 578, 'EXIF DigitalZoomRatio': (0xA404) Ratio=0 @ 888, 'EXIF FocalLengthIn35mmFilm': (0xA405) Short=112 @ 602, 'EXIF SceneCaptureType': (0xA406) Short=Standard @ 614, 'EXIF GainControl': (0xA407) Short=None @ 626, 'EXIF Contrast': (0xA408) Short=Normal @ 638, 'EXIF Saturation': (0xA409) Short=Normal @ 650, 'EXIF Sharpness': (0xA40A) Short=Normal @ 662, 'EXIF SubjectDistanceRange': (0xA40C) Short=0 @ 674, 'item': ".\\ExamplePhotos\\DSCN0010.jpg"}
```
