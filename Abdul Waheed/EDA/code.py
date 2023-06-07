import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from matplotlib import pyplot as plt

data = pd.read_csv('C:\\Users\\Mega Computers\\Desktop\EDA\\sales_data.csv')

# Display the first few rows of the dataset
print(data.head())
# Check the dimensions of the dataset
print("Dimensions of the dataset:", data.shape)

# Check the data types of each column
print("Data types of each column:\n", data.dtypes)

# Calculate summary statistics of numerical columns
print("Summary statistics:\n", data.describe())

# Check for missing values
print("Missing values:\n", data.isnull().sum())

# Calculate total sales
total_sales = data['Revenue'].sum()
print("Total sales:", total_sales)

# Calculate average sales
average_sales = data['Revenue'].mean()
print("Average sales:", average_sales)

# Calculate maximum and minimum sales
max_sales = data['Revenue'].max()
min_sales = data['Revenue'].min()
print("Maximum sales:", max_sales)
print("Minimum sales:", min_sales)

# Visualize sales distribution
fig = px.histogram(data, x='Revenue', nbins=10, title='Sales Distribution')
fig.update_layout(xaxis_title='Sales', yaxis_title='Frequency')
fig.show()

# Create a bar plot to show sales by product category
sales_by_category = data.groupby('Product')['Revenue'].sum().reset_index()
fig = px.bar(sales_by_category, x='Product', y='Revenue', title='Sales by Category')
fig.update_layout(xaxis_title='Product', yaxis_title='Revenue')
fig.show()

# Create a line plot to show sales trend over time
data['Date'] = pd.to_datetime(data['Date'])
sales_over_time = data.groupby('Date')['Revenue'].sum().reset_index()
fig = px.line(sales_over_time, x='Date', y='Revenue', title='Sales Trend over Time')
fig.update_layout(xaxis_title='Sales', yaxis_title='date')
fig.show()

# Create a scatter plot to visualize the relationship between unit sold and Revenue
fig = px.scatter(data, x='Units Sold', y='Revenue', title='Price vs. Sales')
fig.update_layout(xaxis_title='unit sold', yaxis_title='Sales')
fig.show()

# Create a box plot to show the distribution of product by Revenue
fig = px.box(data, x='Product', y='Revenue', title='Sales Distribution by Region')
fig.update_layout(xaxis_title='Product', yaxis_title='Sales')
fig.show()
