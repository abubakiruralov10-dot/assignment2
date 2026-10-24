n = []
days = int(input("Enter the days progress take: "))
for a in range(days):
    which_day = int(input())
    n.append(which_day)


for b in range(len(n)):
    print(f"Day {b+1}: {n[b]} ")

print(f"First height: {n[0]}")
print(f"Last height: {n[-1]}")
print(f"Change: {n[-1] - n[0]}")


