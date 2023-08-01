import json
import os
from fpdf import FPDF

class JsonData:
    def __init__(self, filename):
        with open(filename) as f:
            self.data = json.load(f)

class PDFFileProperty:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        data_dict = super().__getattribute__('_data')
        return data_dict[name]

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        data_dict = super().__getattribute__('_data')
        data_dict[name] = value


class JsonToPDF:
    def __init__(self, json_data, pdf_property):
        self.json_data = json_data
        self.pdf_property = pdf_property

    def words_to_pdf(self):
        pdf = FPDF(orientation=self.pdf_property.orientation, unit=self.pdf_property.unit, format=self.pdf_property.format)
        pdf.page_mode = self.pdf_property.page_mode
        pdf.add_font(self.pdf_property.font_name, '',self.pdf_property.font_ttf,uni=self.pdf_property.uni)
        pdf.set_font(self.pdf_property.font_name, '', self.pdf_property.font_size)
        pdf.add_page()

        for rank, (word, meaning_example) in enumerate(self.json_data.items(), 1):
            self.pdf_property.font_size = 16
            pdf.set_font(self.pdf_property.font_name, '', self.pdf_property.font_size)
            pdf.cell(w=3, h=10, txt=f'{rank}:  {word}', ln=1)
            for item in meaning_example:
                self.pdf_property.font_size = 12
                pdf.set_font(self.pdf_property.font_name, '', self.pdf_property.font_size)
                pdf.cell(w=3, h=10, txt=f' {item}', ln=1)

        pdf.output(self.pdf_property.pdf_name, 'F')

json_name = 'new_words'
json_data = JsonData('json_files/'+ json_name + '.json')


pdf_data = {
   'orientation': 'P',
    'format' : 'A4',
    'unit' : 'mm',
    'font_size' :10,
    'font_name': 'Arial Rounded Bold',
    'page_mode': "FULL_SCREEN",
    'pdf_name' : os.getcwd() + '/pdf_files/' + json_name + '.pdf',
    'font_ttf' : os.getcwd() + '/font/' + 'Arial Rounded Bold.ttf',
    'uni' : True
}
pdf_file_attribute = PDFFileProperty(pdf_data)
print(pdf_file_attribute.format)

json2pdf = JsonToPDF(json_data.data, pdf_file_attribute)
json2pdf.words_to_pdf()