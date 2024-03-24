#Given a CSV file with employee details (name, age, salary), calculate the average salary of all employees2

import csv

def calculate_average_salary(csv_file):
    total_salary = 0
    num_employees = 0

    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                salary = float(row['Salary'])
                total_salary += salary
                num_employees += 1

        if num_employees > 0:
            average_salary = total_salary / num_employees
            print(f"The average salary of all employees is: {average_salary:.2f}")
        else:
            print("No data found in the CSV file.")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: Calculate the average salary of employees from the CSV file "employees.csv"
calculate_average_salary('employees.csv')

