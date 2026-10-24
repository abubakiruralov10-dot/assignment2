bins =  int(input("Enter the number of bins: "))
total_bottles = 0
empty_bins = 0
for bottle_count in range(bins):
    bottle = int(input("Enter the bottle count: "))
    if bottle == 0:
        empty_bins += 1
    else:
        total_bottles += bottle
print(f"Total bottles: {total_bottles}")
print(f"Empty bins: {empty_bins}")
