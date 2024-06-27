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

st.markdown(
    """
    The Land Use and Land Cover (LULC) change happened during the Twenty-Three year period in Bengaluru Urban District, Karnataka. One of the fast-growing cities in India is Bengaluru which has undergone many changes to its landscape as it moves to urbanization. Land cover / land use changes (LULC) were assessed through the employment of remote sensing data and Geographic Information System (GIS) technology, for years 2000 to 2023. Built-up, vegetation, water bodies and barren land are classified based on the desired land use through a machine learning algorithm known as Support Vector Machine. This page shows the significant expansion in built-up landuse, mainly at the cost of greenspace and bare land. The change underscores an urgent need for sustainable urban planning to tackle environmental risks associated with the expansion of megacities, such as increased temperatures.
    """
)

st.header("Ward Classifications")

markdown = """
The below map is the classification of the Bangalore wards with their Boundaries.

"""

st.markdown(markdown)

m = leafmap.Map(center=[12.971599,77.594566], zoom=9.8)
heatmap_data_path = "https://github.com/Naresh131004/bhuh_geomaps/blob/main/bangalore_wards.geojson"
m.add_geojson(heatmap_data_path, layer_name="Bangalore Heatmap")
m.to_streamlit(height=500)

st.header("Bangalore")

markdown = """
Bengaluru is the capital and largest city of the southern Indian state of Karnataka. It has a population of more than 8 million and a metropolitan population of around 15 million, making it India's third most popular city and fourth most popular urban city. Bangalore spans an area of approximately 741 square kilometers (286 square miles). Including the urban and suburban areas, the Bangalore metropolitan region covers about 8,005 square kilometers (3,090 square miles). It is the most popular city and largest urban city in South India, and is the 27th largest city in the world. Located on the Deccan Plateau, at a height of over 900 m (3,000 ft) above sea level, Bangalore has a pleasant climate throughout the year, with its parks and green spaces earning it the reputation of India's "Garden City". Its elevation is the highest of India's major cities.

Bangalore, known as the "Silicon Valley of India," is the country's top IT exporter. It is home to notable technological organizations including ISRO, Infosys, Wipro, and HAL. As India's second fastest-growing major metropolis, Bangalore boasts numerous educational and research institutions, such as IISc, IIMB, NIFT, NID, NLSIU, and NIMHANS. Additionally, the city hosts state-owned aerospace and defense entities like Bharat Electronics, Hindustan Aeronautics, and National Aerospace Laboratories, as well as the Kannada film industry.

Agriculture:

Bangalore, surrounded by fertile rural areas, is a hub for horticulture, silk production, and dairy farming. The region is known for cultivating fruits, vegetables, flowers, and key crops like ragi and maize. Bangalore also hosts prominent agricultural research institutions like the University of Agricultural Sciences, fostering innovations in farming techniques and crop improvement. Despite challenges from urbanization and water scarcity, government initiatives support local farmers with subsidies, training, and market access, maintaining the area's significant role in agriculture.

Places with Pincode, Latitude and Longitude:"""

st.markdown(markdown)

file_path = "https://github.com/Naresh131004/bhuh_geomaps/raw/main/BangaloreAreaLatLongDetails.csv"

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
