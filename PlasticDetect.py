import streamlit as st
from PIL import Image

# Definir el estilo CSS para el color de fondo
color_reto = "#FFD700"  # Amarillo
color_defi = "#ADD8E6"  # Azul claro
color_ries_con = "#90EE90"  # Verde claro

st.header("<h1 style='text-align: center;'>MonomerFinder</h1>", unsafe_allow_html=True)

# Menú desplegable para "¿Qué es MonomerFinder?"
with st.expander("¿Qué es MonomerFinder?"):
    st.markdown(f"<div style='background-color:{color_reto}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
    st.write("MonomerFinder es una aplicación que facilita la identificación y clasificación de microplásticos presentes en imágenes capturadas por los propios usuarios. Para esto utiliza una IA que se encarga de analizar las imágenes y señalar la cantidad de microplásticos presentes y su tipo. Esta aplicación es el resultado del Reto 5 del Hackaton Coafina 2024: 'Microplásticos: un desafío ciudadano'.")
    st.markdown("</div>", unsafe_allow_html=True)

# Menú desplegable para "¿Qué son los microplásticos?"
with st.expander("¿Qué son los microplásticos?"):
    st.markdown(f"<div style='background-color:{color_defi}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
    st.write("Los microplásticos son diminutas partículas de plástico, generalmente con tamaños menores a 5 mm, que se han convertido en un problema ambiental global. Provienen de diversas fuentes, como la degradación de objetos plásticos más grandes, productos cosméticos y fibras sintéticas de la ropa. Estos diminutos fragmentos contaminan océanos, ríos, suelos e incluso el aire, siendo ingeridos por organismos marinos y terrestres, lo que puede llevar a su acumulación en la cadena alimentaria. Su persistencia en el medio ambiente y sus potenciales efectos negativos en la salud humana y de los ecosistemas son motivo de creciente preocupación entre científicos y ambientalistas.")
    st.markdown("</div>", unsafe_allow_html=True)

# Menú desplegable adicional para "Fuentes de microplásticos"
with st.expander("Fuentes de microplásticos"):
    st.markdown(f"<div style='background-color:{color_ries_con}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
    st.write("Los microplásticos pueden provenir de diversas fuentes, entre las que se destacan:")
    st.write("- Textiles:  El 70% de los textiles producidos hoy en día son de origen sintético y liberan grandes cantidades de microplásticos al medio ambiente. La liberación de fibras y sustancias sintéticas de la ropa se produce no solo a través del lavado y el uso, sino también durante la producción, el procesamiento y el transporte. Los geotextiles, que se utilizan comúnmente para sostener y reforzar las capas del suelo o como manto agrícola, también liberan microplásticos debido a la exposición a los rayos UV, daños físicos y un mantenimiento deficiente.")
    st.write("- Cosméticos y productos de cuidado personal: Un gran número de productos de cuidado personal todavía contienen microplásticos añadidos intencionadamente (por ejemplo, escarcha, microperlas en exfoliantes faciales y corporales). Estos productos ingresan al sistema de alcantarillado y a las plantas de tratamiento de aguas residuales. Aquí no se eliminan por completo y, por lo tanto, ingresan al medio ambiente.")
    st.write("- Pesca y acuicultura: Los microplásticos son liberados por: aguas grises de los buques que desembocan sin filtrar en el mar, la degradación de las líneas de pesca perdidas, pinturas y revestimientos marinos, residuos plásticos de un solo uso procedentes de la pesca y la acuicultura, y pérdida de contenedores marítimos con productos plásticos.")
    st.write("- Agricultura: Diversas fuentes agrícolas contribuyen a la propagación de microplásticos en el suelo, por ejemplo, a través de: el uso generalizado de películas de cultivo, tuberías de riego, comprimidos nutritivos, recubrimientos de semillas, lodos de depuradora de plantas de tratamiento de aguas residuales utilizados como fertilizante del suelo. Dado que la mitad de todos los lodos de depuradora de europa acaban de nuevo en tierra, se trata de un problema generalizado.")
    st.write("- Tráfico: La abrasión de los neumáticos, las marcas viales y los escombros de la carretera son fuentes de microplásticos ambientales. Se estima que solo la abrasión de los neumáticos genera más de 1,3 millones de toneladas de microplásticos en Europa cada año. El 'reciclaje' de neumáticos usados suele ser problemático, ya que los microplásticos se liberan directamente al medio ambiente a través de su uso en arrecifes artificiales, campos deportivos o patios escolares.")
    st.write("- Procesamiento de plásticos: Los pellets son perlas de plástico nuevas o recicladas que se utilizan como materia prima en la fabricación de la mayoría de los productos plásticos. Sin embargo, las pérdidas de gránulos, escamas y polvo de plástico se producen a lo largo de toda la cadena de valor de la producción, el transporte y el reciclaje de plástico. Además, el agua del proceso y las aguas residuales de la industria del plástico pueden estar muy contaminadas con microplásticos.")
    st.write("- Turismo: La eliminación inadecuada de los residuos de los turistas, los sistemas locales de gestión de residuos deficientes o inexistentes, la descarga incontrolada de aguas residuales de los cruceros y el consumo masivo de productos y envases de plástico de un solo uso en los países impulsados por el turismo, aumentan los aportes de microplásticos.")

    st.markdown("</div>", unsafe_allow_html=True)

# Añadir la opción de subir una foto
st.markdown("<h2 style='text-align: center;'>Subir una foto para análisis</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Elige una imagen...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Mostrar la imagen subida
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida', use_column_width=True)
    st.write("Imagen subida exitosamente. Procesando...")
