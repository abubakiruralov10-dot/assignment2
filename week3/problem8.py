def hours_to_pay(minutes):
    if minutes % 60 == 0 and minutes // 60 == 0:
        return 0
    elif minutes % 60 > 0 and minutes // >0:
        return (minutes/60)+1
def parking_fee(minutes):
    if hours_to_pay(minutes) == 0:
        return 0
    elif hours_to_pay(minutes) == 1:
        return 5000
    elif hours_to_pay(minutes) > 1:
        return 5000 + 3000*hours_to_pay(minutes)



assert hours_to_pay(0) == 0
assert hours_to_pay(60) == 1
assert hours_to_pay(61) == 2

assert parking_fee(0) == 0
assert parking_fee(1) == 5000
assert parking_fee(60) == 5000
assert parking_fee(61) == 8000
assert parking_fee(125) == 11000







