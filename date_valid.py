from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")  # Default format: YYYY-MM-DD
        return True
    except ValueError:
        return False

# Input and output
date = input("Enter a date (YYYY-MM-DD): ")

if is_valid_date(date):
    print("The date is valid.")
else:
    print("The date is invalid.")
