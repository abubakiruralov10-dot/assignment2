def classify(value):
    if value < 118:
        return "Below range"
    elif 118 <= value <= 122:
        return "In range"
    elif value > 118:
        return "Above range"


def calculate_avarage(total, count):
    average = total/count
    return average

# Main part

number = int(input("Enter the number of candles: "))
total_height = 0
in_range = 0
above_range = 0
below_range = 0
for i in range(number):
    height = int(input("Enter the candle height: "))
    if classify(height) == "Above range":
        above_range += 1
        total_height += height
    elif classify(height) == "Below range":
        below_range += 1
        total_height += height
    elif classify(height) == "In range":
        total_height += height
        in_range += 1
    classification = classify(height)
    print(classification)

average_height = calculate_avarage(total_height, number)

print(f"Total height: {total_height} mm")
print(f"Average height: {average_height} mm")
print(f"Below range: {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}")




