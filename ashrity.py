import streamlit as st
import requests
from streamlit_folium import st_folium
import folium

st.title("🌤 Weather App with Clickable Map")

API_KEY = "YOUR_API_KEY_HERE"

# Create a map (centered on USA)
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)
st.write("**Click on the map to get the weather for that location**")

# Display map and get click data
map_data = st_folium(m, width=700, height=500)

# Only run if the user clicked somewhere
if map_data is not None and map_data.get('last_clicked') is not None:
    lat = map_data['last_clicked']['lat']
    lon = map_data['last_clicked']['lng']

    # Fetch weather using coordinates
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city_name = data.get('name', 'Unknown Location')
        st.subheader(f"Weather in {city_name}")
        st.write(f"📍 Coordinates: {lat:.2f}, {lon:.2f}")
        st.write(f"🌡 Temperature: {data['main']['temp']}°C")
        st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        st.write(f"☁ Weather: {data['weather'][0]['description'].title()}")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
        
        # Weather icon
        icon = data['weather'][0]['icon']
        st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
    else:
        st.error("Weather data not found at this location.")
else:
    st.info("Click on the map to see the weather for that location.")
