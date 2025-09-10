# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/sales_data.csv', sep='\t')
data.columns = data.columns.str.strip()
# ...existing code...

data.columns = data.columns.str.strip()  # <-- Add this line
# ...existing code...

# Preview dataset
print(data.head())

# Sales trend of each product
plt.figure(figsize=(10,6))
sns.lineplot(data=data, x='Month', y='Sales', hue='Product', marker='o')
plt.title('Monthly Sales Trend of Products')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend(title='Product')
plt.tight_layout()
plt.show()

# Total sales per product
total_sales = data.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print("\nTotal Sales per Product:\n", total_sales)

# Bar plot of total sales
plt.figure(figsize=(8,5))
sns.barplot(x=total_sales.index, y=total_sales.values, palette='viridis')
plt.title('Total Sales of Each Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()
# ...existing code...

# ...existing code...

# Summary statistics for sales
print("\nSummary Statistics for Sales:\n", data['Sales'].describe())

# Monthly total sales
monthly_sales = data.groupby('Month')['Sales'].sum()
print("\nTotal Sales by Month:\n", monthly_sales)

# Best month for sales
best_month = monthly_sales.idxmax()
print(f"\nBest Month for Sales: {best_month} ({monthly_sales.max()} units)")

# Best-selling product
best_product = total_sales.idxmax()
print(f"Best-Selling Product: {best_product} ({total_sales.max()} units)")

# Sales share by product (percentage)
sales_share = (total_sales / total_sales.sum() * 100).round(2)
print("\nSales Share by Product (%):\n", sales_share)

# Pie chart of product sales share
plt.figure(figsize=(7,7))
plt.pie(sales_share, labels=sales_share.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', n_colors=len(sales_share)))
plt.title('Sales Share by Product')
plt.tight_layout()
plt.show()

# Save plots as images (optional)
import os
os.makedirs('output', exist_ok=True)

# Monthly sales trend plot
plt.figure(figsize=(10,6))
sns.lineplot(data=data, x='Month', y='Sales', hue='Product', marker='o')
plt.title('Monthly Sales Trend of Products')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend(title='Product')
plt.tight_layout()
plt.savefig('output/monthly_sales_trend.png')
plt.close()

# Total sales per product bar plot
plt.figure(figsize=(8,5))
sns.barplot(x=total_sales.index, y=total_sales.values, palette='viridis')
plt.title('Total Sales of Each Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('output/total_sales_per_product.png')
plt.close()

# Pie chart of product sales share
plt.figure(figsize=(7,7))
plt.pie(sales_share, labels=sales_share.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', n_colors=len(sales_share)))
plt.title('Sales Share by Product')
plt.tight_layout()
plt.savefig('output/sales_share_pie_chart.png')
plt.close()

print("\nPlots saved in the 'output' folder.")# Remove or comment out this block:
# ...existing code...

# Monthly sales growth rate
monthly_growth = monthly_sales.pct_change().fillna(0) * 100
print("\nMonthly Sales Growth Rate (%):\n", monthly_growth.round(2))

# Plot monthly growth rate
plt.figure(figsize=(10,5))
sns.barplot(x=monthly_growth.index, y=monthly_growth.values, palette='crest')
plt.title('Monthly Sales Growth Rate (%)')
plt.xlabel('Month')
plt.ylabel('Growth Rate (%)')
plt.tight_layout()
plt.savefig('output/monthly_growth_rate.png')
plt.close()

# ...existing code.# plt.figure(figsize=(6,4))
# sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
# plt.title('Correlation Heatmap')
# plt.tight_layout()
# plt.savefig('output/correlation_heatmap.png')
# plt.show()

# ...existing code..
