users = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


names = []

# for user in users:
#     names.append(user[0])

# Transform
names = [user[0] for user in users]
print(names)

# Filter
names = [user for user in users if user[1] > 2]
print(names)

# Filter and transform
names = [user[0] for user in users if user[1] > 2]
print(names)

# Transform using map()
names = list(map(lambda user: user[0], users))
print(names)

# Filter using filter()
names = list(filter(lambda user: user[1] > 2, users))
print(names)