def count_divisors(number):
    divisors = 0
    for a in range(1,number+1):
        if number%a == 0:
         divisors +=1
    return divisors
assert count_divisors(1) == 1
assert count_divisors(6) == 4
assert count_divisors(7) == 2

number = int(input("Enter a number: "))
result = count_divisors(number)
print(f"Number of divisors: {result}")

        
    