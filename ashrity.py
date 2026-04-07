lat = map_data['last_clicked']['lat']
lon = map_data['last_clicked']['lng']

url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    st.subheader("Weather Info")
    st.write(f"📍 Coordinates: {lat:.2f}, {lon:.2f}")
    st.write(f"🌡 Temperature: {data['main']['temp']}°C")
    st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    st.write(f"☁ Weather: {data['weather'][0]['description'].title()}")
    st.write(f"💧 Humidity: {data['main']['humidity']}%")
    
    icon = data['weather'][0]['icon']
    st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
else:
    st.error("Weather data not found at this location.")
