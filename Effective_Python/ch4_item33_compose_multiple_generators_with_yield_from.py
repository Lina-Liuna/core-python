# Generators are so useful that many programs start to look like layers of generators strung together.

# Example: I have a graphical program that's using generators to animate the movement of images onscreen.
# To get the visual effect I'm looking for, I need the images to move quickly at first, pause temporarily,
# and then continue moving at a slower pace.

# I define two generators that yield the expected onscreen deltas for each part of this animation.

# what is the meaning of "for _ in range()?"
# when you are not interested in some values returned by a function we use underscore in place of variable name.
# basically it means you are not interested in how many times the loop is run till now just that it should run
# some specific number of times overall.

def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

def render(delta):
    print(f'Delta:{delta:.1f}')
    # Move the images onscreen

def run(func):
    for delta in func():
        render(delta)

run(animate)

# improvement in function animate:
# why make improvement in animate: repetitive and redundancy
# The solution: use the yield from expression.
# use the yield from expression allows you to yield all values from a nested generator
# before returning control to the parent generator

# reimplment the animation function by using yield from:

def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)

run(animate_composed)


# yield from expression essentialy causes the python interpreter to handle the nested for loop and yield expression
# boilerplate for you, which results in better performance.

# Excellent example: verify the speedup by using the timeit built-in module to run a micro-benchmark:

import timeit

def child():
    for i in range(1_000_000):
        yield i

def slow():
    for i in child():
        yield i

def fast():
    yield from child()

baseline = timeit.timeit(stmt='for _ in slow(): pass',
                         globals=globals(),
                         number=50)
print(f'Manual nesting {baseline:.2f}s')

comparison = timeit.timeit(stmt='for _ in fast(): pass',
                           globals=globals(),
                           number=50)
print(f'Composed nesting {comparison:.2f}s')

reduction = -(comparison - baseline) / baseline
print(f'{reduction:.1%} less time')

# Things to Remember
# 1. the yield from expression allows you to compose multiple nested generators together into a single combined generator.
# 2. yield from provides better performance than manually itertating nested generators and yielding their outputs.

