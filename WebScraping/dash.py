import streamlit as st
import pandas as pd

# Sample data
data = {
    "Title": [
        "Nigeria — North-east — Mobility Tracking Round 46 IDP and Returnee Atlas (December 2023)",
        "Latvia — On the Way Back: Survey with Ukrainian nationals — Annual (2023)",
        "Burundi — Suivi des urgences (04 - 10 Février 2024)",
        "Thailand - Multisectoral Assessment of Needs 2023 – Chiang Mai province",
        "Cameroun — Suivi des urgences 89 (06-13 Février 2024)"
    ],
    "Summary": [
        "In Round 46 a total of 2305335 Internally Displaced Persons IDPs were identified in 472239 households. This signifies a slight increase of less than one per cent or 9801 individuals compared to Round 4…",
        "Surveys with Ukrainian Nationals LATVIA UKRAINE RESPONSE © IO M 2 02 3 2023 ANNUAL… photo: IOM field workers welcome people from Ukraine in Zahony to support them and provide…",
        "La DTM a identifié 1772 personnes affectées dont 327 personnes déplacées par les pluies torrentielles et les vents violents dans les provinces de Rutana Cibitoke et Bubanza",
        "This factsheet aims to provide a snapshot of multisectoral conditions needs and challenges among Myanmar migrants in Chiang Mai province as captured between October 2023 and January 2024 by IOM Thaila…",
        "Le suivi des situations d'urgence (Emergency Tracking Tool - ETT) est une des composantes de la Matrice de suivi des déplacements (Displacement Tracking Matrix - DTM) déployée par l'Orga…"
    ],
    "Link": [
        "https://dtm.iom.int/reports/nigeria-north-east-mobility-tracking-round-46-idp-and-returnee-atlas-december-2023",
        "https://dtm.iom.int/reports/latvia-way-back-survey-ukrainian-nationals-annual-2023",
        "https://dtm.iom.int/reports/burundi-suivi-des-urgences-04-10-fevrier-2024",
        "https://dtm.iom.int/reports/thailand-multisectoral-assessment-needs-2023-chiang-mai-province",
        "https://dtm.iom.int/reports/thailand-multisectoral-assessment-needs-2023-chiang-mai-province"
    ],
    "Published Date": [
        "Feb 14 2024",
        "Feb 14 2024",
        "Feb 14 2024",
        "Feb 14 2024",
        "Feb 14 2024"
    ],
    "country_name": ["Nigeria", "Latvia", "Burundi", "Thailand", "Cameroon"],
    "Thematics": ["Return", "Humanitarian", "Solutions", "Solutions", "Solutions"]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Streamlit app
def app():
    st.title('Interactive Report Dashboard')

    # Sidebar filters
    country = st.sidebar.multiselect('Select Country:', options=df['country_name'].unique(), default=df['country_name'].unique())
    thematic = st.sidebar.multiselect('Select Thematic:', options=df['Thematics'].unique(), default=df['Thematics'].unique())

    # Filtering data
    filtered_data = df[(df['country_name'].isin(country)) & (df['Thematics'].isin(thematic))]

    # Displaying filtered data
    for index, row in filtered_data.iterrows():
        st.subheader(row['Title'])
        st.write(f"Published Date: {row['Published Date']}")
        st.write(f"Country: {row['country_name']}")
        st.write(f"Thematics: {row['Thematics']}")
        st.write(row['Summary'])
        st.markdown(f"[Read More]({row['Link']})", unsafe_allow_html=True)

if __name__ == '__main__':
    app()
