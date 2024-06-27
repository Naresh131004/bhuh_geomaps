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
    
    On the left, you can see the land use and classification map of Bangalore for the year 2000, while on the right, the map shows the updated land use and classification for the year 2023.    """
)

m = leafmap.Map()
before_raster = "https://github.com/Naresh131004/bhuh_geomaps/raw/main/2000.tif"
after_raster= "https://github.com/Naresh131004/bhuh_geomaps/raw/main/2023.tif"
m.split_map(
        left_layer=before_raster, right_layer=after_raster, left_label="2000", right_label="2023"
    )

m.to_streamlit(height=800)

file_path = "https://github.com/Naresh131004/bhuh_geomaps/raw/main/Population%20in%20Bengaluru%20wards.csv"

df = pd.read_csv(file_path)

st.dataframe(df)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)