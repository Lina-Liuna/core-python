import operator

s = 'test operator'
tuple_result = operator.itemgetter(1)(s)
print(tuple_result)
# e
tuple_result = operator.itemgetter(2, 4, 6)(s)
print(tuple_result)
# ('s', ' ', 'p')
print(list(tuple_result))


# ['s', ' ', 'p']
d = {}
for k, v in zip('abcde', '12345'):
    d[k] = v
print(operator.itemgetter('e', 'a', 'b', 'd')(d))
# ('5', '1', '2', '4')

fruit_tuple = [('blueberry', 5), ('raspberry', 3), ('blackberry', 1), ('strawberry', 4)]
get_count = operator.itemgetter(1)
print(get_count)
# operator.itemgetter(1)
print(list(map(get_count, fruit_tuple)))
# [5, 3, 1, 4]

print(sorted(fruit_tuple, key=get_count))


