#Write a Python program that reads the content of a text file and prints it to the console. 

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = input("Enter the filename: ")
read_file(file_name)