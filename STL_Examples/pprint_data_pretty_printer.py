import pprint
s = 'I am sorry to rain on your parade but I have to stop thinking of you everyday and night'
stuff = s.split(' ')
#stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

pp = pprint.PrettyPrinter(width=61, compact=True)
pp.pprint(stuff)


import json
import pprint
import urllib
from urllib.request import urlopen
# This restores the same behavior as before.
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#input = input.replace("!web ", "")
url = 'https://pypi.org/pypi/sampleproject/json'
with urlopen(url) as resp:
    project_info = json.load(resp)

pprint.pprint(project_info)
pprint.pprint(project_info, depth=1)
pprint.pprint(project_info, depth=1, width=40)