#Implement a program that reads a CSV file and generates a bar chart to represent the data using Matplotlib

import csv
import matplotlib.pyplot as plt

def generate_bar_chart(csv_file):
    data = {'Labels': [], 'Values': []}
    
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        
        for row in reader:
            data['Labels'].append(row[0])  # Assuming the first column contains labels
            data['Values'].append(float(row[1]))  # Assuming the second column contains values
    
    plt.bar(data['Labels'], data['Values'])
    plt.xlabel(header[0])  # Set x-axis label
    plt.ylabel(header[1])  # Set y-axis label
    plt.title('Bar Chart')  # Set title
    plt.show()

# Example usage:
csv_file = input("Enter the path of the CSV file: ")
generate_bar_chart(csv_file)
