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


def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield     # Receive initial amplitude
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output    # Recevie next amplitude

def run_modulating(it):
    amplitudes = [ None, 1, 3, 5, 7, 9, 8, 6, 4, 2]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)


run_modulating(wave_modulating(12))

# The advice: avoid the send method entirely and go with a simpler approach.


# The easist solution is to pass an iterator into the wave function.
# The iterator should return an input amplitude each time the next built-in function is called on it.
# this arragement ensures that each generator is progressed in a cascade as inputs and outputs are processed.
def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it) # Get next input
        output = amplitude * fraction
        yield output


def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)


def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)

run_cascading()

# Things to Remember:
# 1. The send method can be used to inject data into a generator by giving the yield expression a value that can be
# assigned to a variable.

# 2. Using send with yield from expressions may cause surprising behavior, such as non values appearing at unexpected times
# in the generator output

# 3. Providing an input iterator to a set of composed generators is a better approach than using send method,
# which should be avoided.

