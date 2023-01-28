# defaultdict class from the collections built-in module automatically storing a default value when a key doesn't exist.
# All you have to do is provide a function that will return the default value to use each time a key is missing

from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)

visits = Visits()
visits.add('China', 'Shanghai')
visits.add('China', 'Beijing')
print(visits.data)