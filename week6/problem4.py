def jump_limits(distances):
    return (min(distances) , max(distances))


assert jump_limits([4.2, 3.8, 4.5, 4.0]) == (3.8, 4.5)
assert jump_limits([3.5, 3.5]) == (3.5, 3.5)
assert jump_limits([4.1]) == (4.1, 4.1)
