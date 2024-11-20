class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says Woof!")


my_dog = Dog("Kira", 5)
my_dog2 = Dog("Tequila", 5)
print(type(my_dog))
print(isinstance(my_dog, Dog))
print(my_dog.name)
print(my_dog2.name)
my_dog.speak()
