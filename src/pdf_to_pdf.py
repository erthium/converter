"""
This script is used to make conversions between PDF files.\n
It includes the following functions:
- clip_pdf
- merge_pdfs
- clip_selections
"""

from PyPDF2 import PdfReader, PdfWriter

def clip_pdf(pdf_path: str, output_path: str, start: int, end: int) -> None:
    """
    Clip a PDF file from start to end and save it to the output path.
    """
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for index in range(start, end):
        writer.add_page(reader.pages[index])
    writer.write(output_path)


def merge_pdfs(pdf_paths: list[str], output_path: str) -> None:
    """
    Merge multiple PDF files into a single PDF file.\n
    The order of the files is the same as the order in the list.    
    """
    writer = PdfWriter()
    for pdf_path in pdf_paths:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)
    writer.write(output_path)


def clip_selections(pdf_path: str, output_path: str, selections: list[int]) -> None:
    """
    Clip a PDF file from the given selections and save it to the output path.\n
    The selections are the indexes of the pages to be selected.\n
    The first page has an index of 0.
    """
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for index in selections:
        writer.add_page(reader.pages[index])
    writer.write(output_path)

if __name__ == "__main__":
    # get two PDF files and merge them
    # usage: python pdf_to_pdf.py file1.pdf file2.pdf out.pdf
    import argparse
    parser = argparse.ArgumentParser(description="Merge PDF files.")
    parser.add_argument("pdf_paths", nargs="+", help="Paths to the PDF files to merge.")
    parser.add_argument("out", help="Path to the output PDF file.")
    args = parser.parse_args()
    merge_pdfs(args.pdf_paths, args.out)
