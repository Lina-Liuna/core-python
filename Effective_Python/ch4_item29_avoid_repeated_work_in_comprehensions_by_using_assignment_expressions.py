# writing a program to manage orders for a shoes store.
# as new orders come in from customers, I need to be able to tell them whether I can fulfill their orders.
# I need to verify that a request is sufficiently in stock and above the minimum threshold for shopping.

shoes_color_stock = {
    'write' : 100,
    'floral': 10,
    'black' : 60,
    'pink' :20,
    'mix':5
}

order = ['floral', 'black', 'pink']

def get_batches(count, size):
    return count // size

found = {name:batches for name in order
         if (batches := get_batches(shoes_color_stock.get(name, 0), 8))}
print(found.items())

found = ((name, batches) for name in order
         if (batches := get_batches(shoes_color_stock.get(name, 0), 8)))

print(list(found))