import pandas as pd

# Load world cities from online URL
cities_url = "https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.75/worldcities.csv"
cities = pd.read_csv(cities_url)
st.write(cities.head())  # test if loaded
