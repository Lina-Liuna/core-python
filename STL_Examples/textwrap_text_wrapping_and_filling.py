import textwrap

s = 'It is raining outside, today is last day of 2022!'
print(textwrap.shorten(s, width=len(s)))
print(textwrap.shorten(s, width=len(s) - 5))
print(textwrap.shorten(s, width=len(s) - 5, placeholder='***'))

# remove any common leading whitespace from every line in text
s = """\
       she told me she likes me as a friend.
          I told her that in C++, Friends can 
             access the private parts
"""
print(s)
print(repr(s))
print(repr(textwrap.dedent(s)))
