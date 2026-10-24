value = 1
doubling = 0
target = int(input("Enter the target: "))
while value < target:
    value *=2
    doubling += 1
print(f"Final value: {value}")
print(f"Doublings: {doubling}")