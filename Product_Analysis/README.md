# 📊 Product Analysis Tool

> **A comprehensive Python script for analyzing product sales data with advanced filtering and statistical insights**

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![CSV Support](https://img.shields.io/badge/data-CSV-green.svg)](https://docs.python.org/3/library/csv.html)
[![Status](https://img.shields.io/badge/status-Active-success.svg)](https://github.com/midrees555/Python_Practice_Projects)

---

## 🎯 Project Overview

This project implements a robust **Product Analysis System** that processes CSV-based sales data to generate meaningful business insights. Built as part of Python OOP fundamentals, it demonstrates practical application of file handling, data processing, and error management in a real-world scenario.

### 🚀 Key Features

- **📥 Smart CSV Reading**: Intelligent parsing with automatic header cleanup
- **🔍 Advanced Filtering**: Price-based product filtering with customizable thresholds
- **📈 Statistical Analysis**: Comprehensive metrics including totals, averages, and top performers
- **💾 Flexible Output**: Results saved in human-readable format
- **🛡️ Error Handling**: Robust try/except implementation for production-ready code
- **⚡ Performance Optimized**: Efficient data processing using Python built-ins

---

## 📋 Problem Statement

**Assignment Goal**: Create a Python module that integrates core programming concepts including:
- File I/O operations with CSV data
- Data filtering and transformation
- Statistical calculations and analysis
- Error handling and edge case management
- Modular function design

---

## 🏗️ Architecture & Design

### Core Functions

| Function | Purpose | Input | Output |
|----------|---------|-------|--------|
| `read_product_records()` | CSV data ingestion | File path | List of product dictionaries |
| `filter_product()` | Price-based filtering | Products list, threshold | Filtered products |
| `products_summary()` | Statistical analysis | Products list | Summary statistics |
| `save_summary()` | Results persistence | Summary data, file path | Saved file |

### 🔄 Workflow Pipeline

```
📁 CSV File → 📊 Read Data → 🔍 Filter → 📈 Analyze → 💾 Save Results
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+**
- **CSV module** (built-in)
- Sample CSV data file

### 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/midrees555/Python_Practice_Projects.git
   cd Python_Practice_Projects/Product_Analysis
   ```

2. **Prepare your data**:
   - Place your CSV file in the `./assets/` directory
   - Ensure CSV contains columns: `name`, `price`, `quantity_sold`

### ▶️ Usage

**Basic Execution**:
```python
python product_analysis.py
```

**Custom Configuration**:
```python
# Modify threshold and file paths as needed
products = read_product_records("your_data.csv")
filtered = filter_product(products, threshold=15000)  # Custom threshold
summary = products_summary(filtered)
save_summary(summary, "custom_output.txt")
```

---

## 📊 Sample Output

**Generated Summary Statistics**:
```
total_price: 45750.50
avg_price: 9150.10
max_sold: {'name': 'Product X', 'quantity_sold': '150', 'price': '8500'}
max_profit: {'name': 'Product Y', 'quantity_sold': '100', 'price': '12000'}
```

---

## 🧪 Data Processing Logic

### 🔍 Filtering Algorithm
- **Price Threshold**: Configurable limit (default: ₹10,000)
- **Data Validation**: Automatic handling of invalid/missing price values
- **Type Safety**: Robust conversion with fallback mechanisms

### 📈 Analytics Engine
- **Total Revenue**: Sum of all product prices
- **Average Price**: Mean price calculation
- **Top Seller**: Product with highest quantity sold
- **Most Profitable**: Product with maximum (price × quantity) value

---

## 🛡️ Error Handling

| Error Type | Handling Strategy | User Impact |
|------------|-------------------|-------------|
| `FileNotFoundError` | Graceful fallback with empty list | Prevents crash, shows warning |
| `ValueError` | Skip invalid records | Continues processing valid data |
| `TypeError` | Type conversion protection | Maintains data integrity |

---

## 📁 Project Structure

```
Product_Analysis/
├── 📄 product_analysis.py    # Main analysis script
├── 📄 README.md             # This documentation
└── 📁 assets/               # Data files directory
    ├── 📊 assignment_sales.csv
    └── 📄 summary.txt
```

---

## 🔧 Technical Specifications

- **Language**: Python 3.7+
- **Dependencies**: Standard library only
- **Input Format**: CSV with headers
- **Output Format**: Text file with key-value pairs
- **Performance**: O(n) time complexity for most operations

---

## 🎓 Learning Objectives Achieved

✅ **File I/O Mastery**: CSV reading and writing operations  
✅ **Data Structures**: Lists and dictionaries manipulation  
✅ **Control Flow**: Loops, conditionals, and exception handling  
✅ **Function Design**: Modular, reusable code architecture  
✅ **Error Management**: Production-ready error handling  
✅ **Code Organization**: Clean, readable, and maintainable structure  

---

## 🔮 Future Enhancements

- [ ] **Multi-format Support**: JSON, Excel integration
- [ ] **Database Connectivity**: SQLite/PostgreSQL support
- [ ] **Visualization**: Charts and graphs generation
- [ ] **CLI Interface**: Command-line argument parsing
- [ ] **Unit Testing**: Comprehensive test suite
- [ ] **API Integration**: REST API endpoints

---

## 👨‍💻 Author

**[midrees555](https://github.com/midrees555)**  
*Python Developer & Data Enthusiast*

---

## 📄 License

This project is part of the **Python Practice Projects** collection.  
Feel free to use and modify for educational purposes.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/midrees555/Python_Practice_Projects/issues).

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

**Made with ❤️ for the Python learning community**

</div>