a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
D = b**2 - 4*a*c
if D >0:
    print("Two real roots")
elif D == 0:
    print("One real root")
else:
    print("No real roots")