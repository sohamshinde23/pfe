# Function to check if key exists in the dictionary
def check_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

# Example dictionary
my_dict = {"a": 1, "b": 2, "c": 3}

# Input key to check
key = input("Enter the key to check: ")

# Check if key exists and print result
if check_key(my_dict, key):
    print(f"Key '{key}' exists in the dictionary.")
else:
    print(f"Key '{key}' does not exist in the dictionary.")
