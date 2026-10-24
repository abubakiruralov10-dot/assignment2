def prepare_boards(lenghts, needed):
    sorted_org = sorted(lenghts)
    choose = sorted_org[:needed]

    return sorted_org, choose

lengths = [60, 20, 50, 20, 35]
needed = 3

sorted_b, selected_b = prepare_boards(lengths, needed)

print(f"Original: {lengths}")
print(f"Sorted: {sorted_b}")
print(f"Selected: {selected_b}")
print(f"Total selected length: {sum(selected_b)}")