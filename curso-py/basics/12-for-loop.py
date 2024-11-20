search = 10

for number in range(5):
    if number == search:
        print("Found!")
        break
else:
    print("Not found!")

# The same as above
if search in range(5):
    print("Found!")
