# Sample dictionary
fruits = {'apple': 3, 'banana': 1, 'cherry': 2}

# Sort dictionary by value in ascending order
sorted_fruits_asc = dict(sorted(fruits.items(), key=lambda item: item[1]))
print("Ascending:", sorted_fruits_asc)

# Sort dictionary by value in descending order
sorted_fruits_desc = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_fruits_desc)
