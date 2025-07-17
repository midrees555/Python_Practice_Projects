# 📘 Assignment 1:
# Build a Script That Integrates all the topics, thet covered in '2_Python_OOP\01_Basics\Day_01_Variables_Classes\Tasks\1_data_list_processing.py'

# Problem Statement: Create a Python module/script that:
# Reads product records from a CSV file
# Filters products based on price threshold
# Calculates total and average price
# Saves the results to a new file (output.txt or summary.csv)
# Structure your code into functions, and use try/except for errors.

# ✅ Save this as product_analysis.py.
# ✅ Use version control: git init, git add ., git commit -m "Day 1 assignment"
# ----------------------------------------------------------------------------

# import essential packages
import csv

def read_product_records(file_path):
    """Reading product records from file at 'file_path'"""
    
    try:
        with open(file_path, 'r') as file:
            # Clean up headers by stripping whitespace & trailing commas
            reader = csv.DictReader(file)
            return [
                {k.strip(): v.strip()
                 for k, v in row.items()
                 if k is not None}
                for row in reader
            ]
    except FileNotFoundError:
        print(f"Error: file {file_path} not found!\n")
        return []                                   # Return empty list to avoid crashes later
    
    
def filter_product(items, threshold=10000):
    """Key Action: Filter products where price (as float) ≤ threshold.
    Edge Case: Handle missing/incorrect price values."""
    
    filtered = []
    
    for item in items:
        try:
            if float(item.get("price", 0)) <= threshold:
                filtered.append(item)
        except (ValueError, TypeError):
            continue        # skip invalid prices
    
    return filtered


def products_summary(products):
    """Stats to Compute:
    Total/Average price (use sum() and len()).
    Max sold product (track quantity_sold).
    Max profit product (calculate price * quantity_sold)"""
    
    if not products:
        return None     # Handle empty data
    
    prices = [float(p["price"]) for p in products]
    total, avg = sum(prices), sum(prices) / len(prices)
    
    max_sold = max(products, key=lambda p: int(p["quantity_sold"]))
    max_profit = max(products, key=lambda p: float(p["price"]) * int(p["quantity_sold"]))
    
    return {
        "total_price": total,
        "avg_price": avg,
        "max_sold": max_sold,
        "max_profit": max_profit
    }


def save_summary(summary, output_file="./assets/summary.txt"):
    """Save to output.txt (human-readable) or summary.csv (structured)."""
    
    with open(output_file, 'w') as file:
        for key, value in summary.items():
            file.write(f"{key}: {value}\n")     # Write each state as a line
            
    print(f"\nAnalyze Data Saved Successfully!\nFile Path: '{output_file}'")
    print("--------------------------------\n")
            
            
# Main workflow
# Read --> Filter --> Analyze --> Save
products = read_product_records("./assets/assignment_sales.csv")
filtered = filter_product(products, threshold=10000)
summary = products_summary(filtered)
save_summary(summary, "./assets/summary.txt")