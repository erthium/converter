"""
This script is used to convert an image file to another image file.
It includes the following functions:
- resize
- resize_by_ratio
- jpg_to_png
- png_to_jpg
- reduce_size
"""

from PIL import Image
import os

def resize(image: Image.Image, new_size: tuple[int, int], contain_ratio = True) -> Image.Image:
    if contain_ratio:
        image.thumbnail(new_size)
    else:
        image = image.resize(new_size)
    return image


def resize_by_ratio(image: Image.Image, ratio: float) -> Image.Image:
    width, height = image.size
    new_width = int(width * ratio)
    new_height = int(height * ratio)
    return image.resize((new_width, new_height))


def jpg_to_png(image: Image.Image) -> Image.Image:
    return image.convert("RGBA")


def png_to_jpg(image: Image.Image) -> Image.Image:
    return image.convert("RGB")
    

def reduce_size(image_path: str, max_MB: int, output_path: str) -> Image.Image:
    """
    Gets an image and maximum size and reduce its size
    below the given maximum size in mega bytes.
    """
    size_in_MB = os.stat(image_path).st_size / (1024 * 1024)
    ratio = size_in_MB / max_MB
    quality = int(100 / ratio)
    image = Image.open(image_path)
    image.save(output_path, quality=quality)
