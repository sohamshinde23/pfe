# def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)

        with open(output_file, 'w') as file:
            file.write(f"The file '{input_file}' contains {word_count} words.\n")

        print(f"Word count has been written to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")
count_words_in_file(input_file, output_file)
