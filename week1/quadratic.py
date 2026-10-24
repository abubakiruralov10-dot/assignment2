a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
D = b**2 - 4*a*c
if D > 0:
    print("Two real roots")
elif D == 0:
    print("One real root")
else:
    print("No real roots")

