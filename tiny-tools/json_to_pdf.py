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