import streamlit as st
from PIL import Image

# Open your images
image = Image.open('./flyer.png')
header_image = Image.open('./imagies/header.png')

# Display header_image with a large width to maximize it
header_image = Image.open('./imagies/header.png')
st.image(header_image, width=1000)
st.title("This is the title")
st.subheader("This is subheader")
st.markdown("---")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
# Rest of your Streamlit code
