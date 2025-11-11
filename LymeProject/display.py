import streamlit as st
import extractLocations
from streamlit_folium import st_folium
import folium


st.title("Lyme centered Locations")

st.write(extractLocations.location_frequency)
 



