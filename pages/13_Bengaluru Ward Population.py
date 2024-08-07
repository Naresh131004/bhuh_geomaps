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

st.title("Bangalore Ward Population")

st.markdown(
    """
    Bangalore's population data, divided across various wards, can be filtered by various parameters such as total population size, density, growth trends, socio-economic factors, and geographical location. This allows for detailed analysis of the most and least populous areas, population density, changes over time, and socio-economic characteristics. Filtering by geographical location, such as central or peripheral wards, also provides insights into the demographic distribution and urban planning needs across the city. This detailed segmentation helps in effective resource allocation and understanding demographic trends in Bangalore.
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