import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

st.title("🌍 Worldwide Weather App")

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key

# Sidebar: type a city
city_input = st.sidebar.text_input("Enter city name (optional):")

# Create a world map
m = folium.Map(location=[20, 0], zoom_start=2)

# If the user clicks on the map
map_result = st_folium(m, width=700, height=500)

lat, lon = None, None

# Check for map click
if map_result is not None and map_result.get('last_clicked') is not None:
    lat = map_result['last_clicked']['lat']
    lon = map_result['last_clicked']['lng']

# If user typed a city, try to get coordinates from city name
if city_input:
    # Add US default if user types only a city (optional)
    if "," not in city_input:
        city_input += ", US"
    try:
        url_city = f"http://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={API_KEY}&units=metric"
        response_city = requests.get(url_city)
        if response_city.status_code == 200:
            data_city = response_city.json()
            lat = data_city['coord']['lat']
            lon = data_city['coord']['lon']
        else:
            st.warning("City not found. Using map click location instead (if clicked).")
    except:
        st.warning("Error fetching city data. Using map click location instead (if clicked).")

# If we have coordinates (from map click or city), fetch weather
if lat is not None and lon is not None:
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

        # Show map centered on weather location
        m_weather = folium.Map(location=[lat, lon], zoom_start=6)
        folium.Marker([lat, lon], popup=city_name).add_to(m_weather)
        st_folium(m_weather, width=700, height=500)
    else:
        st.error("Weather data not found at this location.")
else:
    st.info("Click on the map or type a city name to see the weather!")
