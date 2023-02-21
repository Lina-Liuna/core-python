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