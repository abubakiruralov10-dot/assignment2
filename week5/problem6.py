batteries = [25, 80, 95, 60]

# 1. Quvvat miqdorini o'qiymiz
charge = int(input())

# 2. Batareyalarni quvvatlaymiz (maksimal 100 gacha)
for i in range(len(batteries)):
    batteries[i] += charge
    if batteries[i] > 100:
        batteries[i] = 100

# 3. Oxirgi qurilmani o'chirib, qiymatini chiqaramiz
last_device = batteries.pop()
print(last_device)

# 4. Yangi qurilma darajasini o'qib, oxiriga qo'shamiz
new_device = int(input())
batteries.append(new_device)

# 5. Qolgan batareyalar ro'yxatini chiqaramiz
print(batteries)