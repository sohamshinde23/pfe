# Initialize variables
max_length = 0
current_length = 1

# Input: Sequence of numbers ending with 0
prev_num = int(input("Enter a number: "))

while prev_num != 0:
    # Read next number
    num = int(input("Enter a number: "))
    
    if num == prev_num:
        current_length += 1  # Increment length for consecutive numbers
    else:
        max_length = max(max_length, current_length)  # Update the maximum length
        current_length = 1  # Reset the count for the new number
    
    prev_num = num

# In case the longest fragment ends at the last number before 0
max_length = max(max_length, current_length)

print("Length of the widest fragment:", max_length)