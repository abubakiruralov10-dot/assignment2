#Variant 1

tickets = int(input("How many tickets do you have: "))
answer=input("Is the customer a student? (yes/no): ")
money = int(input("How much money you have?: "))
choices = ["yes","no"]

if answer == "yes" and tickets >= 5:
    print("Price per ticket is 8")
    print(f"Total cost: {tickets*8}")
    if money - tickets*8 == 0:
       print("Exactly enough money")
    elif money - tickets*8 > 0:
       print(f"Money left: {money-tickets*8}")
    else:
       print(f"More money needed: {tickets*8-money}")
elif answer == "yes" and tickets <5:
    print("Price per ticket is 10")
    print(f"Total cost: {tickets*10}")
    if money - tickets*10 == 0:
             print("Exactly enough money")
    elif money - tickets*10 > 0:
           print(f"Money left: {money-tickets*10}")
    else:
          print(f"More money needed: {tickets*10-money}")
elif answer == "no" and tickets >= 5:
    print("Price per ticket is 10")
    print(f"Total cost: {tickets*10}")
    if money - tickets*10 == 0:
             print("Exactly enough money")
    elif money - tickets*10 > 0:
           print(f"Money left: {money-tickets*10}")
    else:
           print(f"More money needed: {tickets*10-money}")
elif answer == "no" and tickets <5:
    print("Price per ticket is 12")
    print(f"Total cost: {tickets*12}")
    if money - tickets*12 == 0:
             print("Exactly enough money")
    elif money - tickets*12 > 0:
           print(f"Money left: {money-tickets*12}")
    else:
           print(f"More money needed: {tickets*12-money}")
else:
      print("Error")



 