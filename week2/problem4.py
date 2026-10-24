a = int(input("Enter a number: "))
if a%15 == 0:
    print("Divisible by both")
elif a%5 == 0 and a%3 != 0:
    print("Divisible by 5")
elif a%5 != 0 and a%3 == 0:
    print("Divisible by 3")