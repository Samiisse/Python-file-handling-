#Write a program that reads a CSV file and finds the total sales revenue for a specific product

import csv

def calculate_total_revenue(csv_file, product_name):
    total_revenue = 0
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        product_index = header.index('Product')
        revenue_index = header.index('Revenue')
        
        for row in reader:
            if row[product_index].strip().lower() == product_name.strip().lower():
                total_revenue += float(row[revenue_index])
    
    return total_revenue

def main():
    csv_file = input("Enter the path of the CSV file: ")
    product_name = input("Enter the product name to calculate total revenue for: ")
    total_revenue = calculate_total_revenue(csv_file, product_name)
    print(f"Total revenue for {product_name}: ${total_revenue:.2f}")

if __name__ == "__main__":
    main()
