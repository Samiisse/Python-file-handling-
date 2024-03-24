#Write a function that reads a JSON file and extracts specific information from it

import json

def extract_info_from_json(json_file, key):
    extracted_info = None
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            if key in data:
                extracted_info = data[key]
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

    return extracted_info

# Example usage:
json_file = input("Enter the path of the JSON file: ")
key = input("Enter the key to extract information for: ")
info = extract_info_from_json(json_file, key)
if info is not None:
    print(f"Extracted information for key '{key}': {info}")
else:
    print(f"No information found for key '{key}' in the JSON file.")
