# importing required modules
from PyPDF2 import PdfReader

# creating a pdf reader object
reader = PdfReader('/Users/linaliu/code/DVC/english/Hyper_Education_Why_Good_Schools,_Good_Grades,_and.._(PART_II._GOOD_GRADES).pdf')

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
for pagenum in range(1, len(reader.pages)):
    page = reader.pages[pagenum]
    text = page.extract_text()
    print(text)