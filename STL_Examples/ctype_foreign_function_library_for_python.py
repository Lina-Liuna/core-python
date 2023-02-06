# ctypes module:
# it provides C compatible data types, and allows calling functions in DLLs or shared libries.
# it can be used to wrap these libries in pure python.

import ctypes
print(ctypes.cdll.LoadLibrary('/usr/local/lib/python3.9/site-packages/cv2/cv2.abi3.so'))
