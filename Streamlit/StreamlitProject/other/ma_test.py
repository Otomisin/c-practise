import streamlit as st
import pandas as pd
import geopandas as gpd
import json
from datetime import datetime

# Decorator for caching should be 'st.cache' not 'st.cache_data'
@st.cache
def today():
    return datetime.now().strftime("%Y-%m-%d")

def display_ssd_facts(ssd_mt_admin_point, ssd_mt_admin_point_yes):
    total_assessment = ssd_mt_admin_point['A3_Supervisor_Name'].value_counts().sum()
    total_points_out = ssd_mt_admin_point_yes['A3_Supervisor_Name'].value_counts().sum()
    total_points_out_per = total_points_out / total_assessment * 100
    total_payams = ssd_mt_admin_point['A7_payam'].value_counts().sum()

    return total_assessment, total_points_out, total_points_out_per, total_payams

def main():
    st.set_page_config(page_title='South Sudan Points Analysis')
    st.title('South Sudan Points Analysis')
    st.caption(f'Checking for points not in designated area. Assessed today: {today()}')

    # File upload for the CSV and GeoJSON files
    csv_file = st.sidebar.file_uploader("Upload CSV File", type=['csv'])
    geojson_file = st.sidebar.file_uploader("Upload GeoJSON File", type=['geojson'])

    if csv_file and geojson_file:
        ssd_points = pd.read_csv(csv_file, low_memory=False)
        SSD_Admin_data = json.load(geojson_file)
        SSD_Admin = gpd.GeoDataFrame.from_features(SSD_Admin_data['features'])

        if SSD_Admin.crs is None:
            SSD_Admin.set_crs('EPSG:4326', inplace=True)

        ssd_ra_p2_20230807_v3 = gpd.GeoDataFrame(
            ssd_points,
            geometry=gpd.points_from_xy(ssd_points['_location_gps_longitude'], ssd_points['_location_gps_latitude']),
            crs='EPSG:4326'
        )

        if ssd_ra_p2_20230807_v3.crs != SSD_Admin.crs:
            ssd_ra_p2_20230807_v3.to_crs(SSD_Admin.crs, inplace=True)

        ssd_mt_admin_point = gpd.sjoin(ssd_ra_p2_20230807_v3, SSD_Admin, how='inner', predicate='intersects')

        ssd_mt_admin_point = ssd_mt_admin_point.assign(
            Point_outside_payam=lambda x: [
                'Yes' if a != b and a != 'other' and b != 'other' else 'No' 
                for a, b in zip(x['A7_payam'], x['Payam_MT_P'])
            ]
        )

        ssd_mt_admin_point_yes = ssd_mt_admin_point[ssd_mt_admin_point['Point_outside_payam'] == 'Yes']

        # Metrics Display
        total_assessment, total_points_out, total_points_out_per, total_payams = display_ssd_facts(ssd_mt_admin_point, ssd_mt_admin_point_yes)

        st.subheader('The Mini Facts')
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(label="Total Assessment", value=total_assessment)

        with col2:
            st.metric(label="Total Points Out", value=f"{total_points_out} ({total_points_out_per:.2f}%)")

        with col3:
            st.metric(label="Total Payams", value=total_payams)

        # Continue with additional analysis or visualizations

# Run the main function
if __name__ == "__main__":
    main()
