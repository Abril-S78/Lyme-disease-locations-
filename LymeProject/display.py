import streamlit as st
import extractLocations


st.title("Lyme centered Locations")
st.write(extractLocations.location_frequency)
