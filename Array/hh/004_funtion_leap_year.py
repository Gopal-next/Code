def leap_year(year):
    if year %4 ==0:
        if year %100 ==0:
            if year %400 ==0:
                return True
            else:
                return False
        else:
            return True
    
print(leap_year(2020))  # Output: True
print(leap_year(1900))  # Output: False
print(leap_year(2000))  # Output: True