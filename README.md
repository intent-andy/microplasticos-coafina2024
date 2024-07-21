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