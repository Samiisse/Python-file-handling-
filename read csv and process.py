#Read a CSV file and process its data.

import csv

def create_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write the header row
            writer.writerow(['Name', 'Age', 'City'])
            # Write data rows
            for row in data:
                writer.writerow(row)
        print(f"CSV file '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example data to write to the CSV file
data = [
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

# Example usage: Create a CSV file named 'data.csv' with the provided data
create_csv('data.csv', data)
