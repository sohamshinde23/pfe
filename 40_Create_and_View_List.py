# Input the list
elements = input("Enter the elements of the list, separated by spaces: ").split()

# Display the list
print("\nThe elements of the list are:")
for index, element in enumerate(elements):
    print(f"Index {index}: {element}")
