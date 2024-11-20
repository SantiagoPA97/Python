class Dog:
    legs = 4
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says Woof!")

Dog.legs = 3 # It changes the value for all the instances
my_dog = Dog("Kira", 5)
my_dog.legs = 5 # It changes the value just for this instance
my_dog2 = Dog("Tequila", 5)
print(Dog.legs)
print(my_dog.legs)
