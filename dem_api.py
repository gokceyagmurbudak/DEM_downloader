import requests
import pandas as pd
import streamlit as st

container = st.container()
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    
with st.sidebar:
    south_input = st.text_input('South Bound',         
                                label_visibility=st.session_state.visibility,
                                disabled=st.session_state.disabled,
                                placeholder='South Coordinates')
    north_input = st.text_input('North Bound', 
                                label_visibility=st.session_state.visibility,
                                disabled=st.session_state.disabled,
                                placeholder='North Coordinates')
    west_input = st.text_input('West Bound', 
                                label_visibility=st.session_state.visibility,
                                disabled=st.session_state.disabled,
                                placeholder='West Coordinates')
    east_input = st.text_input('East Bound',  
                                label_visibility=st.session_state.visibility,
                                disabled=st.session_state.disabled,
                                placeholder='East Coordinates')
    
    
    if st.button('Show Bounds'):
        south = float(south_input)
        north = float(north_input)
        east = float(east_input)
        west = float(west_input)
        xbounds = [south,south,north,north]
        ybounds = [east,west,east,west]
        df = pd.DataFrame(data = {'lat': xbounds,'lon': ybounds})
        container.map(df)
    if st.button('Download DEM'):
        url='https://portal.opentopography.org/API/globaldem?demtype=SRTMGL3&south='+south_input+'&north='+north_input+'&west='+west_input+'&east='+east_input+'&outputFormat=GTiff&API_Key=demoapikeyot2022'
        response= requests.get(url)
        open('C:/Users/HP/Desktop/PROJECTS/dem_api/raster.tif','wb').write(response.content)
        st.write('Downloaded Sucessfully')