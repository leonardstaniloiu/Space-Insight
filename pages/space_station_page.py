import streamlit as st

st.set_page_config(
    page_title="Space Insights",
    page_icon=":milky_way:",
    layout="centered"
)

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
        color: #ffffff !important;   /* sau orice culoare vrei */
        font-size: 42px;
    }
    """, unsafe_allow_html=True)
#  End styling


