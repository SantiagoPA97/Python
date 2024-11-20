greeting = "Hello"


def greet():
    # Bad practice to use global variables inside functions
    global greeting
    greeting = "Hi"


print(greeting)
greet()
print(greeting)
