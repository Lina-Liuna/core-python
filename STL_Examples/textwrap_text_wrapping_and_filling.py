import textwrap

s = 'It is raining outside, today is last day of 2022!'
print(textwrap.shorten(s, width=len(s)))
print(textwrap.shorten(s, width=len(s) - 5))
print(textwrap.shorten(s, width=len(s) - 5, placeholder='***'))