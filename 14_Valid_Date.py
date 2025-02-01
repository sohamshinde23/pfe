def is_valid_date(day, month, year):
    # Check if month is between 1 and 12
    if month < 1 or month > 12:
        return False
    
    # Days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust February for leap years
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    
    # Check if the day is valid for the given month
    if day < 1 or day > days_in_month[month - 1]:
        return False
    
    return True

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))


if is_valid_date(day, month, year):
    print("Valid date")
else:
    print("Invalid date")