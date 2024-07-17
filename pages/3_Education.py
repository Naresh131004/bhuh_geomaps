import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Website
<https://www.bhuhpramaan.com>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/MWpI4OI.jpeg"
st.sidebar.image(logo)

st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 10px; /* Adjust the value as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Land use and Land classification of Bangalore")

st.title("Land Usage Map")

st.markdown(
    """
    A land usage map, also known as a land use map, visually represents how different areas of land are utilized in a specific region. These maps are used to display various types of land use categories, such as residential, commercial, industrial, agricultural, forest, water bodies, and undeveloped land.  
    
    Choose the year for the left and right to see the split screen view.
    """
)

# Base URL for the TIF files
base_url = "https://github.com/Naresh131004/bhuh_geomaps/raw/main/"

m = leafmap.Map()
heatmap_data_path = "https://github.com/Naresh131004/Bhuh-geomaps/raw/main/BANK%20LAYER.geojson"
m.add_geojson(heatmap_data_path, layer_name="Bangalore Heatmap")
m.to_streamlit(height=800)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)