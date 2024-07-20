import streamlit as st
from PIL import Image

st.set_page_config(page_title="PlasticDetect", page_icon="🌱", layout="wide")

# Intro

with st.container():
    st.markdown("<h1 style='text-align: center;'>¡Clasifiquemos microplásticos!</h1>", unsafe_allow_html=True)