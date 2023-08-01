from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def write_image_to_pdf(image_path, output_path, x, y, width, height):
    # Create a PDF canvas with the same dimensions as the image
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setPageSize((letter[0], letter[1]))

    # Draw the image on the canvas
    c.drawImage(image_path, x, y, width, height)

    # Save the canvas to the PDF file
    c.save()
# Provide the path to the image, the PDF file, and the desired output path
image_path = '/Users/linaliu/code/Arch_Concept/gallery/Concurrency.png'
output_path = '/Users/linaliu/code/Booklist/gallery/test.pdf'
x = 100  # X-coordinate of the top-left corner of the image
y = 200  # Y-coordinate of the top-left corner of the image
width = 300  # Width of the image
height = 200  # Height of the image

# Call the function to add the image to the PDF
write_image_to_pdf(image_path,  output_path, x, y, width, height)