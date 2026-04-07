import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

st.title("🌍 Worldwide Weather App")

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

# Sidebar: type a city
city_input = st.sidebar.text_input("Enter city (e.g., Dallas, US)")

lat, lon = None, None
city_name = None

# Step 1: Get coordinates from typed city using OpenWeatherMap Geocoding API
if city_input:
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_input}&limit=1&appid={API_KEY}"
    geo_resp = requests.get(geo_url).json()
    if geo_resp:
        lat = geo_resp[0]['lat']
        lon = geo_resp[0]['lon']
        city_name = geo_resp[0]['name'] + ", " + geo_resp[0]['country']
    else:
        st.warning("City not found. Try 'City, CountryCode' (e.g., Dallas, US).")

# Step 2: Display world map and allow click for coordinates
m = folium.Map(location=[20, 0], zoom_start=2)
map_data = st_folium(m, width=700, height=500)

# If no city typed, use clicked coordinates
if lat is None and map_data and map_data.get('last_clicked'):
    lat = map_data['last_clicked']['lat']
    lon = map_data['last_clicked']['lng']
    city_name = f"Lat {lat:.2f}, Lon {lon:.2f}"

# Step 3: Fetch weather
if lat and lon:
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    weather_resp = requests.get(weather_url).json()
    if weather_resp.get('main'):
        st.subheader(f"Weather in {city_name}")
        st.write(f"🌡 Temperature: {weather_resp['main']['temp']}°C")
        st.write(f"💨 Wind Speed: {weather_resp['wind']['speed']} m/s")
        st.write(f"☁ Weather: {weather_resp['weather'][0]['description'].title()}")
        st.write(f"💧 Humidity: {weather_resp['main']['humidity']}%")
        icon = weather_resp['weather'][0]['icon']
        st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
    else:
        st.error("Weather data not found for this location.")
else:
    st.info("Type a city in the sidebar or click on the map to see weather.")
