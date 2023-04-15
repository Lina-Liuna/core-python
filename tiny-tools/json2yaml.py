import json
import os
from fpdf import FPDF
import yaml
import collections

class JsonData:
    def __init__(self, filename):
        with open(filename) as f:
            self.data = json.load(f)


class YamlData:
    def __init__(self, filename, dict_data):
        with open(filename, 'w') as f:
            self.data = yaml.safe_dump(dict_data, f)

def pure_json_data(data):
    new_dict = dict()
    for rank, (word, meaning_example) in enumerate(data.items(), 1):
        word = word.replace(':', '')
        # print(f'{word}')
        example_list = list()
        for item in meaning_example:
            if len(item) > 0 and item[0] == ' ':
                item = item[1:]
            if len(item) > 0 and  item[-1].isalpha() == False:
                item = item[:-1]
            example_list.append(item)
        new_dict[word] = example_list
    return new_dict

json_name = "new_words"
json_data = JsonData('json_files/'+ json_name + '.json')
new_data = pure_json_data(json_data.data)
print(new_data)
yaml_name = "vocabulary"
YamlData('yaml_files/' + yaml_name + '.yaml', new_data)



