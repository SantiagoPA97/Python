def suma(*numbers) -> None:
    result = 0
    for number in numbers:
        result += number
    print(result)


suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
