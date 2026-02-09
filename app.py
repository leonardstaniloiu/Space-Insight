import streamlit as st

st.set_page_config(
    page_title="Space Insights",
    page_icon=":milky_way:",
    layout="centered"
)

apod_page = st.Page("pages/apod_page.py", title="Astronomy picture of day", icon=":material/planet:")
iss_page = st.Page("pages/space_station_page.py", title="Space Station Tracker", icon=":material/satellite_alt:")
pg = st.navigation([apod_page, iss_page])
pg.run()
