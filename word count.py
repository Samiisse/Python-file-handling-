#Implement a program that reads a text file and counts the number of words and lines in it

def count_words_and_lines(filename):
    try:
        with open(filename, 'r') as file:
            # Read the contents of the file
            contents = file.read()
            
            # Count the number of words (assuming words are separated by whitespace)
            word_count = len(contents.split())
            
            # Count the number of lines
            line_count = contents.count('\n') + 1  # Add 1 for the last line
            
            # Print the results
            print(f"Number of words: {word_count}")
            print(f"Number of lines: {line_count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: Count the number of words and lines in the text file "example.txt"
count_words_and_lines('new_file.txt')
