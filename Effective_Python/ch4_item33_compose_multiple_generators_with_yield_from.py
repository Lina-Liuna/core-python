# Generators are so useful that many programs start to look like layers of generators strung together.

# Example: I have a graphical program that's using generators to animate the movement of images onscreen.
# To get the visual effect I'm looking for, I need the images to move quickly at first, pause temporarily,
# and then continue moving at a slower pace.

# I define two generators that yield the expected onscreen deltas for each part of this animation.

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