b = int(input("Enter a number: "))
a = int((input("Enter another number: ")))
option = input("Choose an operation (+, -, *, /): ")
if option == "+":
    result = a + b
    print("The result is:", result)
elif option == "-":
    result = a - b
    print("The result is:", result)
elif option == "*":
    result = a * b
    print("The result is:", result)
elif option == "/":
    if b != 0:
        result = a / b
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
        