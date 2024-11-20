numbers = [1, 2, 3]

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# Another approach
# first, second, third = numbers
# first, *others = numbers
# print(first, others)

# first and last element
first, *others, last = numbers
print(first, last)