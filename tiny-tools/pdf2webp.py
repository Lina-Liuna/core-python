import fitz
from PIL import Image
import os
from pathlib import Path
from fpdf import FPDF

pdf_dir = '/Users/linaliu/code/Lina-Liuna.github.io/chinese_grade1/'
image_dir = '/Users/linaliu/code/Lina-Liuna.github.io/images/'

target_width = 300  # Replace with your desired width in pixels
pdf_width = 612
pdf_height = 792
target_height = int(pdf_height * (target_width / pdf_width))
target_resolution = (target_width, target_height)

def pdf2webp(pdf_dir, pdf_name,image_folder):
    pdf_path = pdf_dir + pdf_name
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        image = page.get_pixmap(
            matrix=fitz.Matrix(target_resolution[0] / page.rect.width, target_resolution[1] / page.rect.height))
        pdf_name = pdf_name.replace('.pdf', '')
        image_path = f'{image_folder}{pdf_name }.webp'
        image_pil = Image.frombytes("RGB", [image.width, image.height], image.samples)
        image_pil.save(image_path, "WEBP")

    pdf_document.close()


def pdf2webp_loops(pdir, idir):
    os.chdir(pdir)
    paths = sorted(Path(pdir).iterdir(), key=os.path.getmtime)
    print(paths)
    for pdffile in paths:
        basename = os.path.basename(pdffile)
        dirname = os.path.dirname(pdffile)
        print(basename)
        if '.pdf' not in basename:
            continue
        pdf2webp(pdir, basename, idir)

pdf2webp_loops(pdf_dir, image_dir)
