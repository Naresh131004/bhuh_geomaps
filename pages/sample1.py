import streamlit as st
import folium
from streamlit_folium import folium_static

# Function to load and display map data
def load_map_data(year):
    # Replace with your actual data loading logic
    map_data = folium.Map(location=[12.9716, 77.5946], zoom_start=10)
    folium.TileLayer('cartodb positron', name=f"Map {year}").add_to(map_data)
    return map_data

# Sidebar for selecting years
st.sidebar.title("Select Years")
year_left = st.sidebar.selectbox("Select Year for Left Map", [2000, 2010, 2020, 2023])
year_right = st.sidebar.selectbox("Select Year for Right Map", [2000, 2010, 2020, 2023])

# Load map data for the selected years
map_left = load_map_data(year_left)
map_right = load_map_data(year_right)

# Display the maps side by side
st.write(f"### Maps for {year_left} (Left) and {year_right} (Right)")

# Add a split pane or similar component to compare maps
# This part depends on the specific libraries and methods you use to display maps side by side
# Here's an example using Folium to create two separate maps
col1, col2 = st.columns(2)
with col1:
    st.write(f"Map for {year_left}")
    folium_static(map_left)

with col2:
    st.write(f"Map for {year_right}")
    folium_static(map_right)