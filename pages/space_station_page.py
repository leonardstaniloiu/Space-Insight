import json  
import urllib.request 
import time 
import streamlit as st
import pandas as pd
import pydeck as pdk

# Styling
st.markdown("""<style>
    .title-gradient {            
        background: linear-gradient(to right top, #d16ba5, #c777b9, #ba83ca, #aa8fd8, #9a9ae1, #8aa7ec, #79b3f4, #69bff8, #52cffe, #41dfff, #46eefa, #5ffbf1);
        color: transparent;
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        text-fill-color: transparent;
        font-size: 42px;
        font-weight: 900;
        font-family: Arial, sans-serif;
    }
    
    .icon-title {
        background: none !important;
        -webkit-background-clip: initial !important;
        background-clip: initial !important;
        -webkit-text-fill-color: initial !important;
        color: #ffffff !important;
        font-size: 42px;
    }
    """, unsafe_allow_html=True)

st.html(
    "<h1 class='title-gradient'>ISS Location Tracker <span class='icon-title'>🛰️</span></h1>"
    "<br><br>"
)

if st.button("Refresh ISS Location"):
     st.rerun()

try:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result["iss_position"]
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    
    # Display coordinates
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🌍 Latitude", f"{lat:.4f}°")
    with col2:
        st.metric("🌎 Longitude", f"{lon:.4f}°")
    
    df = pd.DataFrame({
        'lat': [lat],
        'lon': [lon],
        'icon_data': [{"url": "https://i.imgur.com/MCxgKhM.png", "width": 64, "height": 64, "anchorY": 64}]
    })
    
    icon_layer = pdk.Layer(
        type="IconLayer",
        data=df,
        get_icon="icon_data",
        get_size=4,
        size_scale=15,
        get_position=["lon", "lat"],
        pickable=True,
    )
    
    view_state = pdk.ViewState(
        latitude=lat,
        longitude=lon,
        zoom=2,
        pitch=0,
    )
    
    st.pydeck_chart(pdk.Deck(
        layers=[icon_layer],
        initial_view_state=view_state,
        tooltip={"text": "🛰️ ISS Position {lat}, {lon}"}
    ))
except Exception as e:
    st.error(f"Error fetching ISS location: {e}")