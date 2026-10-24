def is_in_range(number,lower,upper):
    if lower <= number <= upper:
        return True
    else:
        return False
assert is_in_range(5, 1, 10) == True
assert is_in_range(1, 1, 10) == True
assert is_in_range(10, 1, 10) == True
assert is_in_range(0, 1, 10) == False
assert is_in_range(11, 1, 10) == False
