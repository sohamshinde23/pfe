def append_to_file(filename):
    user_input = input("Enter the text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(user_input + '\n')
    print(f"The text has been appended to {filename}.")

# Example usage
filename = 'example.txt'  # Replace with your file name
append_to_file(filename)
