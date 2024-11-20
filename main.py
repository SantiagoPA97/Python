from classes.cow import Cow
from classes.dog import Dog
from variables.variables_scope import variables
from classes.yorkshire_terrier import YorkshireTerrier


def main():
  # dog = Dog("Freya", "Golden Retriever")
  # print(dog)

  # dog2 = Dog(race="Yorkshire Terrier", name="Chiky")

  # print(type(dog2))
  # print("dog2 name", dog2.name)

  # dog.bark()
  # dog.walk(10)
  # print(YorkshireTerrier.__bases__)
  # print(Dog.__subclasses__())
  
  # dog = Dog("Freya", "Mammal", 3, "Santiago")
  # dog.speak()
  # print(dog.owner)
  
  # cow = Cow("Lola", "Mammal", 5)
  # cow.speak()
  
  # MRO Method Order Resolution
  # print(Cow.__mro__)
  
  # yorkshire = YorkshireTerrier("Chiky")
  # print(yorkshire.ownerprop)
  
  # yorkshire.ownerprop = "Santiago"
  # print(yorkshire.ownerprop)
  
  variables()
  
if __name__ == "__main__":
  main()
