print("Welcome to the advanced calculator!")
print("Please type exit to quit the program.")
print("Operations: +, -, *, /")
result = None

while True:
    if not result:
        result = input("Enter the first number: ")
        if result.lower() == "exit":
            break
        result = float(result)

    op = input("Enter the operation: ")
    if op.lower() == "exit":
        break

    n2 = input("Enter the second number: ")
    if n2.lower() == "exit":
        break
    n2 = float(n2)

    if op == "+":
        result += n2
    elif op == "-":
        result -= n2
    elif op == "*":
        result *= n2
    elif op == "/":
        result /= n2
    else:
        print("Invalid operation.")
        break

    print(f"Result: {result}")
