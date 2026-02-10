import datetime
import streamlit as st
import requests


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
    "<h1 class='title-gradient'>Space Insights <span class='icon-title'>🌠</span></h1>"
    "<br><br>"
)

today = datetime.date.today()

selected_date = st.date_input(
    "Select a date to view the Astronomy Picture of the Day (APOD):",
    value=today,
    max_value=today,
    min_value=datetime.date(1995, 6, 16)
)

API_KEY = "DEMO_KEY" 
API_url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={selected_date}"

response = requests.get(API_url)

if response.status_code == 200:
    data = response.json()
    st.subheader(data['title'])
    st.image(data['url'])
    st.markdown(f"**Date:** {data['date']}")
    st.markdown(f"**Explanation:** {data['explanation']}")
    st.markdown(f"**Copyright:** {data.get('copyright', 'N/A')}")
elif response.status_code == 404:
    st.warning("No data available for the selected date. Please choose another date.")
elif response.status_code == 429:
    st.warning("Too many requests. Please try again later.")
elif response.status_code == 500:
    st.error("Internal server error.")
else:
    st.error(f"Error fetching data: {response.status_code}")