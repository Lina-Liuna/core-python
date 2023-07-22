from reportlab.pdfgen import canvas

def create_blank_pdf(output_pdf_path):
    """
    Function to create a PDF with a white blank page.
    """
    c = canvas.Canvas(output_pdf_path)

    # Set the page size (A4 by default)
    c.setPageSize((595.27, 841.89))

    # Draw a white rectangle covering the entire page
    c.setFillColorRGB(1, 1, 1)  # White color (RGB: 1, 1, 1)
    c.rect(0, 0, 595.27, 841.89, fill=True, stroke=False)

    # Save the canvas as a PDF
    c.save()

if __name__ == "__main__":
    # Path to the output PDF (the PDF with a white blank page)
    output_pdf_path = "blank_pdf.pdf"

    # Create a PDF with a white blank page
    create_blank_pdf(output_pdf_path)