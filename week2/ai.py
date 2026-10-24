# Kirish ma'lumotlarini o'qib olish (masalaning shartiga qarab)
n50 = int(input())  # 50,000 so'mliklar soni
n20 = int(input())  # 20,000 so'mliklar soni
amount = int(input())  # Mijoz yechib olmoqchi bo'lgan summa

possible = False

# 50,000 so'mliklar sonini 0 dan n50 gacha birma-bir tekshiramiz
for x in range(n50 + 1):
    qoldiq = amount - (x * 50000)
    
    # Qoldiq musbat bo'lib, 20,000 ga qoldiqsiz bo'linsa
    if qoldiq >= 0 and qoldiq % 20000 == 0:
        y = qoldiq // 20000  # Kerakli 20,000 so'mliklar soni
        
        # Agar bu 20,000 so'mliklar bizda yetarli bo'lsa
        if y <= n20:
            possible = True
            break  # Topildi, ortiq qidirish shart emas

# Natijani chiqarish
if possible:
    print("Withdrawal possible")
else:
    print("Withdrawal impossible")