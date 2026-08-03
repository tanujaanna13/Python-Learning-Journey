import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 ABC Store Sales Dashboard")

# -------------------------------
# Store Information
# -------------------------------

st.header("Store Information")

st.write("**Store Name:** ABC Store")
st.write("**Location:** Bengaluru")
st.write("**Year:** 2026")

# -------------------------------
# KPI Cards
# -------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales","₹15,00,000")
col2.metric("Profit","₹3,50,000")
col3.metric("Orders","1200")
col4.metric("Customers","850")

st.divider()

# -------------------------------
# Monthly Sales
# -------------------------------

sales = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales":[200000,250000,180000,300000,270000,300000]
})

st.subheader("Monthly Sales (Line Chart)")

fig, ax = plt.subplots(figsize=(7,4))

ax.plot(sales["Month"],sales["Sales"],marker='o')

ax.set_ylabel("Sales")

st.pyplot(fig)

st.divider()

# -------------------------------
# Product Sales
# -------------------------------

product = pd.DataFrame({
    "Product":["Laptop","Mobile","Keyboard","Mouse","Printer"],
    "Sales":[120,200,150,180,70]
})

st.subheader("Product Sales (Bar Chart)")

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(product["Product"],product["Sales"])

ax.set_ylabel("Units Sold")

st.pyplot(fig)

st.divider()

# -------------------------------
# Category Sales
# -------------------------------

category = pd.DataFrame({
    "Category":["Electronics","Accessories","Office"],
    "Sales":[800000,400000,300000]
})

st.subheader("Category Sales (Pie Chart)")

fig, ax = plt.subplots(figsize=(6,6))

ax.pie(
    category["Sales"],
    labels=category["Category"],
    autopct="%1.1f%%",
    startangle=90
)

st.pyplot(fig)

st.divider()

# -------------------------------
# Top Selling Products
# -------------------------------

st.header("Top Selling Products")

table = pd.DataFrame({
    "Product":["Mobile","Laptop","Mouse","Keyboard","Printer"],
    "Units Sold":[200,120,180,150,70]
})

st.table(table)