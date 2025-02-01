def find_maximum(a, b):
    if a > b:
        return a
    else:
        return b

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The maximum of {num1} and {num2} is {find_maximum(num1, num2)}.")

