import random

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

random_number = random.randint(start, end)

print("Random number between", start, "and", end, "is", random_number)