# In Python, there are two types that represent sequences of character data: bytes and str

a = b'h\x65llo'
print(list(a))
print(a)

a = 'a\u0300 propos'
print(list(a))
print(a)

# f.write() argument must be str, not bytes
# 1. bytes contains sequences of 8-bit values, and str contains sequences of Unicode code points
# 2.  use helper functions to ensure that the inputs you operate on are the type of character sequence that you
# expect.
# 3. bytes and str instances can't be used together with operators
# 4. if you want to read/write binary data always open the file with binary mode(rb, wb)
# 5. if you want to read or write unicode data to/from a file, be careful about your system's default text encoding
# Explicitly pass the encoding parameters to open if you want to avoid surprises.

