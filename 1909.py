import calendar

def proverka_dats(day, month, year):
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    proverka_year=calendar.isleap(year)
    if 1 <= day <= 31 and month in months_31:
        return True
    if 1 <= day <= 30 and month in months_30:
        return True
    if proverka_year == True and month == 2 and 1 <= day <= 29:
        return True
    else:
        return False
print(proverka_dats(29, 2, 2020))
