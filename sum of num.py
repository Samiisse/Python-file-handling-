# Given a text file with a list of numbers, write a function that finds the sum of all numbers in the file

import csv

def sum_of_numbers_in_csv(file_path):
    total_sum = 0
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                for number in row:
                    total_sum += int(number)
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Error: Unable to convert to float.")

    return total_sum

# Example usage:
file_path = input("Enter the path of the CSV file: ")
total_sum = sum_of_numbers_in_csv(file_path)
print("Sum of all numbers in the CSV file:", total_sum)
