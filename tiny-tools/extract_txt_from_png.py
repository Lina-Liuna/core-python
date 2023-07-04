import pytesseract
from PIL import Image

# Open the image file
image_path = 'pdf_files/67.png'
image = Image.open(image_path)

# Extract text from the image using Tesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)