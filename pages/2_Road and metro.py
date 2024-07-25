import streamlit as st
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

st.title("Road and Metro")

st.markdown(
    """
    Bangalore, known as Bengaluru, has a robust metro and road network. The Namma Metro, launched in 2011, covers over 40 kilometers, connecting key areas like MG Road and Majestic, with expansions in progress. Major roads like MG Road, Bannerghatta Road, and Outer Ring Road ensure city-wide connectivity. Despite rapid urbanization leading to traffic congestion, the city has developed flyovers, underpasses, and signal-free corridors to improve traffic flow. Ongoing projects aim to further enhance connectivity and transportation efficiency, supporting Bangalore's growth as a major tech and economic hub.
    """
)

# URL for the GeoJSON file
geojson_data_url = "https://github.com/geohacker/namma-metro/raw/master/metro-lines-stations.geojson"

# Load the GeoJSON data
response = requests.get(geojson_data_url)
geojson_data = response.json()

# Filter GeoJSON to include only 'Name' in the popup
for feature in geojson_data['features']:
    properties = feature['properties']
    filtered_properties = {'Name': properties.get('Name')}
    feature['properties'] = filtered_properties

# Create a map object
m = leafmap.Map()

# Add the filtered GeoJSON to the map
m.add_geojson(geojson_data, layer_name="Bangalore Metro Lines")

# Render the map in Streamlit
m.to_streamlit(height=800)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)