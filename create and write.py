# Create a new text file and write some content into it.

def create_and_write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Text file '{filename}' created and content written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Content to write into the file
file_content = """This is a new text file created with Python.
It contains some sample content.
You can write anything you want here."""

# Create and write to the file
create_and_write_to_file('new_file.txt', file_content)
