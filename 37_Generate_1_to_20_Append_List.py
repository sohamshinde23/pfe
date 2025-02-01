import random

# List to store random numbers
random_numbers = []

# Generate 10 random numbers from 1 to 20 and append to the list
for _ in range(10):  # You can change 10 to any number of random numbers you want
    random_numbers.append(random.randint(1, 20))

# Display the list of random numbers
print("Random numbers:", random_numbers)