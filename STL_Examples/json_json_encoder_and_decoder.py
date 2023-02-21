# What is JSON?
# JavaScript Object Notation, is a lightweight data interchange format inspired by javascript object literal syntax.

# Warning: Be cautious when parsing JSON data from untrusted sources.
# A malicious JSON string may cause the decoder to consume considerable CPU and memory resources.
# Limiting the size of data to be parsed is recommended.

# json exposes an API familiar to users of the standard library marshal and pickle modules.

# Encoding basic python object hierarchies
import json

# why print [] square brackets instead of () Parentheses?
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

print(json.dumps([1,2,3,{'4':5, '6': 7}]))
print(json.dumps([1,2,3,{'4':5, '6': 7}], separators=(',',':')))
print(json.dumps([1,2,3,{'4':5, '6': 7}], separators=('','')))
print(json.dumps([1,2,3,{'4':5, '6': 7}], separators=('?','*')))
print(json.dumps([1,2,3,{'4':5, '6': 7}], separators=('--------','-----')))


data = {
  'first_name': 'Lina',
  'last_name': 'Liu',
  'titles': ['MTS', 'Developer']
}
# use json.dumps to convert python dict into a JSON String.
print(json.dumps(data))
print(json.dumps(data, sort_keys=True))
print(json.dumps(data, separators=('*','?')))
print(json.dumps(data, indent=4))

# use json.load to convert json string into python dict
contact_data= """{
    "Name":"Lina Liu",
    "Title":"MTS",
    "Email":"liuna.lina@gmail.com"
    }"""
print(json.loads(contact_data))

# what happened if repeated name in json string
weird_json = '{"x": 1, "x": 2, "x": 3}'
print(json.loads(weird_json))