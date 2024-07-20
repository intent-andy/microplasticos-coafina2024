#Software de Conteo y Reconocimiento de Microplásticos

##Bienvenida
Este software permite contar y clasificar microplásticos en imágenes. Para obtener los mejores resultados:

1. Ten a mano tu ubicación.
2. Asegúrate de que las fotos contengan solo microplásticos.
3. Utiliza fotos claras.

##Configuración del Dataset
1. Descarga y Configuración: Se descarga el dataset desde Roboflow y se configura en formato COCO. Se definen las rutas para los datos de entrenamiento y validación.
2. Registro del Dataset: Se registran los datasets de entrenamiento y validación.

##Configuración del Modelo
1. Entrenamiento: Se configura y entrena un modelo Faster R-CNN con un conjunto de parámetros predefinidos.
2. Predicción: Se carga el modelo entrenado y se configura el umbral de predicción.

##Procesamiento de Imágenes
1. Entrada: Solicita al usuario el nombre de la imagen y lee la imagen correspondiente.
2. Detección y Clasificación: Detecta microplásticos en la imagen, clasifica por color y dibuja las cajas delimitadoras.
3. Entrada de Datos de Ubicación: Solicita datos de ubicación y muestra un mapa con el marcador.

##Exportación de Resultados
1. Conteo de Microplásticos: Cuenta los microplásticos por color y guarda los resultados en un archivo CSV junto con los datos de ubicación.
2. Imagen Resultante: Guarda la imagen con las cajas delimitadoras y colores anotados.
##Resultados
    -Los resultados se guardan en microplastico_y_ubicaciones.csv.
    -La imagen con los rectángulos se guarda como image_with_boxes.jpg.
