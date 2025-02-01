# Function to read and print the sequence in reverse order using recursion
def print_reverse():
    # Get the user input
    num = int(input())
    
    # Base case: if the number is 00, stop the recursion
    if num == 0:
        return
    
    # Recursive case: print the number after the recursion call
    print_reverse()
    
    # Print the current number after the recursive call
    print(num)

# Calling the function to initiate the process
print_reverse()
