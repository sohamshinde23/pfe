## Program to create and view elements of a tuple

n = int(input("How many elements? "))
my_tuple = tuple(input("Enter element: ") for _ in range(n))

print("The tuple is:", my_tuple)
