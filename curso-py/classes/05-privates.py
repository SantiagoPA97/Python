class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def get_name(self):
        return self.__name

    def speak(self):
        print(f"{self.__name} says Woof!")

    @classmethod
    def factory(cls):
        return cls("Tequila", 5)


my_dog = Dog("Kira", 5)
my_dog.speak()
my_dog2 = Dog.factory()
print(my_dog2.age)
print(my_dog2.get_name())
