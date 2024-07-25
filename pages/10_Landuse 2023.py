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

st.title("Land Use 2023")

st.markdown(
    """
    As of 2023, Bangalore's land use reflects its rapid growth and urbanization, featuring a diverse mix of residential, commercial, industrial, and green spaces. Residential areas include high-density apartments and traditional neighborhoods, with key zones in Whitefield and Koramangala. Commercial activity is concentrated in business districts like the CBD, Electronic City, and IT hubs. Industrial areas such as Peenya and Bommasandra focus on manufacturing and technology. The city maintains significant green spaces, including Cubbon Park and Lalbagh Botanical Garden, amidst the urban landscape. Additionally, mixed-use developments are increasingly common, blending residential, commercial, and recreational facilities to create integrated communities.
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