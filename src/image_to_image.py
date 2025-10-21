"""
This script is used to convert an image file to another image file.\n
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


def save_heic_to_png(image_path: str, output_path: str = "", quality: int = 100) -> None:
    from heic2png import HEIC2PNG
    heic_img = HEIC2PNG(image_path, quality=quality)  # Specify the quality of the converted image
    if not output_path:
        output_path = ".".join(image_path.split(".")[0: -1]) + ".png"
    heic_img.save(output_path)  # The converted image will be saved as `test.png`            
    

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


def main():
    import os
    import argparse
    parser = argparse.ArgumentParser(description="Convert an image file to another image file.")
    parser.add_argument("image_path", help="Path to the image file to convert.")
    parser.add_argument("out", help="Path to the output image file.")
    parser.add_argument("--jpg-to-png", action="store_true", help="Convert JPG to PNG.")
    parser.add_argument("--png-to-jpg", action="store_true", help="Convert PNG to JPG.")
    parser.add_argument("--resize", nargs=2, type=int, metavar=('width', 'height'), help="Resize the image to the given width and height.")
    parser.add_argument("--resize-by-ratio", type=float, help="Resize the image by the given ratio.")
    parser.add_argument("--reduce-size", type=int, metavar='max_MB', help="Reduce the image size below the given maximum size in mega bytes.")
    if not os.path.exists(parser.parse_args().image_path):
        raise FileNotFoundError(f"Image file {parser.parse_args().image_path} not found.")
    args = parser.parse_args()
    image = Image.open(args.image_path)
    if args.jpg_to_png:
        image = jpg_to_png(image)
    if args.png_to_jpg:
        image = png_to_jpg(image)
    if args.resize:
        new_size = (args.resize[0], args.resize[1])
        image = resize(image, new_size)
    if args.resize_by_ratio:
        image = resize_by_ratio(image, args.resize_by_ratio)
    if args.reduce_size:
        reduce_size(args.image_path, args.reduce_size, args.out)
    image.save(args.out)
    print(f"Image saved to {args.out}")
    image.close()

if __name__ == "__main__":
    main()
