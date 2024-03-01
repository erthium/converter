"""
This script is used to convert an image file to a PDF file.
"""

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

page_size = A4
#page_ratio = page_size[0] / page_size[1]

def draw_to_canvas(canvas: canvas.Canvas, image_path: str, x: int, y: int, width: int, height: int) -> None:
    """
    Draws an image on the PDF canvas.\n
    Intended to be used in function 'images_to_pdf'. Do not use it directly.
    """
    image = Image.open(image_path)
    #image.thumbnail((width, height))

    # Calculate the position to center the image within the puzzle space
    x_offset = (width - image.width) / 2
    y_offset = (height - image.height) / 2

    # Draw the image on the PDF canvas
    # Let's not use drawInlineImage, as it doesn't support transparency
    canvas.drawImage(image_path, x + x_offset, y + y_offset, image.width, image.height)


def images_to_pdf(output_filename: str, image_paths: list[str], columns: int = 1) -> None:
    pdf = canvas.Canvas(output_filename, pagesize=page_size)
    rows = len(image_paths) // columns
    offset = (20, 100)
    single_width = (page_size[0] - ((columns + 1) * offset[0])) / columns
    single_height = (page_size[1] - ((rows + 1) * offset[1])) / rows

    for i, image_path in enumerate(image_paths):
        row = i // columns
        col = i % columns

        x = col * single_width + (col + 1) * offset[0]
        y = page_size[1] - (row + 1) * single_height - (row + 1) * offset[1]

        draw_to_canvas(pdf, image_path, x, y, single_width, single_height)

        """ Currently now necessary
        if i % (rows * columns) == (rows * columns) - 1:
            pdf.showPage()  # Start a new page
        """
    pdf.save()


def image_to_pdf(output_filename: str, image_path: str, fit_page: bool = True, 
                 page_offset: tuple[int, int] = (20, 100)) -> None:
    """
    Creates a PDF from an image file.\n
    If 'fit_page' is True, the image will be resized to fit the page.
    """
    pdf: canvas.Canvas = canvas.Canvas(output_filename, pagesize=page_size)
    image: Image.Image = Image.open(image_path)
    if fit_page:
        new_width: int = page_size[0] - 2 * page_offset[0]
        new_height: int = page_size[1] - 2 * page_offset[1]
        image.thumbnail((new_width, new_height))
    x_offset: int = (page_size[0] - image.width) / 2
    y_offset: int = (page_size[1] - image.height) / 2
    # Let's not use drawInlineImage, as it doesn't support transparency
    pdf.drawImage(image_path, x_offset, y_offset, image.width, image.height)
    print(f"Image size: {image.size}")
    pdf.save()
