import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

st.title("🌤 Weather App with City List")

API_KEY = "YOUR_API_KEY_HERE"

# Sidebar for city selection
cities = {
    "New York, US": (40.7128, -74.0060),
    "Los Angeles, US": (34.0522, -118.2437),
    "Dallas, US": (32.7767, -96.7970),
    "London, UK": (51.5074, -0.1278),
    "Tokyo, JP": (35.6762, 139.6503),
    "Sydney, AU": (-33.8688, 151.2093)
}

selected_city = st.sidebar.selectbox("Select a city", list(cities.keys()))
lat, lon = cities[selected_city]

# Fetch weather
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    st.subheader(f"Weather in {selected_city}")
    st.write(f"🌡 Temperature: {data['main']['temp']}°C")
    st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    st.write(f"☁ Weather: {data['weather'][0]['description'].title()}")
    st.write(f"💧 Humidity: {data['main']['humidity']}%")
    icon = data['weather'][0]['icon']
    st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
else:
    st.error("Weather data not found.")

# Display map centered on selected city
m = folium.Map(location=[lat, lon], zoom_start=10)
folium.Marker([lat, lon], popup=selected_city).add_to(m)
st_folium(m, width=700, height=500)
