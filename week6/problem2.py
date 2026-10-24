def book_position(codes, wanted):
    count = 0
    for code in codes:
        if code  == wanted:
            count += 1
    return count


codes = ["BK103", "BK207", "BK103", "BK410"]

assert book_position(codes, "BK207") == 1
assert book_position(codes, "BK103") == 0
assert book_position(codes, "BK410") == 3
