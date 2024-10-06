# -*- coding: utf-8 -*-
"""dashboard

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jLkMBqEcYu9kGdH7GQN7AHa24ml_MEOH
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('dashboard/main_data.csv')

# Title and description
st.title('E-commerce Dashboard')
st.write('Overview of sales, shipping, and product category breakdown.')

# Convert shipping_limit_date to datetime
data['shipping_limit_date'] = pd.to_datetime(data['shipping_limit_date'])

# 1. Top Product Categories
st.header('Top Product Categories by Number of Orders')
category_counts = data['product_category_name'].value_counts().head(10)
st.bar_chart(category_counts)

# 2. Revenue by Product Category
st.header('Revenue by Product Category')
revenue_by_category = data.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(10)
st.bar_chart(revenue_by_category)

# 3. Shipping Cost vs. Product Price
st.header('Shipping Cost vs. Product Price')
fig, ax = plt.subplots()
ax.scatter(data['price'], data['freight_value'], alpha=0.5)
ax.set_xlabel('Product Price')
ax.set_ylabel('Freight Value (Shipping Cost)')
ax.set_title('Shipping Cost vs Product Price')
st.pyplot(fig)

# 4. Order Frequency Over Time
st.header('Order Frequency Over Time')
order_freq = data.set_index('shipping_limit_date').resample('M')['order_id'].count()
st.line_chart(order_freq)

# 5. Top Sellers by Number of Products Sold
st.header('Top Sellers by Number of Products Sold')
top_sellers = data['seller_id'].value_counts().head(10)
st.bar_chart(top_sellers)

st.write("This dashboard analyzes customer purchasing behavior, providing insights into popular product categories, revenue generation, and shipping cost patterns.")
