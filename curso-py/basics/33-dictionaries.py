point = {"x": 25, "y": 50}
point["z"] = 45

if "lala" in point:
    print(point["lala"])

# print("lala", point.get("lala", 0))
# del point["x"]

# for value in point:
#     print(point[value])

# for value in point.items():
#     print(value)

for key, value in point.items():
    print(key, value)


users = [
    {"id": 1, "name": "Santiago"},
    {"id": 2, "name": "Nicolas"},
    {"id": 3, "name": "Felipe"},
    {"id": 4, "name": "Luisa"}
]

for user in users:
    print(user["name"])

for user in users:
    for key, value in user.items():
        print(key, value)
