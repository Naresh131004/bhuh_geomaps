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

st.title("Malls,Market and Shopping areas")

st.title("Land Usage Map")

st.markdown(
    """
   Bangalore, officially Bengaluru, is renowned for its diverse shopping experiences, featuring a mix of high-end malls, bustling markets, and vibrant shopping areas. Major malls like Phoenix Marketcity, Orion Mall, and UB City offer a range of international and local brands, along with dining and entertainment options. The city also boasts popular markets such as Commercial Street and Russell Market, where shoppers can find everything from clothing and accessories to fresh produce and spices. Areas like Brigade Road and MG Road are known for their eclectic mix of shops and eateries, catering to various tastes and preferences. This blend of modern retail spaces and traditional markets makes Bangalore a dynamic destination for shopping enthusiasts.
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