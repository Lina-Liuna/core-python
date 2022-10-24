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

a = ['Mary', 'had', 'a', 'little']