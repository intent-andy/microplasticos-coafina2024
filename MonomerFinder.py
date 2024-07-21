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
        st.image("RaceforWater_PeterCharaf_MicroplasticsAzores_(2).jpg", use_column_width=True)
        st.markdown(f"<div style='background-color:{color_page}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
        st.write("MonomerFinder es una aplicación que facilita la identificación y clasificación de microplásticos presentes en imágenes capturadas por los propios usuarios. Para esto utiliza una IA que se encarga de analizar las imágenes y señalar la cantidad de microplásticos presentes y su tipo. Esta aplicación es el resultado del Reto 5 del Hackaton Coafina 2024: 'Microplásticos: un desafío ciudadano'.")
        st.markdown("</div>", unsafe_allow_html=True)

    # Menú desplegable adicional para "Fuentes de microplásticos"
    with st.expander("Fuentes de microplásticos"):
        st.image("Pollution_on_Land.jpg", use_column_width=True)
        st.markdown(f"<div style='background-color:{color_page}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
        st.write("Los microplásticos pueden provenir de diversas fuentes, entre las que se destacan:")
        st.write("- Textiles:  El 70% de los textiles producidos hoy en día son de origen sintético y liberan grandes cantidades de microplásticos al medio ambiente. La liberación de fibras y sustancias sintéticas de la ropa se produce no solo a través del lavado y el uso, sino también durante la producción, el procesamiento y el transporte. Los geotextiles, que se utilizan comúnmente para sostener y reforzar las capas del suelo o como manto agrícola, también liberan microplásticos debido a la exposición a los rayos UV, daños físicos y un mantenimiento deficiente.")
        st.write("- Cosméticos y productos de cuidado personal: Un gran número de productos de cuidado personal todavía contienen microplásticos añadidos intencionadamente (por ejemplo, escarcha, microperlas en exfoliantes faciales y corporales). Estos productos ingresan al sistema de alcantarillado y a las plantas de tratamiento de aguas residuales. Aquí no se eliminan por completo y, por lo tanto, ingresan al medio ambiente.")
        st.write("- Pesca y acuicultura: Los microplásticos son liberados por: aguas grises de los buques que desembocan sin filtrar en el mar, la degradación de las líneas de pesca perdidas, pinturas y revestimientos marinos, residuos plásticos de un solo uso procedentes de la pesca y la acuicultura, y pérdida de contenedores marítimos con productos plásticos.")
        st.write("- Agricultura: Diversas fuentes agrícolas contribuyen a la propagación de microplásticos en el suelo, por ejemplo, a través de: el uso generalizado de películas de cultivo, tuberías de riego, comprimidos nutritivos, recubrimientos de semillas, lodos de depuradora de plantas de tratamiento de aguas residuales utilizados como fertilizante del suelo. Dado que la mitad de todos los lodos de depuradora de europa acaban de nuevo en tierra, se trata de un problema generalizado.")
        st.write("- Tráfico: La abrasión de los neumáticos, las marcas viales y los escombros de la carretera son fuentes de microplásticos ambientales. Se estima que solo la abrasión de los neumáticos genera más de 1,3 millones de toneladas de microplásticos en Europa cada año. El 'reciclaje' de neumáticos usados suele ser problemático, ya que los microplásticos se liberan directamente al medio ambiente a través de su uso en arrecifes artificiales, campos deportivos o patios escolares.")
        st.write("- Procesamiento de plásticos: Los pellets son perlas de plástico nuevas o recicladas que se utilizan como materia prima en la fabricación de la mayoría de los productos plásticos. Sin embargo, las pérdidas de gránulos, escamas y polvo de plástico se producen a lo largo de toda la cadena de valor de la producción, el transporte y el reciclaje de plástico. Además, el agua del proceso y las aguas residuales de la industria del plástico pueden estar muy contaminadas con microplásticos.")
        st.write("- Turismo: La eliminación inadecuada de los residuos de los turistas, los sistemas locales de gestión de residuos deficientes o inexistentes, la descarga incontrolada de aguas residuales de los cruceros y el consumo masivo de productos y envases de plástico de un solo uso en los países impulsados por el turismo, aumentan los aportes de microplásticos.")
        st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Menú desplegable para "¿Qué son los microplásticos?"
    with st.expander("¿Qué son los microplásticos?"):
        st.image("Microplastic.jpg", use_column_width=True)
        st.markdown(f"<div style='background-color:{color_page}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
        st.write("Los microplásticos son diminutas partículas de plástico, generalmente con tamaños menores a 5 mm, que se han convertido en un problema ambiental global. Provienen de diversas fuentes, como la degradación de objetos plásticos más grandes, productos cosméticos y fibras sintéticas de la ropa. Estos diminutos fragmentos contaminan océanos, ríos, suelos e incluso el aire, siendo ingeridos por organismos marinos y terrestres, lo que puede llevar a su acumulación en la cadena alimentaria. Su persistencia en el medio ambiente y sus potenciales efectos negativos en la salud humana y de los ecosistemas son motivo de creciente preocupación entre científicos y ambientalistas.")
        st.markdown("</div>", unsafe_allow_html=True)

    # Menú desplegable para "Componentes tóxicos presentes en los plásticos"
    with st.expander("Componentes tóxicos presentes en los plásticos"):
        st.image("P061337-98078.jpg", use_column_width=True)
        st.markdown(f"<div style='background-color:{color_page}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
        st.write("- Polibutileno tereftalato (PBT): Es un polímero termoplástico lineal que se fabrica para fines específicos, incluso para su uso en productos de cuidado personal (como exfoliantes, productos de baño, limpiadores faciales, pastas dentales). También se pueden utilizar en otros usos de consumo, incluidos productos de limpieza y tóneres de impresoras, y en productos industriales como medios abrasivos (por ejemplo, chorreado de plástico), industria (por ejemplo, exploración de petróleo y gas, impresión textil y moldeo automotriz), otros productos plásticos (aplicaciones antideslizantes) y aplicaciones médicas. \n Es probable que los productos que contienen PBT y se tiran por el desagüe se liberen en el medio acuático después del tratamiento de las aguas residuales. Los estudios han demostrado que los microplásticos, Incluido el PBT, están presentes en el medio ambiente y que pueden residir en el medio ambiente durante mucho tiempo. Se ha demostrado que el PBT provoca efectos a corto y largo plazo en organismos de laboratorio, y además este compuesto es capaz de absorber contaminantes del medio ambiente y liberarlos en el organismo que consuma o absorba el microplástico.\n El PBT es fácilmente absorbido por una variedad de organismos, incluidos peces, mejillones y varios tipos de zooplancton, los posibles efectos negativos de la absorción o ingesta de estos compuestos por parte de animales afectan al hígado por el agotamiento del glucógeno y la vacuolización de grasas, se encontró una regulación negativa significativa de la expresión génica de la coriogenina en los machos y una regulación negativa significativa de la vitelogenina, la coriogenina y el receptor de estrógeno alfa en las hembras.")
        st.write("- El bisfenol A (BPA): es una sustancia química sintética que se utiliza como monómero para producir ciertos plásticos de policarbonato y resinas epoxi. \n Los plásticos de policarbonato y las resinas epoxi se utilizan ampliamente en productos de consumo. Algunos ejemplos son los envases de alimentos y bebidas, los equipos deportivos y de seguridad, la electrónica, las piezas de automóviles y los dispositivos médicos. El BPA también se utiliza en papel térmico recubrimientos para recibos, etiquetas de recetas y billetes de avión.\n El BPA se absorbe con facilidad y se metaboliza ampliamente en el organismo. Este compuesto y sus metabolitos se miden habitualmente en orina como BPA total. Estas mediciones reflejan la exposición reciente al compuesto.\n Los riesgos potenciales para la salud humana derivados de la exposición al BPA incluyen efectos sobre el hígado y los riñones. También incluyen efectos potenciales sobre la reproducción, el desarrollo, el neurodesarrollo y el comportamiento.")
        st.write("- Los ftalatos: También conocidos como ésteres de ácido ftálico, son un conjunto de más de 80 compuestos químicos sintéticos utilizados en numerosas industrias como plastificadores, y cuya función principal es la de dar mayor flexibilidad y elasticidad a los polímeros rígidos. \n Los estudios con animales han demostrado que la exposición al DEHP puede tener efectos sobre el desarrollo y la reproducción. También puede afectar al hígado y los riñones. El Centro Internacional de Investigaciones sobre el cáncer ha clasificado el DEHP como posiblemente cancerígeno para los seres humanos. ,\n Están presentes en productos de cuidado personal como cosméticos, también en productos de construcción y renovación como lubricantes y grasas, pinturas, revestimientos, adhesivos, selladores, textiles. Puede encontrarse en artículos eléctricos y electrónicos, también en juguetes y en algunos materiales de envasado de alimentos y plásticos de tipo PVC.")
        st.write("- Los éteres difenílicos polibromados (PBDE): son sustancias producidas comercialmente que se utilizan como retardantes de llama para frenar la ignición y propagación del fuego en una amplia variedad de productos de consumo como las bases de alfombras, espuma para muebles, electrodomésticos y los equipos eléctricos y electrónicos. Los PBDE pueden encontrarse en el medio ambiente en todo el mundo. Los efectos críticos o importantes considerados en la evaluación de la salud humana eran efectos sobre el desarrollo neurológico (como cambios en el movimiento y el comportamiento).")
        st.markdown("</div>", unsafe_allow_html=True)

# Menú desplegable para "Objetivos del proyecto"
with st.expander("Objetivos del proyecto"):
    st.markdown(f"<div style='background-color:{color_page}; padding: 5px; border-radius: 5px;'>", unsafe_allow_html=True)
    st.write("- Proporcionar una herramienta de uso libre para incentivar la colaboración ciudadana en la identificación de los microplásticos presentes en las playas del mundo.")
    st.write("- Difundir conocimientos y recomendaciones de acción a los usuarios de esta herramienta basándose en los resultados obtenidos de la identificación.")
    st.write("- Sentar las bases para la creación de una base de datos abiertos y así aportar al desarrollo de nuevos estudios y análisis siguiendo los Objetivos de Desarrollo Sostenible de la ONU y contribuyendo con los retos 1 y 9 de la Década Oceánica.")
    
    # Imágenes de los Objetivos de Desarrollo Sostenible
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.image("S_SDG_Icons-01-06.jpg", use_column_width=True)
    
    with col2:
        st.image("S_SDG_Icons-01-14.jpg", use_column_width=True)

    with col3:
        st.image("S_SDG_Icons-01-17.jpg", use_column_width=True)

    # Imágenes de los retos de la Década Oceánica
    col1, col2, col3, col4, col5 = st.columns([1, 3, 1, 3, 1])
    with col2:
        st.image("Understand-and-beat-marine-pollution.webp", caption="Desafío 1: Comprender y vencer la contaminación marina", use_column_width=True)

    with col4:
        st.image("Skills-knowledge-and-technology-for-all.webp", caption="Desafío 9: Habilidades, conocimientos y tecnología para todos", use_column_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Software de MonomerFinder
st.markdown("""
<style>
.centered {
    text-align: center;
}
</style>
<div class="centered">
    <h1>¡Vamos a identificar y contar microplásticos!</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Estes es un ejemplo de cómo se verá la aplicación MonomerFinder en la versión final. A continuación, se presentan las instrucciones para subir una imagen y obtener los resultados del análisis:
1. Ten a la mano tu ubicación.
2. Las fotos deben ser de microplásticos filtrados, es decir, sin ningún otro material en lo posible.
3. Las fotos deben ser claras para obtener mejores resultados.
""")

# Solicitar al usuario que ingrese una imagen
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

st.write("En este ejemplo se ha cargado una imagen de microplásticos filtrados para su análisis, haz clic en el botón 'Subir archivo' para continuar.")

if st.button("Subir archivo"):
    uploaded_file = "d--52-_jpg.rf.086e80a05c54229e7189ec3bc38c9940.jpg"
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)
    st.success("¡La imagen ha sido cargada con éxito!")


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
# Solicitar los datos de ubicación
st.write("En este ejemplo se ha ingresado la ubicación de dicha imagen, pero se puede cambiar los valores de latitud y longitud para ver cómo se actualiza el mapa.")
latitud = st.number_input('Latitud', value=-0.828698914155737, format="%.6f")
longitud = st.number_input('Longitud', value=-90.82966201810576, format="%.6f")
descripcion = st.text_input('Descripción de la ubicación (opcional)', value="Galápagos")

# Mapa con la ubicación ingresada
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

# Botón para analizar la imagen
if st.button("Analizar imagen"):
    st.success("¡La imagen ha sido analizada con éxito!")
    
    # Mostrar los resultados del análisis
    st.markdown("""
        <style>
        .center {
            display: flex;
            justify-content: center;
        }
        </style>
        <div class="center">
            <h2>Resultados del análisis</h2>
        </div>
        """, unsafe_allow_html=True)
    st.write("Una vez procesada la imagen con el modelo de IA, se obtuvieron los siguientes resultados:")
    df = pd.DataFrame({
    'data_column': [1, 2],
    'microplastic_type': ['Blanco', 'Rojo']
    })
    
    # Mostrar los resultados en un gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(df['microplastic_type'], df['data_column'])
    ax.set_xlabel('Cantidad de microplásticos')
    ax.set_ylabel('Tipo de microplástico')
    st.pyplot(fig)

    # Mostrar los resultados en una tabla
    st.write("A continuación se presenta una tabla con los resultados obtenidos:")
    st.table(df)

# Protocolo de estimación de microplásticos en la arena

st.markdown("""
    <style>
    .centered {
        text-align: center;
    }
    </style>
    <div class="centered">
        <h2>Protocolo de estimación de microplásticos en la arena</h2>
    </div>
    """, unsafe_allow_html=True)
