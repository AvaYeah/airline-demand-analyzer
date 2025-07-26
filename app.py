import os
os.environ["STREAMLIT_WATCH_USE_POLLING"] = "true"

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Airline Demand Analyzer", layout="wide")

st.title("✈️ Airline Demand Analyzer")

st.markdown("""
Welcome to the **Airline Demand Analyzer** web app!

This app is built using **Streamlit** and **Pandas**, and will help you:
- Understand booking trends
- Visualize data
- Make data-driven decisions
""")

# Placeholder for future data
st.info("🧠 Stay tuned — data will appear here once added!")

st.info("🧠 Stay tuned – data will appear here once added!")
# ---- Sample Airline Booking Demand Data ----
sample_data = {
    "City": ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata"],
    "Bookings": [230, 180, 90, 150, 70],
    "Price (INR)": [5000, 4800, 4500, 4600, 4300]
}

df = pd.DataFrame(sample_data)

# ---- Display the data ----
st.subheader("📊 Booking Data Overview")
st.dataframe(df)

# ---- Visualize the data ----
st.subheader("📈 Booking Trends")
st.bar_chart(df.set_index("City")["Bookings"])
