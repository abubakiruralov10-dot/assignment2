a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# 1. Agar 'a' o'rtada bo'lsa
if (b <= a <= c) or (c <= a <= b):
    print(f"Middle value: {a}")

# 2. Agar 'b' o'rtada bo'lsa
elif (a <= b <= c) or (c <= b <= a):
    print(f"Middle value: {b}")

# 3. Agar 'c' o'rtada bo'lsa
elif (a <= c <= b) or (b <= c <= a):
    print(f"Middle value: {c}")

else:
    print("Error")