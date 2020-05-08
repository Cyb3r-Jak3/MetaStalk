"""heic_parse
---

Deals with heic and heif exif
"""
import io
import exifread

try:
    import pyheif
    heic_enabled = True
except ImportError:
    heic_enabled = False


def check_heic():
    """check_heic
    ---

    Returns:
        [bool] -- Whether or not pyheif was imported
    """
    return heic_enabled


def parse_heic(item: str) -> dict:
    """parse_heic
    ---
    The parses heic files
    """
    heif_file = pyheif.read_heif(item)
    if not heif_file.metadata:
        return {}
    for metadata in heif_file.metadata:

        if metadata['type'] == 'Exif':
            fstream = io.BytesIO(metadata['data'][6:])

            return exifread.process_file(fstream)
        return {}
