#Program to display first n multiples of a number
# Program to display the first n multiples of a number

# Get input from the user
number = int(input("Enter the number: "))
n = int(input("Enter how many multiples you want to display: "))

# Display the multiples
for i in range(1, n + 1):
    print(number * i)