# Create a function that takes a list of sentences and writes them to a new text file, each on a new line

def write_sentences_to_file(sentences, filename):
    try:
        with open(filename, 'w') as file:
            # Write each sentence to the file, with a newline character '\n' after each sentence
            for sentence in sentences:
                file.write(sentence + '\n')
        print(f"Sentences written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: Write a list of sentences to a file named 'sentences.txt'
sentences_list = [
    "This is the first sentence.",
    "This is the second sentence.",
    "And this is the third sentence."
]
write_sentences_to_file(sentences_list, 'sentences.txt')
