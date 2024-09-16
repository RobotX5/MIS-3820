import csv
import random

# Define the file name
file_name = 'Generated_customer_behavior.csv'

# Define the headers
headers = ['Age', 'Income', 'Category', 'Number_of_Purchases', 'Target', 'Continuous_Target']

# Generate sample data
data = []
for _ in range(1000):
    age = random.randint(18, 70)
    income = round(random.uniform(20000, 150000), 2)
    category = random.choice(['A', 'B', 'C', 'D'])
    number_of_purchases = random.randint(1, 50)
    target = random.choice([0, 1])
    continuous_target = round(random.uniform(0, 1), 2)
    data.append([age, income, category, number_of_purchases, target, continuous_target])

# Write data to CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Data successfully written to {file_name}")