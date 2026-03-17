# Project Background
# You are working as a Data Analyst for an e-commerce company. The company receives raw order data from multiple systems, but the data contains duplicate orders, repeated customers, and mixed product records. Your task is to clean, process, and analyze the order data using Python data structures.


orders = [
("ORD001", "C101", "Laptop", 1200),
("ORD002", "C102", "Phone", 800),
("ORD003", "C101", "Laptop", 1200),
("ORD004", "C103", "Tablet", 600),
("ORD005", "C104", "Phone", 800),
("ORD006", "C102", "Headphones", 150),
("ORD007", "C105", "Laptop", 1200),
("ORD003", "C101", "Laptop", 1200),   # duplicate order
("ORD008", "C106", "Tablet", 600),
("ORD009", "C101", "Phone", 800)
]


# Pipeline Stage 1 – Data Exploration
# Tasks:
# 1. Print all order records.
# 2. Count the total number of orders received.
# 3. Extract a list of all product names.



# 1. Print all order records
print("1) All Order Records:")
for order in orders:
    print(order)



# 2. Count the total number of orders received

for order in orders:
    cleaned_orders = set(orders)   # Remove duplicates using a set
total_orders = len(cleaned_orders)
print(f"\n2) Total number of unique orders received: {total_orders}")

# or 

# cleaned_orders = set(orders)   # Remove duplicates using a set
# total_orders = len(cleaned_orders)
# print(f"2) Total number of unique orders received: {total_orders}")



# 3. Extract a list of all product names.
product_names = set(order[2] for order in orders)  # Extract product names and remove duplicates
print(f"\n3) List of all unique product names:")
for name in product_names:
    print(name)



# Pipeline Stage 2 – Data Cleaning
# Tasks:
# 4.	1. Remove duplicate order records.
# 5.	2. Calculate the number of unique orders.
# 6.	3. Identify unique customers.

