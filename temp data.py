#Given a CSV file with temperature data for each day of the week, find the average temperature for each day.

import csv

def calculate_average_temperatures(csv_file):
    average_temperatures = {}

    # Initialize dictionary to store total temperature and count for each day
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        average_temperatures[day] = {'total_temperature': 0, 'count': 0}

    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for day in average_temperatures:
                    if day.lower() in row:
                        temperature = float(row[day.lower()])
                        average_temperatures[day]['total_temperature'] += temperature
                        average_temperatures[day]['count'] += 1

        # Calculate average temperature for each day
        for day in average_temperatures:
            if average_temperatures[day]['count'] > 0:
                average_temperatures[day]['average_temperature'] = (
                    average_temperatures[day]['total_temperature'] /
                    average_temperatures[day]['count']
                )
            else:
                average_temperatures[day]['average_temperature'] = None

    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Error: Unable to convert temperature to float.")

    return average_temperatures

# Example usage:
csv_file = input("Enter the path of the CSV file: ")
average_temperatures = calculate_average_temperatures(csv_file)
for day, data in average_temperatures.items():
    if data['average_temperature'] is not None:
        print(f"Average temperature for {day}: {data['average_temperature']:.2f} °C")
    else:
        print(f"No temperature data available for {day}")
