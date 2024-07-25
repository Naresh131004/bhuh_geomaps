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

st.title("Bank Financial Institutions")

st.markdown(
    """
  Bangalore, officially Bengaluru, hosts a robust network of banking and financial institutions that cater to diverse needs. Major national and international banks, including State Bank of India, HDFC Bank, ICICI Bank, and Axis Bank, operate extensively throughout the city, offering a range of services from savings accounts and loans to investment and insurance products. Additionally, numerous financial institutions provide specialized services such as wealth management, brokerage, and financial advisory. Bangalore is also a hub for fintech companies, driving innovation in digital banking and financial services. This comprehensive financial ecosystem supports both individual and corporate financial needs, contributing to the city’s status as a major economic and business center.
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