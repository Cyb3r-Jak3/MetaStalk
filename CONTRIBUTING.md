# How to contribute

Thanks for reading this because I am always looking to collaborate with other people to see their ideas.

If you are looking to submit a pull request then please do so on [GitLab](https://gitlab.com/Cyb3r-Jak3/pystalk) because all development is done there. Any pull request that is opened on GitHub will be closed and I mirror it on GitLab.

## Modules

If you are looking to write a new module for a new metadata graph here is they are currently written.

- Each module is written in the [modules](modules/) directory and is added to the [\_\_init__.py](modules/__init__.py) in the directory.
- A list is passed to the modules called `photos` which containing dictionaries with all the metadata points for each photo.
- The module will find the key that is using and return a figure using plotly.
- A dictionary of all the plots will be passed to [web.py](utils/web.py) which will use dash to display them.

### Example dictionary

```python
{'Image width': '1600 pixels', 'Image height': '1200 pixels', 'Image orientation': 'Horizontal (normal)', 'Bits/pixel': '24', 'Pixel format': 'YCbCr', 'Creation date': '2007-11-29 16:16:21', 'Camera aperture': '2.97', 'Camera focal': '2.8', 'Camera exposure': '1/6', 'Camera model': 'Canon PowerShot SD300', 'Camera manufacturer': 'Canon', 'Compression': 'JPEG (Baseline)', 'Thumbnail size': '5922 bytes', 'EXIF version': '0220', 'Date-time original': '2007-11-29 16:16:21', 'Date-time digitized': '2007-11-29 16:16:21', 'Compressed bits per pixel': '3', 'Shutter speed': '2.59', 'Aperture': '2.97', 'Exposure bias': '0', 'Focal length': '5.8', 'Flashpix version': '0100', 'Focal plane width': '7.14e+03', 'Focal plane height': '7.14e+03', 'Comment': 'JPEG quality: 90% (approximate)', 'MIME type': 'image/jpeg', 'Endianness': 'Big endian', 'item': '.\\utils\\ExamplePhotos\\22-canon_tags.jpg'}
```
