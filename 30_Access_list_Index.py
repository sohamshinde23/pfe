# Program to access list index and value

# my_list = ['Apple', 'Banana', 'Cherry']

# for i in range(len(my_list)):
#     print("Index:", i, "Value:", my_list[i])

#user input
user_list = eval(input("Enter a list (e.g., [1, 2, 3, 'apple']): "))

# Display each index and value
print("\nIndex and value in the list:")

for index, value in enumerate(user_list):
    print(f"Index {index}: {value}")
