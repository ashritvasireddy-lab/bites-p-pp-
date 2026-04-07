import streamlit as st
import pandas as pd

csv_url = "https://raw.githubusercontent.com/condwanaland/worldcities/main/worldcities.csv"
cities = pd.read_csv(csv_url)
