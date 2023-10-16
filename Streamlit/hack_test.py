import streamlit as st
from PIL import Image

# Set the page configuration first
st.set_page_config(
    page_title="IOM-UN 2023 Hackathon",
    page_icon="🧊",
    layout="wide",
)

# Tab titles and content
tab_titles = ["About", "Hackathon Resources", "Data Page"]

# st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio("",tab_titles)

header_image = Image.open('./imagies/header.png')
st.image(header_image, width=1300)
# Streamlit app configuration
st.sidebar.title("Navigation")

# Define the content for the About tab
if selected_tab == "About":
    st.write("Congratulations for being selected for this edition of **IOM-UCL 'Bridging Climate Change and Human Mobility'** hackathon event. To ensure you're well-prepared for this exciting journey, we've outlined the technical requirements and provided a comprehensive list of resources to support your data analysis endeavors.")
    st.write("This section will guide you through the essential aspects of what you'll need in terms of hardware, software, and data resources to make the most of this hackathon experience. The goal is to ensure you with the tools and knowledge required to delve into the complex world of climate change and human mobility in the East and Horn of Africa region.")

# Define the content for the Data Page tab
elif selected_tab == "Data Page":
    st.write("This page")

# Define the content for the Hackathon Resources tab
elif selected_tab == "Hackathon Resources":
    st.write("This section will guide you through the essential aspects of what you'll need in terms of hardware, software, and data resources to make the most of this hackathon experience. The goal is to ensure you with the tools and knowledge required to delve into the complex world of climate change and human mobility in the East and Horn of Africa region.")
    st.write("## Data for Hackathon")
    st.write("Participants will have access to Displacement Tracking Matrix (DTM) dataset related to the East and Horn of Africa region.")
