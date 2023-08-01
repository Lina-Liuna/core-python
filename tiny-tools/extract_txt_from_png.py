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

image_path = '/Users/linaliu/code/core-python/tiny-tools/pdf_files/how_to_talk_to_anyone/'

txt_file = '/Users/linaliu/code/core-python/tiny-tools/pdf_files/talkanyone.txt'
# Extract text from the image using Tesseract
pdf2text(image_path, txt_file)

