import streamlit as st
import requests

st.title("🌤 Weather App")

# Input city
city = st.text_input("Enter your city:", "")

# API key from OpenWeatherMap
API_KEY = "YOUR_API_KEY_HERE"

if city:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {data['name']}, {data['sys']['country']}")
        st.write(f"🌡 Temperature: {data['main']['temp']}°C")
        st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        st.write(f"☁ Weather: {data['weather'][0]['description'].title()}")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
    else:
        st.error("City not found! Please check your spelling.")
