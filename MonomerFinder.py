import streamlit as st
from PIL import Image
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Cargar la imagen del banner
banner_image = Image.open("Microplastics_in_the_natural_environment.jpg")

# Rotar la imagen 90 grados
banner_image_rotated = banner_image.rotate(90, expand=True)

# Mostrar la imagen del banner
st.image(banner_image_rotated, use_column_width=True)

# Definir el estilo CSS para el color de fondo
color_page = "#756AB6"

st.markdown("""
<style>
.centered {
    text-align: center;
}
</style>
<div class="centered">
    <h1>MonomerFinder: Identificación de microplásticos en imágenes</h1>
</div>
""", unsafe_allow_html=True)

# Separar en columnas el contenido
col1, col2 = st.columns([1, 1])

with col1:
    # Menú desplegable para "¿Qué es MonomerFinder?"
    with st.expander("¿Qué es MonomerFinder?"):
        st.markdown(f"<div style='background-color:{color_page}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
        st.write("MonomerFinder es una aplicación que facilita la identificación y clasificación de microplásticos presentes en imágenes capturadas por los propios usuarios. Para esto utiliza una IA que se encarga de analizar las imágenes y señalar la cantidad de microplásticos presentes y su tipo. Esta aplicación es el resultado del Reto 5 del Hackaton Coafina 2024: 'Microplásticos: un desafío ciudadano'.")
        st.image("RaceforWater_PeterCharaf_MicroplasticsAzores_(2).jpg", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Menú desplegable adicional para "Fuentes de microplásticos"
    with st.expander("Fuentes de microplásticos"):
        st.markdown(f"<div style='background-color:{color_page}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
        st.write("Los microplásticos pueden provenir de diversas fuentes, entre las que se destacan:")
        st.write("- Textiles:  El 70% de los textiles producidos hoy en día son de origen sintético y liberan grandes cantidades de microplásticos al medio ambiente. La liberación de fibras y sustancias sintéticas de la ropa se produce no solo a través del lavado y el uso, sino también durante la producción, el procesamiento y el transporte. Los geotextiles, que se utilizan comúnmente para sostener y reforzar las capas del suelo o como manto agrícola, también liberan microplásticos debido a la exposición a los rayos UV, daños físicos y un mantenimiento deficiente.")
        st.write("- Cosméticos y productos de cuidado personal: Un gran número de productos de cuidado personal todavía contienen microplásticos añadidos intencionadamente (por ejemplo, escarcha, microperlas en exfoliantes faciales y corporales). Estos productos ingresan al sistema de alcantarillado y a las plantas de tratamiento de aguas residuales. Aquí no se eliminan por completo y, por lo tanto, ingresan al medio ambiente.")
        st.write("- Pesca y acuicultura: Los microplásticos son liberados por: aguas grises de los buques que desembocan sin filtrar en el mar, la degradación de las líneas de pesca perdidas, pinturas y revestimientos marinos, residuos plásticos de un solo uso procedentes de la pesca y la acuicultura, y pérdida de contenedores marítimos con productos plásticos.")
        st.write("- Agricultura: Diversas fuentes agrícolas contribuyen a la propagación de microplásticos en el suelo, por ejemplo, a través de: el uso generalizado de películas de cultivo, tuberías de riego, comprimidos nutritivos, recubrimientos de semillas, lodos de depuradora de plantas de tratamiento de aguas residuales utilizados como fertilizante del suelo. Dado que la mitad de todos los lodos de depuradora de europa acaban de nuevo en tierra, se trata de un problema generalizado.")
        st.write("- Tráfico: La abrasión de los neumáticos, las marcas viales y los escombros de la carretera son fuentes de microplásticos ambientales. Se estima que solo la abrasión de los neumáticos genera más de 1,3 millones de toneladas de microplásticos en Europa cada año. El 'reciclaje' de neumáticos usados suele ser problemático, ya que los microplásticos se liberan directamente al medio ambiente a través de su uso en arrecifes artificiales, campos deportivos o patios escolares.")
        st.write("- Procesamiento de plásticos: Los pellets son perlas de plástico nuevas o recicladas que se utilizan como materia prima en la fabricación de la mayoría de los productos plásticos. Sin embargo, las pérdidas de gránulos, escamas y polvo de plástico se producen a lo largo de toda la cadena de valor de la producción, el transporte y el reciclaje de plástico. Además, el agua del proceso y las aguas residuales de la industria del plástico pueden estar muy contaminadas con microplásticos.")
        st.write("- Turismo: La eliminación inadecuada de los residuos de los turistas, los sistemas locales de gestión de residuos deficientes o inexistentes, la descarga incontrolada de aguas residuales de los cruceros y el consumo masivo de productos y envases de plástico de un solo uso en los países impulsados por el turismo, aumentan los aportes de microplásticos.")
        st.image("Pollution_on_Land.jpg", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Menú desplegable para "¿Qué son los microplásticos?"
    with st.expander("¿Qué son los microplásticos?"):
        st.markdown(f"<div style='background-color:{color_page}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
        st.write("Los microplásticos son diminutas partículas de plástico, generalmente con tamaños menores a 5 mm, que se han convertido en un problema ambiental global. Provienen de diversas fuentes, como la degradación de objetos plásticos más grandes, productos cosméticos y fibras sintéticas de la ropa. Estos diminutos fragmentos contaminan océanos, ríos, suelos e incluso el aire, siendo ingeridos por organismos marinos y terrestres, lo que puede llevar a su acumulación en la cadena alimentaria. Su persistencia en el medio ambiente y sus potenciales efectos negativos en la salud humana y de los ecosistemas son motivo de creciente preocupación entre científicos y ambientalistas.")
        st.image("Microplastic.jpg", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Menú desplegable para "Componentes tóxicos presentes en los plásticos"
    with st.expander("Componentes tóxicos presentes en los plásticos"):
        st.markdown(f"<div style='background-color:{color_page}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
        st.write("- Polibutileno tereftalato (PBT): Es un polímero termoplástico lineal que se fabrica para fines específicos, incluso para su uso en productos de cuidado personal (como exfoliantes, productos de baño, limpiadores faciales, pastas dentales). También se pueden utilizar en otros usos de consumo, incluidos productos de limpieza y tóneres de impresoras, y en productos industriales como medios abrasivos (por ejemplo, chorreado de plástico), industria (por ejemplo, exploración de petróleo y gas, impresión textil y moldeo automotriz), otros productos plásticos (aplicaciones antideslizantes) y aplicaciones médicas. \n \n Es probable que los productos que contienen PBT y se tiran por el desagüe se liberen en el medio acuático después del tratamiento de las aguas residuales. Los estudios han demostrado que los microplásticos, Incluido el PBT, están presentes en el medio ambiente y que pueden residir en el medio ambiente durante mucho tiempo. Se ha demostrado que el PBT provoca efectos a corto y largo plazo en organismos de laboratorio, y además este compuesto es capaz de absorber contaminantes del medio ambiente y liberarlos en el organismo que consuma o absorba el microplástico.")
        st.write("El PBT es fácilmente absorbido por una variedad de organismos, incluidos peces, mejillones y varios tipos de zooplancton, los posibles efectos negativos de la absorción o ingesta de estos compuestos por parte de animales afectan al hígado por el agotamiento del glucógeno y la vacuolización de grasas, se encontró una regulación negativa significativa de la expresión génica de la coriogenina en los machos y una regulación negativa significativa de la vitelogenina, la coriogenina y el receptor de estrógeno alfa en las hembras.")
        st.write("- El bisfenol A (BPA): es una sustancia química sintética que se utiliza como monómero para producir ciertos plásticos de policarbonato y resinas epoxi.")
        st.write("Los plásticos de policarbonato y las resinas epoxi se utilizan ampliamente en productos de consumo. Algunos ejemplos son los envases de alimentos y bebidas, los equipos deportivos y de seguridad, la electrónica, las piezas de automóviles y los dispositivos médicos. El BPA también se utiliza en papel térmico recubrimientos para recibos, etiquetas de recetas y billetes de avión.")
        st.write("El BPA se absorbe con facilidad y se metaboliza ampliamente en el organismo. Este compuesto y sus metabolitos se miden habitualmente en orina como BPA total. Estas mediciones reflejan la exposición reciente al compuesto.")
        st.write("Los riesgos potenciales para la salud humana derivados de la exposición al BPA incluyen efectos sobre el hígado y los riñones. También incluyen efectos potenciales sobre la reproducción, el desarrollo, el neurodesarrollo y el comportamiento.")
        st.write("- Los ftalatos: También conocidos como ésteres de ácido ftálico, son un conjunto de más de 80 compuestos químicos sintéticos utilizados en numerosas industrias como plastificadores, y cuya función principal es la de dar mayor flexibilidad y elasticidad a los polímeros rígidos.")
        st.write("Los estudios con animales han demostrado que la exposición al DEHP puede tener efectos sobre el desarrollo y la reproducción. También puede afectar al hígado y los riñones. El Centro Internacional de Investigaciones sobre el cáncer ha clasificado el DEHP como posiblemente cancerígeno para los seres humanos.")
        st.write("Están presentes en productos de cuidado personal como cosméticos, también en productos de construcción y renovación como lubricantes y grasas, pinturas, revestimientos, adhesivos, selladores, textiles. Puede encontrarse en artículos eléctricos y electrónicos, también en juguetes y en algunos materiales de envasado de alimentos y plásticos de tipo PVC.")
        st.write("- Los éteres difenílicos polibromados (PBDE): son sustancias producidas comercialmente que se utilizan como retardantes de llama para frenar la ignición y propagación del fuego en una amplia variedad de productos de consumo como las bases de alfombras, espuma para muebles, electrodomésticos y los equipos eléctricos y electrónicos. Los PBDE pueden encontrarse en el medio ambiente en todo el mundo. Los efectos críticos o importantes considerados en la evaluación de la salud humana eran efectos sobre el desarrollo neurológico (como cambios en el movimiento y el comportamiento).")
    

# Software de MonomerFinder
st.write("""
<style>
.centered {
    text-align: center;
}
</style>
<div class="centered">
    <h1>¡Vamos a identificar y contar microplásticos!</h1>
</div>
""", unsafe_allow_html=True)
st.write("Recuerda:")
st.write("1-.Tener a la mano tu ubicación")
st.write("2-.La fotos deben ser de microplásticos filtrados es decir sin ningún otro material en lo posible")
st.write("3-.Las fotos deben ser claras para obtener mejores resultados")

# Solicitar al usuario que ingrese el nombre del archivo de imagen
st.markdown("""
    <style>
    .center {
        display: flex;
        justify-content: center;
    }
    </style>
    <div class="center">
        <h2>Sube tu imagen</h2>
    </div>
    """, unsafe_allow_html=True)
uploaded_file = st.file_uploader(" ", type=["jpg", "jpeg", "png"])

# Ubicación en el mapa
st.markdown("""
    <style>
    .center {
        display: flex;
        justify-content: center;
    }
    </style>
    <div class="center">
        <h2>Ingresa tu ubicación</h2>
    </div>
    """, unsafe_allow_html=True)

def solicitar_datos():
  latitud = st.number_input('Latitud', value=0.0, format="%.6f")
  longitud = st.number_input('Longitud', value=0.0, format="%.6f")
  descripcion = st.text_input('Descripción de la ubicación (opcional)')

  # Ubicación en el mapa
  st.markdown("""
      <style>
      .center {
          display: flex;
          justify-content: center;
      }
      </style>
      <div class="center">
          <h2>Ubicación en el mapa</h2>
      </div>
      """, unsafe_allow_html=True)
  st.map(pd.DataFrame({'lat': [latitud], 'lon': [longitud], 'zoom': [1]}))

# Solicitar los datos
ubicacion_data = []
entrada = solicitar_datos()
if entrada:
    ubicacion_data.append(entrada)