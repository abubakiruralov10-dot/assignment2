def digit_sum(number):
    total_sum = 0
    while number > 0:
        digit = number % 10       # Oxirgi raqamni ajratib olish
        total_sum += digit        # Yig'indiga qo'shish
        number = number // 10     # Oxirgi raqamni sondan olib tashlash
    return total_sum

# Assertions (tekshiruvlar)
assert digit_sum(0) == 0
assert digit_sum(507) == 12
assert digit_sum(1111) == 4

# Input va output funksiyadan tashqarida
number = int(input("Enter a number: "))
result = digit_sum(number)
print(f"Digit sum: {result}")