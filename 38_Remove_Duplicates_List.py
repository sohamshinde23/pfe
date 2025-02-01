# Program to remove duplicate items from a list

my_list = [1, 2, 3, 2, 4, 1, 5, 6]

# Remove duplicates by converting to a set and back to a list
unique_list = list(set(my_list))

print("List without duplicates:", unique_list)
