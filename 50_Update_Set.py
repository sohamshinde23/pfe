# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Update the first set with items that don't exist in the second set
set1.difference_update(set2)

# Display the updated first set
print("Updated Set 1:", set1)