numbers = [2, 4, 1, 45, 75, 22]
# numbers.sort(reverse=True)
# The differemce between sort and sorted is sorted will return a new list.
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

users = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


def custom_sort(element: list):
    return element[1]


# users.sort(key=custom_sort)

users.sort(key=lambda el: el[1])
print(users)
