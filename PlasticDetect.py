import streamlit as st
from PIL import Image

st.set_page_config(page_title="PlasticDetect", page_icon="🌱", layout="wide")

# Intro

with st.container():
    st.markdown("<h1 style='text-align: center;'>¡Clasifiquemos microplásticos!</h1>", unsafe_allow_html=True)

reto, defi, ries_con = st.columns(3)

# Definir el estilo CSS para el color de fondo
color_reto = "#FFD700"  # Amarillo
color_defi = "#ADD8E6"  # Azul claro
color_ries_con = "#90EE90"  # Verde claro


# Colores de fondo para los títulos
color_fondo_titulo_reto = "#333300"  # Un amarillo más oscuro
color_fondo_titulo_defi = "#002244"  # Un azul más oscuro
color_fondo_titulo_ries_con = "#004400"  # Un verde más oscuro

# Usar las columnas con HTML y CSS para el color de fondo
with reto:
    st.markdown(f"<div style='background-color:{color_reto};padding:10px;border-radius:10px;'>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; background-color:{color_reto}; padding: 5px; border-radius: 5px;'>¿Qué es PlasticDetect?</h2>", unsafe_allow_html=True)
    st.write("PlasticDetect es una aplicación que facilita la identificación y clasificación de microplásticos presentes en imágenes capturadas por los propios usuarios. Para esto utiliza una IA que se encarga de analizar las imágenes y señalar la cantidad de microplásticos presentes y su tipo. Esta aplicación es el resultado del Reto 5 del Hackaton Coafina 2024: 'Microplásticos: un desafío ciudadano'.")
    st.markdown("</div>", unsafe_allow_html=True)

with defi:
    st.markdown(f"<div style='background-color:{color_defi};padding:10px;border-radius:10px;'>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; background-color:{color_fondo_titulo_defi}; padding: 5px; border-radius: 5px;'>¿Qué son los microplásticos?</h2>", unsafe_allow_html=True)
    st.write("Los microplásticos son partículas de plástico de tamaño inferior a 5 mm que se encuentran en el medio ambiente y que son resultado de la degradación de plásticos más grandes. Estos pueden ser ingeridos por animales y afectar su salud, además de contaminar el agua y el suelo.")
    st.markdown("</div>", unsafe_allow_html=True)

with ries_con:
    st.markdown(f"<div style='background-color:{color_ries_con};padding:10px;border-radius:10px;'>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; background-color:{color_fondo_titulo_ries_con}; padding: 5px; border-radius: 5px;'>Riesgos y consecuencias</h2>", unsafe_allow_html=True)
    st.write("Los microplásticos pueden tener efectos negativos en la salud de los seres vivos, ya que pueden ser ingeridos por animales y pasar a través de la cadena alimentaria. Además, pueden contaminar el agua y el suelo, afectando a los ecosistemas y a la biodiversidad.")
    st.markdown("</div>", unsafe_allow_html=True)