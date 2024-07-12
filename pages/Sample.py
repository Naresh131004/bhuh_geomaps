import altair as alt
import pandas as pd
import streamlit as st


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

@st.cache_data
def load_data():
    df = pd.read_csv("https://github.com/Naresh131004/Bhuh-geomaps/raw/main/year,population,growth%20rate,rainfal.csv")
    return df


df = load_data()

# Show a multiselect widget with the genres using `st.multiselect`.
genres = st.multiselect(
    "Genres",
    df.genre.unique(),
    ["population", "growth rate", "rainfall(mm)"],
)

# Show a slider widget with the years using `st.slider`.
years = st.slider("Years", 2000, 2023, (2000, 2023))

# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df["genre"].isin(genres)) & (df["year"].between(years[0], years[1]))]
df_reshaped = df_filtered.pivot_table(
    index="year", columns="genre", values="population", aggfunc="sum", fill_value=0,
)
df_reshaped = df_reshaped.sort_values(by="year", ascending=False)


# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"year": st.column_config.TextColumn("year")},
)

df_population = df[df['genre'] == 'population']
df_growth_rate = df[df['genre'] == 'growth rate']
df_rainfall = df[df['genre'] == 'rainfall(mm)']

# Create Altair charts for each dataframe
# Population Chart
population_chart = alt.Chart(df_population).mark_line().encode(
    x='year:N',
    y='population:Q',
    tooltip=['year:N', 'population:Q']
).properties(
    title='Population Over Time'
)

st.altair_chart(population_chart, use_container_width=True)

# Growth Rate Chart
growth_rate_chart = alt.Chart(df_growth_rate).mark_line().encode(
    x='year:N',
    y='growth rate:Q',
    tooltip=['year:N', 'growth rate:Q']
).properties(
    title='Growth Rate Over Time'
)

st.altair_chart(growth_rate_chart, use_container_width=True)

# Rainfall Chart
rainfall_chart = alt.Chart(df_rainfall).mark_line().encode(
    x='year:N',
    y='rainfall(mm):Q',
    tooltip=['year:N', 'rainfall(mm):Q']
).properties(
    title='Rainfall Over Time'
)

st.altair_chart(rainfall_chart, use_container_width=True)