def ticket_price(age):
    if age < 12:
        return 20000
    else:
        return 35000

def total_price(first_age, second_age):
    return ticket_price(first_age) + ticket_price(second_age)

assert ticket_price(11) == 20000
assert ticket_price(12) == 35000
assert total_price(8, 10) == 40000
assert total_price(8, 20) == 55000
assert total_price(20, 8) == 55000
assert total_price(18, 25) == 70000
