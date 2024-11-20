name = "Santiago"

class Number:
  def __init__(self, value):
    self.value = value

# Inicio de la función variables
def variables() -> str :
  return "Pelaez"
# Fin de la función variables


def sumNumbers(a: Number, b: int) -> None:
  a.value = a.value + b
  # print(result)

totalSum = Number(10)
print("totalSum1", totalSum.value)

sumNumbers(totalSum, 5)

print("totalSum2", totalSum.value)