#Write a Python program to copy the contents of one text file into another

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                # Read the contents of the source file
                contents = source.read()
                # Write the contents to the destination file
                destination.write(contents)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: Copy the contents of 'source.txt' to 'destination.txt'
copy_file('source.txt', 'destination.txt')

