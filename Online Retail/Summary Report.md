# Online Retail Sales Analysis

This project analyzes transaction-level retail data to uncover trends in monthly revenue and identify the most profitable product categories.

## Dataset

**File:** `Online Retail.csv`  
Contains transaction data of an e-commerce store (likely sourced from the UCI Machine Learning Repository).

## Key Insights

### 1. Monthly Sales Trend

- Revenue showed a significant increase over time, with peak sales observed in **November and December 2011**.
- A consistent upward trend indicates growing customer engagement or seasonal effects.

**Visualization:**  
Bar chart displaying total monthly revenue from December 2010 to December 2011.

### 2. Top-Selling Products by Revenue

- The most profitable product is **"PAPER CRAFT , LITTLE BIRDIE"**, followed by **"REGENCY CAKESTAND 3 TIER"** and **"WHITE HANGING HEART T-LIGHT HOLDER"**.
- These products contributed significantly to the company’s total revenue.

**Visualization:**  
Horizontal bar chart of the top 10 product categories by total revenue.

## Tools Used

- **Pandas**: For data cleaning, aggregation, and transformation
- **Matplotlib & Seaborn**: For creating visualizations and applying styles
- **Datetime Handling**: Used `pd.to_datetime()` and Period features for time-based grouping

## Data Cleaning Steps

- Removed missing entries using `dropna()`
- Filtered out transactions with non-positive quantity or unit price

## Feature Engineering

- Created a new column:  
  `TotalPrice = Quantity × UnitPrice`
- Extracted the month from the invoice date to enable monthly aggregation

---

This project provides a clear understanding of sales trends and helps identify high-performing products using effective data visualization and analysis techniques.
