
def count_size(sizes, wanted):
    count = 0
    for size in sizes:
        if size == wanted:
         count += 1
    return count

assert count_size([38, 40, 39, 40, 42, 40], 40) == 3
assert count_size([38, 40, 39, 40, 42, 40], 41) == 0
assert count_size([], 40) == 0
