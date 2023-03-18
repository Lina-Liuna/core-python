import json
import os
from fpdf import FPDF

class JsonData:
    def __init__(self, filename):
        with open(filename) as f:
            self._data = json.load(f)

    def __getattribute__(self, name):
        print(f'called __getattribute__ {name!r}')
        data_dict = super().__getattribute__('_data')
        return data_dict[name]


json_data = JsonData('quiz_data.json')
print(json_data.answer)
print(json_data.options)
print(json_data.question)


class PDFFileProperty:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        print(f'called __getattribute__ {name!r}')
        data_dict = super().__getattribute__('_data')
        return data_dict[name]

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        data_dict = super().__getattribute__('_data')
        data_dict[name] = value

pdf_data = {
   'orientation': 'P',
    'format' : 'A4',
    'unit' : 'mm',
    'font_size' :10,
    'font_name': 'BreadleySansRegular-MVyEB',
    'page_mode': "FULL_SCREEN",
    'pdf_name' : 'test.pdf',
    'font_ttf' : os.getcwd() + '/font/' + 'BreadleySansRegular-MVyEB.ttf',
    'uni' : True
}
pdf_file_attribute = PDFFileProperty(pdf_data)
print(pdf_file_attribute.format)


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
        pdf.cell(w=2, h=self.pdf_property.font_size, txt=f'test here', ln=1)

        pdf.output(self.pdf_property.pdf_name, 'F')


json2pdf = JsonToPDF(json_data, pdf_file_attribute)
json2pdf.words_to_pdf()