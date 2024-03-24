#Given a CSV file with student names and scores, find the student with the highest score

import csv

def find_student_with_highest_score(csv_file):
    highest_score = float('-inf')  # Initialize with negative infinity to ensure any score is higher
    student_with_highest_score = None

    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_name = row['Student Name']
                score = float(row['Score'])
                if score > highest_score:
                    highest_score = score
                    student_with_highest_score = student_name

        if student_with_highest_score:
            print(f"The student with the highest score is {student_with_highest_score} with a score of {highest_score}.")
        else:
            print("No data found in the CSV file.")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: Find the student with the highest score in the CSV file "students.csv"
find_student_with_highest_score('students.csv')
