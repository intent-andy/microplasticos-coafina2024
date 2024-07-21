# Monomer Finder
MonomerFinder es una aplicación que facilita la identificación y clasificación de microplásticos presentes en imágenes capturadas por los propios usuarios. Para esto utiliza una IA que se encarga de analizar las imágenes y señalar la cantidad de microplásticos presentes y su tipo. Esta aplicación es el resultado del Reto 5 del Hackaton Coafina 2024: 'Microplásticos: un desafío ciudadano'.

# Procedimiento
Se desarrolló el Software de Conteo y Reconocimiento de Microplásticos, que permite contar y clasificar microplásticos en imágenes que funciona de la siguiente manera:

## Configuración del Dataset
1. Descarga y Configuración: Se descarga el dataset desde Roboflow y se configura en formato COCO. Se definen las rutas para los datos de entrenamiento y validación.
2. Registro del Dataset: Se registran los datasets de entrenamiento y validación.

## Configuración del Modelo
1. Entrenamiento: Se configura y entrena un modelo Faster R-CNN con un conjunto de parámetros predefinidos.
2. Predicción: Se carga el modelo entrenado y se configura el umbral de predicción.

## Procesamiento de Imágenes
1. Entrada: Solicita al usuario el nombre de la imagen y lee la imagen correspondiente.
2. Detección y Clasificación: Detecta microplásticos en la imagen, clasifica por color y dibuja las cajas delimitadoras.
3. Entrada de Datos de Ubicación: Solicita datos de ubicación y muestra un mapa con el marcador.

## Exportación de Resultados
1. Conteo de Microplásticos: Cuenta los microplásticos por color y guarda los resultados en un archivo CSV junto con los datos de ubicación.
2. Imagen Resultante: Guarda la imagen con las cajas delimitadoras y colores anotados.
##Resultados
    -Los resultados se guardan en microplastico_y_ubicaciones.csv.
    -La imagen con los rectángulos se guarda como image_with_boxes.jpg.

El siguiente paso fue desarrollar una página web que sirviera de interfaz para dicho software. En la misma se hace una breve presentación de qué es MonomerFinder y algunas definicione importantes para entender la relevancia de este proyecto.

El sitio web actual no tienen integrada la IA, solo muestra una ejemplo de cómo se vería el resultado final. El siguiente paso es terminar de desarrollar el sitio web para que tenga integrado el Software y que además se pueda crear una base de datos abierta para almacenar los resultados de los análisis y así contribuir con el desarrollo de nuevos estudios y análisis sobre los microplásticos en las playas del mundo.

# Referencias

1. Arbic, B.K., Mahu, E., Alexander, K., Buchan, P.M., Hermes, J., Kidwai, S., Kostianaia, E., Li, L., Lin, X., Mahadeo,  S.,  Maúre,  E.d.R.,  Munga,  C.,  M-Muslim,  A.,  Sant,  G.,  Seeyave,  S.,  &  Sun,  Z.  (2024).  Ocean Decade Vision 2030 White Papers – Challenge 9: Skills, Knowledge, Technology, and Participatory Decision-Making  for  All.  Paris,  UNESCO-IOC.  (The  Ocean  Decade  Series,  51.9.). https://doi.org/10.25607/k5pt-fp54
2. Hatje, V., Rayfuse, R., Polejack, P., Goddard, C., Jiang, C., Jones, D., Faloutsos, D., Fiedler, H., Akrofi, J., Sheps, K., Leung, K., Pinheiro, L.M., Pradhan, M., Castrillejo, M., Bustamante, P., Kershaw, P., Zitoun, R., Silva, S., & Kiefer, T. (2024). Ocean Decade Vision 2030 White Papers – Challenge 1: Understand and Beat Marine Pollution. Paris, UNESCO-IOC. (The Ocean Decade Series, 51.1). https://doi.org/10.25607/6m86-s908
3. Naciones Unidas. (2018). Naciones Unidas (2018). La Agenda 2030 y los Objetivos de Desarrollo Sostenible: una oportunidad para América Latina y el Caribe (LC/G.2681-P/Rev.3), Santiago
4. NESCO/COI. (2019). La ciencia que necesitamos para el océano que queremos: El Decenio de las Naciones Unidas de las Ciencias Oceánicas para el Desarrollo Sostenible (2021–2030). París. 24 pp. (Inglés) Folleto COI 2018-7
5. https://www.conasi.eu/blog/consejos-de-salud/consejos-de-salud-consejos-de-salud/ftalatos-disruptores-hormonales/
6. https://www.canada.ca/content/dam/hc-sc/documents/services/environmental-workplace-health/reports-publications/environmental
7. contaminants/human-biomonitoring-resources/bisphenol-a-canadians/bpa-eng.pdf
8. https://www.canada.ca/en/health-canada/services/environmental-workplace-health/reports-publications/environmental-contaminants/human-biomonitoring-resources/2-ethylhexyl-phthalate-canadians.html
9. https://www.canada.ca/en/health-canada/services/chemicals-product-safety/phthalates.html
10. https://www.canada.ca/en/health-canada/services/chemical-substances/fact-sheets/chemicals-glance/polybrominated-diphenyl-ethers-public-summary.html
11. https://www.canada.ca/en/health-canada/services/food-nutrition/food-safety/chemical-contaminants/environmental-contaminants/polybrominated-diphenyl-ethers-pbdes/fact-sheet-polybrominated-diphenyl-ethers-pbdes-fish.html
12. https://www.canada.ca/en/environment-climate-change/services/evaluating-existing-substances/microbeads-science-summary.html#s05
13. https://wasserdreinull.de/en/knowledge/microplastics/?gad_source=1&gclid=CjwKCAjwnei0BhB-EiwAA2xuBozZhqlqwWj2oibhaJ4ng4Q_oSjlROwAm8NNc1RQQgnVRKLoK7Y0rhoC81oQAvD_BwE
