import streamlit as st
from PIL import Image

st.set_page_config(page_title="MonomerFinder", page_icon="🌱", layout="wide")

# Intro
st.markdown("<h1 style='text-align: center;'>¡Clasifiquemos microplásticos!</h1>", unsafe_allow_html=True)

# Definir el estilo CSS para el color de fondo
color_reto = "#FFD700"  # Amarillo
color_defi = "#ADD8E6"  # Azul claro
color_ries_con = "#90EE90"  # Verde claro

# Menú desplegable para "¿Qué es MonomerFinder?"
with st.expander(f"¿Qué es MonomerFinder?"):
    st.markdown(f"<div style='background-color:{color_reto}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
    st.write("MonomerFinder es una aplicación que facilita la identificación y clasificación de microplásticos presentes en imágenes capturadas por los propios usuarios. Para esto utiliza una IA que se encarga de analizar las imágenes y señalar la cantidad de microplásticos presentes y su tipo. Esta aplicación es el resultado del Reto 5 del Hackaton Coafina 2024: 'Microplásticos: un desafío ciudadano'.")
    st.markdown("</div>", unsafe_allow_html=True)

# Menú desplegable para "¿Qué son los microplásticos?"
with st.expander("¿Qué son los microplásticos?"):
    st.markdown(f"<div style='background-color:{color_defi}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
    st.write("Los microplásticos son partículas de plástico de tamaño inferior a 5 mm que se encuentran en el medio ambiente y que son resultado de la degradación de plásticos más grandes. Estos pueden ser ingeridos por animales y afectar su salud, además de contaminar el agua y el suelo.")
    st.markdown("</div>", unsafe_allow_html=True)

# Menú desplegable adicional para "Riesgos y consecuencias"
with st.expander("Riesgos y consecuencias"):
    st.markdown(f"<div style='background-color:{color_ries_con}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
    st.write("Los microplásticos pueden tener efectos negativos en la salud de los seres vivos, ya que pueden ser ingeridos por animales y pasar a través de la cadena alimentaria. Además, pueden contaminar el agua y el suelo, afectando a los ecosistemas y a la biodiversidad.")
    st.markdown("</div>", unsafe_allow_html=True)