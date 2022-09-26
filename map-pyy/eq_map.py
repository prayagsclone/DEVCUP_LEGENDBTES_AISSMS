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

#view Port rtemp deletions 
