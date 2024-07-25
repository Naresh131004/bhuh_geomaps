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

st.title("Education")

st.markdown(
    """
   Bangalore, also known as Bengaluru, is a major educational hub in India. The city offers a wide range of schools, including international, national, and public institutions, providing quality education from primary to secondary levels. In higher education, Bangalore is home to numerous colleges and universities specializing in engineering, management, science, arts, and commerce. These institutions, known for their excellence, offer undergraduate, postgraduate, and doctoral programs. With modern facilities, experienced faculty, and vibrant campuses, Bangalore attracts students from across India and the world, making it a key center for learning and innovation. This strong educational infrastructure produces skilled professionals, contributing to the city's status as a knowledge and technology hub.
    """
)

# Base URL for the TIF files
base_url = "https://github.com/Naresh131004/bhuh_geomaps/raw/main/"

m = leafmap.Map()
heatmap_data_path = "https://github.com/Naresh131004/Bhuh-geomaps/raw/main/clippedengineeringcollege.geojson"
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