def overlap_minutes(start1, end1, start2, end2):
    # Partial overlapping periods
    if start1 < start2 < end1 < end2:
        return end1 - start2
    elif start2 < start1 < end2 < end1:
        return end2 - start1
    # Same periods
    elif start1 == start2 and end1 == end2:
        return end1 - start1
    elif start1 < start2 < end2 < end1:
        return end2 -start2
    elif start2 < start1 < end1 < end2:
        return end1 - start1
    else:
        return 0
    
def can_meet(start1, end1, start2, end2, duration):
    return True if overlap_minutes(start1, end1, start2, end2) >= duration else False

assert overlap_minutes(540, 660, 600, 720) == 60

# One period is inside the other
assert overlap_minutes(540, 720, 600, 660) == 60

# Same periods
assert overlap_minutes(540, 600, 540, 600) == 60

# Periods that touch or are separate
assert overlap_minutes(540, 600, 600, 660) == 0
assert overlap_minutes(540, 600, 660, 720) == 0
assert overlap_minutes(600, 720, 540, 660) == 60
assert can_meet(540, 660, 600, 720, 60) == True
assert can_meet(540, 660, 600, 720, 61) == False


