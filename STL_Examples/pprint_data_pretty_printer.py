import pprint
s = 'I am sorry to rain on your parade but I am have to stop thinking of you everyday and night'
stuff = s.split(' ')
#stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

pp = pprint.PrettyPrinter(width=61, compact=True)
pp.pprint(stuff)