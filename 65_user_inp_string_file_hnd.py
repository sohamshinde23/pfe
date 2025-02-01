# Create a Python program that takes user input (a string) and writes it to a new text file
def write_to_file(file_name, user_input):
    try:
        with open(file_name, "w") as file:
            file.write(user_input)
        print(f"Content successfully written to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = input("Enter the filename: ")
user_input = input("Enter the content to write to the file: ")
write_to_file(file_name, user_input)
