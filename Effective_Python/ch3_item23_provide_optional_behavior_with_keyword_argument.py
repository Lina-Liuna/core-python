# you can assign keyword arguments withing the parentheses of a function call.
# you can mix and match keyword and positional arguments.
import collections

acronym_words = {
    'FYI': 'For your information',
    'BTW': 'By the way',
    'GR8': 'Great',
    'IDK': 'I don\'t know',
    'IDC': 'I don\'t care',
    'JK' : 'Just kidding',

}

def words(word, meaning):
    print(f'{word}:{meaning}')

#words(**acronym_words)     #error, dont find word and meaning
acronym_words = {
    'word': 'FYI',
    'meaning': 'For your information',
}
words(**acronym_words)


fruit_count = {
    'apple' : 3,
    'blueberry': 200,
    'strawberry': 10,
}

def print_fruit(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}={value}')

#print_fruit(**fruit_count)

print_fruit(cherry=1.5, raspberry=9, blackberry=6)

# give keyword argument a default value can make it optional

def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period
weight_diff = 0.5
time_diff = 3
flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)

# Things to remember:
# 1. Function arguments can be specified by position or by keyword
# 2. keyword make it clear what the purpose of each argument is when it would be confusing with only positional argument.
# 3. keyword arguments with default values make it easy to add new behaviors to a function without needing to migrate
# all existing calls.
# 4. Optional keyword arguments should always be passed by keyword instead of by position.




