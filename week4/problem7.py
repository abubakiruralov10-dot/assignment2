rows = int(input("Enter number of rows: "))

total_cans = 0

for i in range(1, rows + 1):
    total_cans += i  

# print() buyrug'ini sikldan tashqariga, ya'ni boshiga bo'sh joy tashlamasdan yozamiz
print("Total cans:", total_cans)