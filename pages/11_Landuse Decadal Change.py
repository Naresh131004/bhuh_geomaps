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

st.title("Landuse Decadal Change")

st.markdown(
    """
   The maps from 2000, 2010, 2020, and 2023 illustrate the decadal changes in Bangalore's land use. Over these years, residential areas have expanded, commercial zones have increased, and industrial areas have grown. Green spaces and parks have seen changes, with some areas being developed and new ones added. Mixed-use developments have emerged, blending residential, commercial, and recreational spaces. These maps provide a clear visual representation of how land use in Bangalore has evolved over the past two decades.
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