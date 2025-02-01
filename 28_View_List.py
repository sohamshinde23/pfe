#Program to Create and view elements of a list
# Program to create and view elements of a list

n = int(input("How many elements? "))
my_list = [input("Enter element: ") for _ in range(n)]

print("The list is:", my_list)
