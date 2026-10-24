a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if (a+b>c and a+c>b and b+c>a) and (a != b != c):
    print("Scalene")
elif (a+b>c and a+c>b and b+c>a) and (a == b == c):
    print("Equilateral")
elif (a+b>c and a+c>b and b+c>a) and (a == b or a == c or b == c):
    print("Isosceles")
else:
    print("Not a triangle")
