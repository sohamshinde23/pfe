set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", result)


# using funtion 
def symmetric_difference(set_a, set_b):
    return set_a.symmetric_difference(set_b)

# Example usage:
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

result = symmetric_difference(set_a, set_b)
print(result)