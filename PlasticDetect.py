import streamlit as st
from PIL import Image

st.set_page_config(page_title="PlasticDetect", page_icon="🌱", layout="wide")

# Intro

with st.container():
    st.markdown("<h1 style='text-align: center;'>¡Clasifiquemos microplásticos!</h1>", unsafe_allow_html=True)

# Crear dos columnas
reto, defi, ries_con = st.columns(3)

# Usar las columnas
with reto:
    st.header("¿Qué es PlasticDetect?")
    st.write("PlasticDetect es una aplicación que facilita la identificación y clasiﬁcación de microplásticos presentes en imágenes capturadas por los propios usuarios. Para esto utiliza una IA que se encarga de analizar las imágenes y señalar la cantidad de microplásticos presentes y su tipo. Esta aplicación es el resultado del Reto 5 del Hackaton Coafina 2024: 'Microplásticos: un desafío ciudadano'.")

with defi:
    st.header("¿Qué son los microplásticos?")
    st.write("Los microplásticos son partículas de plástico de tamaño inferior a 5 mm que se encuentran en el medio ambiente y que son resultado de la degradación de plásticos más grandes. Estos pueden ser ingeridos por animales y afectar su salud, además de contaminar el agua y el suelo.")

with ries_con:
    st.header("Riesgos y consecuencias")
    st.write("Los microplásticos pueden tener efectos negativos en la salud de los seres vivos, ya que pueden ser ingeridos por animales y pasar a través de la cadena alimentaria. Además, pueden contaminar el agua y el suelo, afectando a los ecosistemas y a la biodiversidad.")