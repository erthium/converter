import markdown2
import pdfkit

def markdown_to_pdf(markdown_file, output_pdf):
    # Read Markdown file
    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown2.markdown(markdown_content)

    # Generate PDF from HTML
    pdfkit.from_string(html_content, output_pdf)


markdown_file = 'test_assets/tech.md'
pdf_file = 'output.pdf'
markdown_to_pdf(markdown_file, pdf_file)
