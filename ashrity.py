import streamlit as st
import pandas as pd

st.title("🌍 Worldwide Weather App")

# Use a raw CSV hosted online (direct link)
csv_url = "https://raw.githubusercontent.com/datasets/world-cities/master/data/world-cities.csv"

# Try to load the CSV
try:
    cities = pd.read_csv(csv_url)
    st.success("Cities loaded successfully!")
    st.write(cities.head())  # test if loaded
except Exception as e:
    st.error(f"Failed to load cities CSV: {e}")
