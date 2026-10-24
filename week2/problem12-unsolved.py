a = int(input())   # 50 000 lik banknotalar soni
b = int(input())   # 20 000 lik banknotalar soni
c = int(input())   # yechmoqchi bo'lgan summa

if c % 10000 != 0:
    print("Withdrawal impossible")
else:
    t = c // 10000
    x = t // 5

    if x > a:
        x = a

    if x % 2 != t % 2:
        x = x - 1

    if x < 0:
        print("Withdrawal impossible")
    else:
        y = (t - 5 * x) // 2
        if y <= b:
            print("Withdrawal possible")
        else:
            print("Withdrawal impossible")