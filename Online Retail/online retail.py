# libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# plot style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load dataset
df = pd.read_csv(r"C:\Users\LOKESHRAJ M\codmetric\Online Retail\Online Retail.csv")

# Data cleaning
df.dropna(inplace=True)  # Removes missing values
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]  # Removes negative/zero quantity/price

# Add useful columns
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True)  
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']  # Revenue per row
df['Month'] = df['InvoiceDate'].dt.to_period('M')  # Extract month-year

# Sales Trend Over Time (Bar Chart)
monthly_sales = df.groupby('Month')['TotalPrice'].sum()
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 Product Categories (Bar Chart)
top_products = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='barh', color='orange')
plt.title('Top 10 Product Categories by Revenue')
plt.xlabel('Revenue')
plt.tight_layout()
plt.show()
