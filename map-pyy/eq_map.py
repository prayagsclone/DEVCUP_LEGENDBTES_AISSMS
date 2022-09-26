import imp
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk

st.header('3D Visualization')

#a=st.pydeck_chart
#b=

data=pd.read_csv('Indian_earthquake_data.csv')

#layers setting
layers=pdk.Layer('HexagonLayer',
    data,
    get_position=['Longitude', 'Latitude'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,                 
    coverage=1)

#view Port Location
view_state=pdk.ViewState(longitude=78.348516,
    latitude=22.824289,
    zoom=6,
    min_zoom=1,
    max_zoom=15,
    pitch=40.5,
    bearing=-27.36)

# Render
r = pdk.Deck(layers=[layers], initial_view_state=view_state)
st.write(r)
