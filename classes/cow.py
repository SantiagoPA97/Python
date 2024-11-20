from classes.animal import Animal

class Cow(Animal):
  def speak(self) -> None:
    print("Moo")
    
  def move(self) -> None:
    print("Walking slowly")
      