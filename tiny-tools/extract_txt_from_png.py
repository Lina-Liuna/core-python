import pytesseract
from PIL import Image
import os
from pathlib import Path


def pdf2text(dir, txtfile):
    os.chdir(dir)
    paths = sorted(Path(dir).iterdir(), key=os.path.getmtime)
    for img in paths:
        basename = os.path.basename(img)
        print(basename)
        dirname = os.path.dirname(img)


        if '.png' not in basename:
            continue

        im = Image.open(img)
        text = pytesseract.image_to_string(im)
        set_pdf_text(text, txtfile)

def set_pdf_text(text, file):
    with open(file, 'a') as f:
        f.write(text)


dir = '/Users/linaliu/books/librarybooks/from_LA_Library/englishhomework/'
image_path = '/Users/linaliu/code/DVC/CS-110-5129-intro-programming/extracttxt/'
image_path = dir + '/ALongWalktoWater/'
txt_file = image_path + 'ALongWalktoWater.txt'
# Extract text from the image using Tesseract
pdf2text(image_path, txt_file)

