words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#Create a sample collection
users = {'Hans': 'active', 'Eleonore': 'inactive', 'JL': 'active'}

#Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

#Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status

print(active_users)

for i in range(3):
    print(i)

print(list(range(5, 10)))
print(list(range(5, 10, 3)))
print(list(range(-10, -100, -30)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# Python 3.9 doesn't support match statement!!!!!!!!!!
#def http_error(status):
    #match status:
        #case 400:
            #return "Bad Request"

def ask_ok(prompt, retries=4, reminder='Please try agian!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')
ask_ok("Ok to overwrite the file?", 2)
ask_ok('Ok to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5
def f(arg=i):
    print(arg)

i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#if you don't want the default to be shared between subsequent calls,
#you can write the function like this instead:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def parrot(voltage, state='a stiff', action='voom',type='Norwegian Blue'):
    print("--This parrot wouldn't", action, end=' ')
    print("if you put", voltage, 'volts through it.')
    print('--Lovely plumage, the', type)
    print("--It's", state, "!")

parrot(100)
parrot(voltage=1000)
parrot(voltage=100000, action='VOOOOOOOM')
parrot(action="VOOOOOOM", voltage=10000000)
parrot('a millon', 'bereft of life', 'jump')

#all the following calls would be invalid
#parrot()                     # required argument missing
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument

def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind, "?")
    print("--I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
        print('-' * 40)
        for kw in keywords:
            print(kw, ":", keywords[kw])


#it could be called like this:
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, very runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg(2)
standard_arg(arg=2)

pos_only_arg(1)
#pos_only_arg(arg=1)   TypeError

kwd_only_arg(arg=3)
#kwd_only_arg(3)     TypeError

#combined_example(1, 2, 3)  TypeError, 3 should be kwd_only=3
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)

def foo(name, **kwds):
    return 'name' in kwds


def foo_right(name, /, **kwds):
    return 'name' in kwds

print(foo_right(1, **{'name':2}))

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

#The reverse situation occurs when the arguments are already in a list or tupe but need to be
#unpacked for a function call requiring separate positional arguments.
#the build-in range() function expectes separate start and stop arguments.
#if they are available separtely, write the function call with *-operator to unpack  the arguments out of a list or tuple:
print(list(range(3,6)))
args = [3, 6]
print(list(range(*args)))

def parrot(voltage, state='a stiff', action='voom'):
    print("--This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state":"bleedin demised", "action": "voom"}
parrot(**d)


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(43)
print(f(1))
print(f(2))

#example uses a lambda expression to return a function. Another use is to pass a small function as an argument
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
























