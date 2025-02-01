# Program to find perfect squares with sum of digits less than 10

# Get input range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Function to check sum of digits
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# List to store numbers that are perfect squares and have digit sum < 10
perfect_squares = []

for num in range(start, end + 1):
    if int(num**0.5)**2 == num and sum_of_digits(num) < 10:
        perfect_squares.append(num)

print("Perfect squares with sum of digits less than 10:", perfect_squares)
