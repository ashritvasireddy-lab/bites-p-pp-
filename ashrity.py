import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium

st.title("🌍 Worldwide Weather App with City List")

API_KEY = "YOUR_API_KEY_HERE"

# Load cities CSV (city, country, lat, lon)
cities = pd.read_csv("worldcities.csv")  # download from simplemaps.com

# Sidebar: select city
city_selected = st.sidebar.selectbox("Select a city", cities['city'] + ", " + cities['country'])

# Get lat/lon for the selected city
city_row = cities[cities['city'] + ", " + cities['country'] == city_selected].iloc[0]
lat, lon = city_row['lat'], city_row['lng']

# Fetch weather
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    st.subheader(f"Weather in {data.get('name', city_selected)}")
    st.write(f"🌡 Temperature: {data['main']['temp']}°C")
    st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    st.write(f"☁ Weather: {data['weather'][0]['description'].title()}")
    st.write(f"💧 Humidity: {data['main']['humidity']}%")
    icon = data['weather'][0]['icon']
    st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
else:
    st.error("Weather data not found.")

# Map centered on the city
m = folium.Map(location=[lat, lon], zoom_start=6)
folium.Marker([lat, lon], popup=city_selected).add_to(m)
st_folium(m, width=700, height=500)
