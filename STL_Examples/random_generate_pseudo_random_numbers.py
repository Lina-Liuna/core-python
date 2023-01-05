import random

# Random float: 0.0 <= x < 1.0
random_float = random.random()
print(random_float)

# random float: 2.5 <= x <= 10.0
random_float = random.uniform(2.5, 10.0)
print(random_float)

# Integer from 0 to 999 inclusive
random_integer = random.randrange(1000)
print(random_integer)

# Even Integer from 0 to 100 inclusive
random_integer = random.randrange(0, 101, 2)
print(random_integer)

s = 'Those fat cats in government do not care about the poor'
l = s.split(' ')
random_choice = random.choice(l)
print(random_choice)

deck = s.split()
# To shuffle an immutable sequence and return a new shuffled list
random.shuffle(deck)
print(deck)

# Four samples without replacement
random_sample = random.sample([10, 20, 30, 40, 50], k=4)
print(random_sample)

print(help(random.choices))
random_choice = random.choices(['apple', 'orange', 'pineapple'], k=6)
print(random_choice)

# random.choices return a k sized list of popluation elements chosen with replacement
# [20, 0, 5] is the weighs
random_choice = random.choices(['apple', 'orange', 'pineapple'], [20, 0, 5], k=6)
print(random_choice)

# Deal 20 cards without replacement from a deck of 52 playing cards
# determine the proportion of cards with a ten-value: ten, jack, queen, or king.
# here k is the count of populations
# sample(['red', 'blue'], counts=[4, 2], k=5) is equal to sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
print(help(random.sample))
dealt = random.sample(['ten, jack, queen, king','a2-9'], counts=[9, 6], k=15)
print(dealt)
print(dealt.count('a2-9') / 15)


# Estimate the probability of getting 5 or more heads from 7 spins
# of a biased coin that settles on heads 60% of the time
def trial():
    return random.choices('HT', cum_weights=(0.6, 1.00), k=7).count('H') >= 5

print(sum(trial() for i in range(10_000)) / 10_000)

# Probability of the median of 5 samples being in middle two quartiles
def trial():
    random_choices = random.choices(range(10_000), k=5)
    sorted_choices =sorted(random_choices)
    # print(sorted_choices)

    # [2] here is the middle of 5 random choices [3087, 4038, 5729, 8175, 9978]
    sorted_choices =sorted(random_choices)[2]
    # print(sorted_choices)

    return 2_500 <= sorted_choices < 7500

print(sum(trial() for i in range(10_000)) / 10_000)


# Example of statistical bootstrapping using resampling with replacement to estimate a
# confidence interval for the mean of a sample
# https://www.thoughtco.com/example-of-bootstrapping-3126155
# https://en.wikipedia.org/wiki/Bootstrapping_(statistics)
from statistics import fmean as mean
data = [11,22,33,44,55,66,77,88,99,00, 12,13,14,15, 16]
random_choice = random.choices(data, k=len(data))
mean_rc = mean(random_choice)
print(random_choice)
print(mean_rc)

means = sorted(mean(random.choices(data, k=len(data))) for i in range(100))
print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
      f'interval from {means[5]:.1f} to {means[94]:.1f}')

# Examples of a resampling permutation test to determine the statistical significance or p-value
# of an observed difference between the effects of a drug vs a placebo:
# Example from "Statistics is Easy" by Dennis Shasha and Manda Wilson

import statistics

print(help(statistics.fmean))
# fmean(data): convert data to floats and  compute the arithmetic mean.
drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
observed_diff = statistics.fmean(drug) - statistics.fmean(placebo)

print(help(random.shuffle))
n = 10_000
count = 0
combined = drug + placebo
random.shuffle(combined)
print(combined)
for i in range(n):
    random.shuffle(combined)
    new_diff = statistics.fmean(combined[:len(drug)]) - statistics.fmean(combined[len(drug):])
    count += (new_diff >= observed_diff)

print(f'{n} label reshufflings produced only {count} instances with a difference')
print(f'at least as extreme as the observed difference of {observed_diff:.1f}.')
print(f'The one-sided p-value of {count / n:.4f} leads us to reject the null')
print(f'hypothesis that there is no difference between the drug and the placebo.')

# Simulation of arrival times and service deliveries for a multiserver queue:
from heapq import heapify, heapreplace
from random import expovariate, gauss
from statistics import mean, quantiles

average_arrival_interval = 5.6
average_service_time = 15.0
stdev_service_time = 3.5
num_servers = 3

waits = []
arrival_time = 0.0
servers = [0.0] * num_servers  # time when each server becomes available
heapify(servers)
for i in range(1_000_000):
    arrival_time += expovariate(1.0 / average_arrival_interval)
    next_server_available = servers[0]
    wait = max(0.0, next_server_available - arrival_time)
    waits.append(wait)
    service_duration = max(0.0, gauss(average_service_time, stdev_service_time))
    service_completed = arrival_time + wait + service_duration
    heapreplace(servers, service_completed)

print(f'Mean wait: {mean(waits):.1f}   Max wait: {max(waits):.1f}')
print('Quartiles:', [round(q, 1) for q in quantiles(waits)])

# Statistics for Hackers: https://www.youtube.com/watch?v=Iq9DzN6mvYA
# statistics analysis using just a few fundamental concepts including simulation, sampling,
# shuffling, and cross-validation
# Economics simulation: https://nbviewer.org/url/norvig.com/ipython/Economics.ipynb
# a simulation of a marketplace shows effective use of many of the tools
# A Concrete introduction to probability: https://nbviewer.org/url/norvig.com/ipython/Probability.ipynb
# the basics of probability theory, how to write simulations, and how to perform data analysis using paython


