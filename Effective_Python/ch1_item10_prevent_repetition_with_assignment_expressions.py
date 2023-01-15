# a = b pronounced "a equals b"
# a := b pronounced 'a walrus b' why? because := looks like a pair of eyeballs and tusks

# walrus operator is a new syntax(3.8 or later)
# walrus operator used to solve a long-standing problem with the language that can cause code duplication.

# Assignment expression are useful because they enable you to assign variables in places where assignment statements
# are disallowed, such as in the conditional expression of an if statement.

# An assignment expression's value evaluates to whatever was assigned to the identifier on the left side of the
# walrus operator.

class fruit_juice_store:

    fresh_fruit = {
        'strawberry': 50,
        'lemon': 30,
        'watermelon': 20,
        'apple' : 60,
        'mango' : 10,
    }

    def make_lemonade(self, count):
        print(count)

    def make_cider(self, count):
        print(count)

    def slice_bananas(self, count):
        print(count)
        return count * 6

    def make_smoothies(self, count):
        print(count)

    def out_of_stock(self):
        print('out of stock')


class OutOfBananas(Exception):
    pass

fc = fruit_juice_store()

count = fc.fresh_fruit.get('apple', 0)
if count >= 4:
    fc.make_cider(count)
else:
    fc.out_of_stock()


# Improve clarity of above code by using walrus operator:
if (count := fc.fresh_fruit.get('apple', 0)) >= 4:
    fc.make_cider(count)
else:
    fc.out_of_stock()

if (count := fc.fresh_fruit.get('banana', 0)) >= 2:
   pieces = fc.slice_bananas(count)
else:
    pieces = 0
try:
    smoothies = fc.make_smoothies(pieces)

except OutOfBananas:
    fc.out_of_stock()

if (count := fc.fresh_fruit.get('apple', 0)) >= 4:
    fc.make_cider(count)
elif (count := fc.fresh_fruit.get('banana', 0)) >= 2:
    pieces = fc.slice_bananas(count)
    fc.make_smoothies(pieces)
else:
    print("Nothing left")