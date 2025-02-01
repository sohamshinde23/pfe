#Write a Python program that reads the content of one text file and writes it to another file
def copy_file_content(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)
        print(f"Content successfully copied from '{source_file}' to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")
copy_file_content(source_file, destination_file)
