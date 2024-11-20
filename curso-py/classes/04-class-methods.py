class Dog:
    legs = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def speak(cls):
        print("Woof!")

    @classmethod
    def factory(cls):
        return cls("Tequila", 5)


Dog.speak()
my_dog = Dog("Kira", 5)
my_dog2 = Dog.factory()
print(my_dog2.age, my_dog2.name)
