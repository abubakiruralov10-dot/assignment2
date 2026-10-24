def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(month, year):
    
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
   
    elif month in {4, 6, 9, 11}:
        return 30

    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 0  
        
def is_valid_date(day, month, year):
    if year>0 and 1 <= month <= 12 and  month in {1, 3, 5, 7, 8, 10, 12} and 1 <= day <= 31:
        return True
    elif year>0 and 1 <= month <= 12 and  month in {4, 6, 9, 11} and 1 <= day <= 30:
        return True
    elif year>0 and month == 2 and  1 <= day <= 29 and is_leap_year(year) == True:
        return True
    elif  year>0 and month == 2 and  1 <= day <= 28 and is_leap_year(year) == False:
        return True
    else:
        return False


assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert days_in_month(2, 2024) == 29
assert days_in_month(4, 2026) == 30

assert is_valid_date(29, 2, 2024) == True
assert is_valid_date(29, 2, 2026) == False
assert is_valid_date(31, 4, 2026) == False
assert is_valid_date(0, 1, 2026) == False
assert is_valid_date(15, 13, 2026) == False
assert is_valid_date(1, 1, 0) == False
