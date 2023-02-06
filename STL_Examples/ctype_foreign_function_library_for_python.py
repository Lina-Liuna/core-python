# ctypes module:
# it provides C compatible data types, and allows calling functions in DLLs or shared libries.
# it can be used to wrap these libries in pure python.

import ctypes
print(ctypes.cdll.LoadLibrary('/usr/local/lib/python3.9/site-packages/cv2/cv2.abi3.so'))
print(ctypes.c_int())
print(ctypes.c_wchar_p("Good Morning, today is Feb 6, 2023, 06:33"))

s = "Good Morning, today is Feb 6, 2023, 06:33"
c_s = ctypes.c_wchar_p(s)
print(c_s.value)
