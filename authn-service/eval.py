"""Example of exposure analysis (function call detection) with pillow.
View CVE-2022-22817 in this repository's Dependabot Alerts.
"""
from PIL import ImageMath, Image
import glob, os

def image_transform():
    size = 128, 128

    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
         with Image.open(infile) as im:
            im.thumbnail(size)
            im.save(file + ".thumbnail", "JPEG")
            ImageMath.eval("convert(image, shred)", image = real_banksy)
