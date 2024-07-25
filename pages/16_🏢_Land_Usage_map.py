import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap
import requests

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
   The maps from 2000, 2010, 2020, and 2023, displayed with split bars, show the decadal changes in Bangalore's land use. The split bars illustrate how residential areas have expanded, commercial zones have grown, and industrial zones have developed over time. Green spaces and parks have varied, with some areas being converted for development while new parks have been established. Mixed-use developments have increasingly integrated residential, commercial, and recreational spaces. These visual comparisons highlight the evolution of land use in Bangalore over the past two decades.
    """
)

left_year = st.selectbox("Select the year for the left map:", [2000, 2010, 2020, 2023], index=0)
right_year = st.selectbox("Select the year for the right map:", [2000, 2010, 2020, 2023], index=1)

# Base URL for the TIF files
base_url = "https://github.com/Naresh131004/bhuh_geomaps/raw/main/"

# Generate the file paths based on the selected years
left_layer_path = f"{base_url}{left_year}.tif"
right_layer_path = f"{base_url}{right_year}.tif"

m = leafmap.Map()
#m.add_basemap('SATELLITE')
heatmap_data_path = "https://github.com/Naresh131004/bhuh_geomaps/raw/main/bangalore_wards.geojson"

# Function to process GeoJSON properties and remove specified fields
def filter_properties(feature):
    properties = feature["properties"]
    properties = {k: v for k, v in properties.items() if k not in ["@id", "admin_level"]}
    feature["properties"] = properties
    return feature

# Load the GeoJSON data, filter properties, and add to the map
try:
    response = requests.get(heatmap_data_path)
    response.raise_for_status()
    geojson_data = response.json()
    filtered_geojson_data = {"type": "FeatureCollection", "features": [filter_properties(f) for f in geojson_data["features"]]}
    m.add_geojson(filtered_geojson_data, layer_name="Bangalore Heatmap")
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching GeoJSON data: {e}")

m.split_map(
    left_layer=left_layer_path, 
    right_layer=right_layer_path, 
    left_label=str(left_year), 
    right_label=str(right_year)
)

m.to_streamlit(height=800)

@st.cache_data
def load_data():
    df = pd.read_csv("https://github.com/Naresh131004/bhuh_geomaps/raw/main/Population%20in%20Bengaluru%20wards.csv")
    return df.drop(columns=["_id"])

df = load_data()

st.dataframe(df, width=2000)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)