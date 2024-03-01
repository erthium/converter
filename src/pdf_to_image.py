"""
This script is used to convert a PDF file to an image file.\n
It includes the following functions:
- pdf_to_image
"""

from pdf2image import convert_from_path
from PIL.Image import Image
import os


def pdf_to_image(pdf_path: str, output_dir: str, dpi: int = 200) -> None:
    filename = os.path.basename(pdf_path)
    images: list[Image] = convert_from_path(pdf_path, dpi=dpi)
    for i, image in enumerate(images):
        page_path = os.path.join(output_dir, f"{filename}_page_{i}.png")
        image.save(page_path, "PNG")
