import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎓 Student Performance Dashboard")

# -------------------------------
# Student Information
# -------------------------------

st.header("Student Information")

st.write("**Student Name:** Rahul Sharma")
st.write("**Roll Number:** 22A91A0501")
st.write("**Class:** III B.Tech - CSE")

# -------------------------------
# KPI Cards
# -------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Marks", "540")
col2.metric("Percentage", "90%")
col3.metric("Attendance", "95%")
col4.metric("Rank", "3")

st.divider()

# -------------------------------
# Subject-wise Marks
# -------------------------------

marks = pd.DataFrame({
    "Subject":["Python","DBMS","Java","OS","CN","AI"],
    "Marks":[95,90,88,85,92,90]
})

st.subheader("Subject-wise Marks (Bar Chart)")

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(marks["Subject"], marks["Marks"])

ax.set_xlabel("Subjects")
ax.set_ylabel("Marks")

st.pyplot(fig)

st.divider()

# -------------------------------
# Pie Chart
# -------------------------------

st.subheader("Marks Distribution (Pie Chart)")

fig, ax = plt.subplots(figsize=(6,6))

ax.pie(
    marks["Marks"],
    labels=marks["Subject"],
    autopct="%1.1f%%",
    startangle=90
)

st.pyplot(fig)

st.divider()

# -------------------------------
# Attendance Trend
# -------------------------------

attendance = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May"],
    "Attendance":[92,94,95,96,95]
})

st.subheader("Attendance Trend (Line Chart)")

fig, ax = plt.subplots(figsize=(7,4))

ax.plot(attendance["Month"],attendance["Attendance"],marker='o')

ax.set_ylabel("Attendance %")

st.pyplot(fig)

st.divider()

# -------------------------------
# Student Details
# -------------------------------

st.header("Student Details")

details = pd.DataFrame({
    "Field":["Father Name","Phone","Email","Address"],
    "Details":["Ramesh Sharma","9876543210","rahul@gmail.com","Hyderabad"]
})

st.table(details)