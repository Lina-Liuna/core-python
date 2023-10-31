# importing required modules
from PyPDF2 import PdfReader

# creating a pdf reader object
dir = '/Users/linaliu/books/librarybooks/from_LA_Library/linuxhomework/linuxcmdline/'

# dir = '/Users/linaliu/code/DVC/english/pdf_files/'

dir = '/Users/linaliu/code/DVC/CS-110-5129-intro-programming/lectures/'
foldername = 'test'
pdfdir = dir

pdfname = pdfdir + "9.pdf"

# reader = PdfReader('/Users/linaliu/code/DVC/english/Hyper_Education_Why_Good_Schools,_Good_Grades,_and..._----_(PART_III._GOOD_BEHAVIOR).pdf')
reader = PdfReader(pdfname)
# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
for pagenum in range(1, len(reader.pages)):
    print(pagenum)
    page = reader.pages[pagenum]
    text = page.extract_text()
    print(text)