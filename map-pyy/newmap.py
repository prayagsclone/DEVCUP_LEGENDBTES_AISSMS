#from cgitb import html
#from ctypes.wintypes import RGB
#from turtle import color
import streamlit as st
import pydeck as pdk
import pandas as pd
import math
#from io import BytesIO



df = pd.read_csv("use.csv")

layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=600,
    radius_min_pixels=5,
    radius_max_pixels=15,
    line_width_min_pixels=1,
    get_position=['long', 'lat'],
    #get_radius="exits_radius",
    get_fill_color=[255, 140, 0],
    get_line_color=[0, 0, 0],
    
)
tooltip = {
    "html": "<b>{district},{severity}</b>",
    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}

#from cgitb import html
#from ctypes.wintypes import RGB
#from turtle import color
import streamlit as st
import pydeck as pdk
import pandas as pd
import math
#from io import BytesIO



df = pd.read_csv("use.csv")

layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=600,
    radius_min_pixels=5,
    radius_max_pixels=15,
    line_width_min_pixels=1,
    get_position=['long', 'lat'],
    
    
)

#modified 
tooltip = {
    "html": "<b>{district},{severity}</b>",
    "style": {"background": "blue", "color": "white","fint-size": "25", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}


# Set the viewport location

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