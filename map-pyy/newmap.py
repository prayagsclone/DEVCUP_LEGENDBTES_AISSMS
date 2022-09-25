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
# Set the viewport location
view_state = pdk.ViewState(longitude=78.348516,
    latitude=22.824289, zoom=10, bearing=0, pitch=0)

# Render
r = pdk.Deck(layers=[layer],tooltip=tooltip,initial_view_state=view_state)
#r.to_html("scatterplot_layer.html")
st.write(r)


#st.download_button("map_offline", data=html, file_name="of_ma.html")