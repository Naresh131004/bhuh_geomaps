import streamlit as st
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

st.title("Population")

st.markdown(
    """
   Bangalore, officially known as Bengaluru, is Karnataka's capital with a population of approximately 12.3 million. The city is divided into various wards, managed by the Bruhat Bengaluru Mahanagara Palike (BBMP). Each ward varies in population density and socio-economic status, aiding in efficient urban planning and resource management. Central wards like Shanthinagar, Richmond Town, and Vasanth Nagar, part of the Central Business District (CBD), are densely populated and feature a mix of residential and commercial spaces. Peripheral wards, including Yelahanka and Whitefield, have seen rapid growth due to IT and industrial expansion, leading to increased population influx. This ward-based classification helps address local needs effectively, promoting balanced development and better governance across Bangalore's diverse urban landscape. The city's population continues to grow, driven by its status as a major tech and economic hub.    """
)

filepath = "https://raw.githubusercontent.com/Naresh131004/bhuh_geomaps/main/BangaloreAreaLatLongDetails%20(1).csv"
m = leafmap.Map(center=[12.971599,77.594566], zoom=10.8)
m.add_heatmap(
    filepath,
    latitude="Latitude",
    longitude="Longitude",
    value="Pop_max",
    name="Heat map",
    radius=22,
    )
m.to_streamlit(height=700)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)