import yaml

import os
from fpdf import FPDF
import random

class YamlData:
    def __init__(self, filename):
        with open(filename) as f:
            self.data = yaml.safe_load(f)


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


def get_font_color():
    color_list = [(71, 159, 248),
                  (129,214,83),
                  (219,58,38),
                  (242,177,61),
                  (43,59,141),
                  (255,66,161),
                  (0,250,255),
                  (39,255,254),
                  ]
    bc = random.choice(color_list)
    return bc

class YamlToPDF:
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
            font_color = get_font_color()
            pdf.set_text_color(font_color[0], font_color[1],font_color[2])
            pdf.cell(w=3, h=10, txt=f'{rank}:  {word}', ln=1)
            for item in meaning_example:
                self.pdf_property.font_size = 12
                pdf.set_font(self.pdf_property.font_name, '', self.pdf_property.font_size)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(w=3, h=10, txt=f' {item}', ln=1)

        pdf.output(self.pdf_property.pdf_name, 'F')

yaml_name = 'vocabulary'
yaml_data = YamlData('yaml_files/'+ yaml_name + '.yaml')


pdf_data = {
   'orientation': 'P',
    'format' : 'A4',
    'unit' : 'mm',
    'font_size' :10,
    'font_name': 'Arial Rounded Bold',
    'page_mode': "FULL_SCREEN",
    'pdf_name' : os.getcwd() + '/pdf_files/' + yaml_name + '.pdf',
    'font_ttf' : os.getcwd() + '/font/' + 'MerriweatherSansLight-8x72.ttf',
    'uni' : True
}
pdf_file_attribute = PDFFileProperty(pdf_data)
print(pdf_file_attribute.format)



yaml2pdf = YamlToPDF(yaml_data.data, pdf_file_attribute)
yaml2pdf.words_to_pdf()