# Sample set
my_set = {1, 2, 3}

# List of elements to add
my_list = [4, 5, 6]

# Add elements from the list to the set
my_set.update(my_list)

print(my_set)

#user input
# Take set input from the user
user_set = eval(input("Enter a set (e.g., {1, 2, 3}): "))

# Take list input from the user
user_list = eval(input("Enter a list (e.g., [4, 5, 6]): "))

# Add elements from the list to the set
user_set.update(user_list)

# Print the updated set
print("\nUpdated set:")
print(user_set)

