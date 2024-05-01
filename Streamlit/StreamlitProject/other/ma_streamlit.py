import streamlit as st
import pandas as pd
import folium
import geopandas as gpd
from streamlit_folium import st_folium
from datetime import datetime
import json

def today():
    return datetime.now().strftime("%Y-%m-%d")

APP_TITLE = 'Points out of designated locations'
APP_SUB_TITLE = f'Assessed today {today()}'

def load_data():
    # Load data
    ssd_points = pd.read_excel("./Rural_Inter_Sector.xlsx")

    # Load and convert SSD_Admin JSON data to GeoDataFrame
    with open('ssdamingeojson.geojson', 'r') as file:
        SSD_Admin_data = json.load(file)
    SSD_Admin = gpd.GeoDataFrame.from_features(SSD_Admin_data['features'])

    # Convert ssd_points to GeoDataFrame and perform spatial join
    ssd_ra_p2_20230807_v3 = gpd.GeoDataFrame(
        ssd_points, 
        geometry=gpd.points_from_xy(ssd_points['_location_gps_longitude'], ssd_points['_location_gps_latitude']),
        crs='EPSG:4326'
    )

    ssd_mt_admin_point = gpd.sjoin(ssd_ra_p2_20230807_v3, SSD_Admin, how='inner', predicate='intersects')

    ssd_mt_admin_point = ssd_mt_admin_point.assign(
        Point_outside_payam=lambda x: ['No' if a != b else 'Yes' for a, b in zip(x['A7_payam'], x['Payam_MT_P'])]
    )

    ssd_mt_admin_point_yes = ssd_mt_admin_point[ssd_mt_admin_point['Point_outside_payam'] == 'Yes']
    ssd_mt_admin_point_no = ssd_mt_admin_point[ssd_mt_admin_point['Point_outside_payam'] == 'No']
    
    ssd_points_all = ssd_points.shape[0]
    ssd_out_count = ssd_mt_admin_point.shape[0]
    
    return ssd_points, SSD_Admin, ssd_mt_admin_point_yes, ssd_mt_admin_point_no, ssd_points_all, ssd_out_count



def main():
    st.set_page_config(page_title=APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)


    ssd_points, SSD_Admin, ssd_mt_admin_point_yes, ssd_mt_admin_point_no, ssd_points_all, ssd_out_count = load_data()
    
    st.subheader(f'{ssd_out_count} out of {ssd_points_all} points are outside designated areas')
    
    st.write("Points Outside Payam (Yes):", ssd_mt_admin_point_yes.head())
    st.write("The columns", ssd_mt_admin_point_no.columns)


if __name__ == "__main__":
    main()
