def replace_value(values, index, new_value):
    values[index] = new_value

def find_first(values, target):
    for a in range(len(values)): 
        if values[a] == target:
            return a          
    return -1

def summarize(values):
    stats_record = (min(values), max(values), sum(values))
    return stats_record  

number = int(input("Enter the number of days: "))
original = []
for i in range(number):
    time = int(input("Enter reading time in minutes: "))
    original.append(time)

updated = original[:]

index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new reading time: "))
replace_value(updated, index, new_value)

target = int(input("Enter the reading time to search for: "))

stats_record = summarize(updated)
minimum, maximum, total = stats_record

first = find_first(updated, target)
count = updated.count(target)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted(updated)}")
print(f"Minimum reading time: {minimum} minutes")
print(f"Maximum reading time: {maximum} minutes")
print(f"Total reading time: {total} minutes")

if first == -1:
    print("First matching index: Target not found")
else:
    print(f"First matching index: {first}")

print(f"Matching values: {count}")