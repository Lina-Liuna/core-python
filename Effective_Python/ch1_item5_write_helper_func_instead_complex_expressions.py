from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)
# repr() functions return a printable representation of the given object
print(repr(my_values))
print(my_values)

print('red ', my_values.get('red'))
print('green ', my_values.get('green'))
print('opacity ', my_values.get('opacity'))