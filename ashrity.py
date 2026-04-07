import streamlit as st
import requests
from streamlit_folium import st_folium
import folium

st.title("🌤 Weather App with Clickable Map")

API_KEY = "YOUR_API_KEY_HERE"

# Create a map (world view)
m = folium.Map(location=[20, 0], zoom_start=2)
st.write("**Click anywhere on the map to see the weather**")

# Display the map
map_result = st_folium(m, width=700, height=500)

# Check if user clicked
if map_result is not None:
    last_clicked = map_result.get('last_clicked')
    if last_clicked is not None:
        lat = last_clicked['lat']
        lon = last_clicked['lng']

        # Fetch weather for clicked coordinates
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
            icon = data['weather'][0]['icon']
            st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
        else:
            st.error("Weather data not found at this location.")
    else:
        st.info("Click on the map to see the weather!")
else:
    st.info("Loading map…")
