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

st.title("Heatmap")

st.markdown(
    """
    A heatmap is a visual representation of data that uses color variations to represent the density of data points in a particular area. It's a useful tool for understanding patterns, trends, and distributions within a dataset.
    """
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