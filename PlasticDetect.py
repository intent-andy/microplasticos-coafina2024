import streamlit as st
from PIL import Image

st.set_page_config(page_title="PlasticDetect", page_icon="🌱", layout="wide")

# Intro

with st.container():
    st.markdown("<h1 style='text-align: center;'>¡Clasifiquemos microplásticos!</h1>", unsafe_allow_html=True)

    st.write("Bienvenido a PlasticDetect, una aplicación que te permite identificar y clasificar microplásticos presentes en imágenes capturadas por ti. Para comenzar, sube una imagen en la sección de 'Cargar imagen' y presiona el botón 'Analizar imagen'. La IA se encargará de analizar la imagen y señalar la cantidad de microplásticos presentes y su tipo.")