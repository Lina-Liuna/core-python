# yield expressions provide generator functions with a simple way to produce an iterable series of output values.
# this channel appears to be unidirectional: there is no immediately obvious way to simultaneously stream data in and
# out of a generator as it runs.

# Example: I'm writing a program to transmit signals using a software-defined radio.
# I use a function to generate an approximation of a sine wave with a given number of points.
import math


def wave(amplitude, steps):
    step_size = 2 * math.pi / steps

    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output


def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')


def run(it):
    for output in it:
        transmit(output)

run(wave(3.0, 8))

# Problem: what if I want to modulate the amplitude on each iteration of the generator?
# Python generator support the send method, which upgrades yield expressions into a two-way channel.

# The send method can be used to provide streaming inputs to a generator at the same time it's yielding outputs.
# the side-effect using send method:
# it's hard to see the connection between yield and send without already knowing the details of this advance generator feature.

