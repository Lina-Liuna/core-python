import fibo
fibo.fib(1000)
fibo.fib2(100)
print(fibo.__name__)

fib = fibo.fib
fib(500)

from fibo import fib, fib2
fib(500)

from fibo import *
fib(500)

import fibo as fib
fib.fib(500)

from fibo import fib as fibonacci
fibonacci(500)

import fibo, sys
print(dir(fibo))
print(dir(sys))

import builtins
print(dir(builtins))