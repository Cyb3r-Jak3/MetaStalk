# pylint: disable=invalid-name, missing-module-docstring, missing-function-docstring,
import argparse
import os
import logging
from exif import Image
import plotly.express as px


log = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('files', nargs='*', default=None,
                    help='Directory of photos to check')
args = parser.parse_args()

for path in args.files:
    isdir = os.path.isdir(path)


def dms2dd(degrees, minutes, seconds):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    return dd


photos = []
if isdir:
    for file in os.listdir(args.files[0]):
        photos.append(os.path.join(args.files[0], file))
else:
    for item in args.files:
        photos.append(args.files[0])

lats = []
longs = []
gps_photos = []

for each in photos:
    with open(each, 'rb') as image_file:
        my_image = Image(image_file)
        if my_image.has_exif:
            gps_photos.append(each)
            lats.append(dms2dd(*my_image.gps_latitude))
            longs.append(dms2dd(*my_image.gps_longitude))
            log.debug("{} has exif gps data".format(each))
        else:
            log.info("{} has no exif data ".format(each))

points = []
for x in range(len(lats)):
    points.append((lats[x], longs[x]))


fig = px.scatter_mapbox(lon=longs, lat=lats, hover_name=gps_photos)
fig.update_layout(mapbox_style="open-street-map", title="Geo Locations",)
fig.show()
