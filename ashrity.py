import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

st.title("🌍 World Weather App")

API_KEY = "YOUR_API_KEY_HERE"

# Search box for any city
city_input = st.sidebar.text_input("Enter city name (e.g., Dallas, US)")

if city_input:
    # Fetch weather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        st.subheader(f"Weather in {data.get('name', city_input)}, {data['sys']['country']}")
        st.write(f"🌡 Temperature: {data['main']['temp']}°C")
        st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        st.write(f"☁ Weather: {data['weather'][0]['description'].title()}")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
        icon = data['weather'][0]['icon']
        st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
        
        # Map
        m = folium.Map(location=[lat, lon], zoom_start=6)
        folium.Marker([lat, lon], popup=city_input).add_to(m)
        st_folium(m, width=700, height=500)
    else:
        st.error("City not found! Try 'City, CountryCode' (e.g., Dallas, US).")
else:
    st.info("Enter a city in the sidebar to see the weather.")
