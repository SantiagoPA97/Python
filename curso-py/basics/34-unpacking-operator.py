list1 = [1, 2, 3, 4]
list2 = [5, 6]
tuple1 = (7, 8, 9, 10)

print(*list1)
print(*tuple1)

def n(n1, n2, n3, n4):
    print("printing n", n1, n2, n3, n4)

n(*list1)

combined = [*list1, *list2]
print(combined)

# With dictionaries:
point1 = { "x": 19 }
point2 = { "y": 15 }

newPoint = { **point1, **point2 }
print(newPoint)