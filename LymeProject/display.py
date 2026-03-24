import streamlit as st
#import extractLocations
from streamlit_folium import st_folium
import folium
import extractLocations 

import json
import requests


st.title("Lyme centered Locations according to online News Articles")

#st.write(extractLocations.location_frequency)
m = folium.Map([43, -100], zoom_start=3)

url = "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"


geojson_response = requests.get(url)
us_states = geojson_response.json()

# convert location_frequency to title-case for matching
freq_title_case = {k.title(): v for k, v in extractLocations.location_frequency.items()}

# define style function for coloring
def style_function(feature):
    state = feature['properties']['name']
    count = freq_title_case.get(state, 0)
    
    # simple coloring: more mentions = darker green
    if count == 0:
        color = '#f0f0f0'  # light gray
    elif count < 3:
        color = '#a1d99b'  # light green
    elif count < 6:
        color = '#41ab5d'  # medium green
    else:
        color = '#006d2c'  # dark green
    return {
        'fillOpacity': 0.7,
        'weight': 1,
        'fillColor': color,
        'color': 'black'
    }

folium.GeoJson(
    us_states,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(
        fields=['name'],
        aliases=['State:'],
        localize=True
    )
).add_to(m)


st_data = st_folium(m, width=700, height=500)





