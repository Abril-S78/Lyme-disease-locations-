import streamlit as st
#import extractLocations
from streamlit_folium import st_folium
import folium


st.title("Lyme centered Locations")

#st.write(extractLocations.location_frequency)
m = folium.Map([43, -100], zoom_start=7)

url = "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"

folium.GeoJson(url).add_to(m)
st_data = st_folium(m, width=700, height = 500)




