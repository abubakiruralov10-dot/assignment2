def alarm_message(hour,is_weekend):
    if is_weekend:
        return "Sleep in"
    elif hour >= 7:
        return "Get up"
    else:
        return "Too early"

assert alarm_message(6, False) == "Too early"
assert alarm_message(7, False) == "Get up"
assert alarm_message(9, False) == "Get up"
assert alarm_message(6, True) == "Sleep in"
assert alarm_message(9, True) == "Sleep in"
