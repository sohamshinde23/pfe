#Program to calculate sum and average of first n numbers 
# Program to calculate the sum and average of first n numbers

# Get input from the user
n = int(input("Enter a positive integer (n): "))

# Calculate sum of the first n numbers
sum_of_numbers = n * (n + 1) // 2

# Calculate average
average = sum_of_numbers / n

# Display results
print(f"The sum of the first {n} numbers is: {sum_of_numbers}")
print(f"The average of the first {n} numbers is: {average:.2f}")
