# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Input: Range (start and end)
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Display all perfect squares in the range where sum of digits < 10
for num in range(start, end + 1):
    # Check if the number is a perfect square
    if int(num**0.5) == num**0.5:
        # Check if the sum of digits is less than 10
        if sum_of_digits(num) < 10:
            print(num)
