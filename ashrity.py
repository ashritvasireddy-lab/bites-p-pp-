import streamlit as st
import pandas as pd

st.title("🌍 Worldwide Weather App")

# Working CSV with lat/lng (hosted on GitHub)
csv_url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/cities.csv"

try:
    cities = pd.read_csv(csv_url)
    # Keep only necessary columns
    cities = cities[['name', 'country_name', 'latitude', 'longitude']]
    cities.columns = ['city', 'country', 'lat', 'lng']
    st.success("Cities loaded successfully!")
    st.write(cities.head())
except Exception as e:
    st.error(f"Failed to load cities CSV: {e}")
