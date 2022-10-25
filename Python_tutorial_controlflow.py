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


























