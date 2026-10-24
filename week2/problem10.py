unit = int(input("Enter units used: "))
if unit <= 100:
    print(f"Total bill:{unit*500} so'm")
elif 100 < unit <= 200:
    print(f"{100*500+700*(unit-100)}")
elif unit > 200:
    print(f"{100*500+100*700+1000*(unit-200)}")
else:
    print("Error")