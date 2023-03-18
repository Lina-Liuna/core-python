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
    'font_size' :'10',
    'font_name': 'BreadleySansRegular-MVyEB',
    'page_mode': "FULL_SCREEN",
    'pdf_name' : 'test.pdf'

}

pdf_file_attribute = PDFFileProperty(pdf_data)
print(pdf_file_attribute.format)