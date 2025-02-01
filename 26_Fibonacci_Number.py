#Program to display first n Fibonacci numbers 
# Program to display the first n Fibonacci numbers

n = int(input("Enter how many Fibonacci numbers to display: "))

# First two Fibonacci numbers
a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
