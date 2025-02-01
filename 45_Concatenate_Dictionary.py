# Original dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Create a new dictionary by copying dict1
merged_dict = dict1.copy()

# Update the new dictionary with dict2
merged_dict.update(dict2)

print(merged_dict)
