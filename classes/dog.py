from classes.animal import Animal


class Dog(Animal):
    def __init__(self, name: str, breed: str, age: int, owner: str = None):
        # Alternative 1
        # self.breed = breed
        # self.owner = owner
        # self.name = name
        # self.age = age

        # Alternative 2
        super().__init__(name, breed, age)
        self.owner = owner

    def bark(self):
        print("Woof woof")

    def walk(self, steps: int):
        print(f"Walking {steps} steps")

    def speak(self) -> None:
        self.bark()
