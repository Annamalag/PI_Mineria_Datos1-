Trabajo Integrador de mineria datos 1

Integrante: Malagueño Ana Laura

Información general:Este proyecto corresponde al trabajo integrador de la materia Minería de Datos I.  
Se desarrolla un análisis completo de un dataset de usuarios de una plataforma de streaming utilizando técnicas de análisis de datos y visualización.  
El objetivo es comprender el comportamiento de los usuarios, identificar patrones de consumo y generar insights útiles para la toma de decisiones.  
Se aplican procesos de limpieza, análisis exploratorio y reducción de dimensionalidad.

Objetivo del proyect: 
El objetivo del proyecto es analizar el comportamiento de usuarios de una plataforma de streaming mediante técnicas de minería de datos.  
Se busca identificar patrones de consumo, diferencias entre planes de suscripción y variables que influyen en el uso del servicio.  
Además, se aplica PCA para reducir la dimensionalidad del dataset y facilitar la visualización de estructuras internas en los datos.  
El análisis permite generar información útil para segmentación de usuarios y toma de decisiones

Dataset: 
El dataset contiene información de 8160 usuarios de una plataforma de streaming.  
Incluye variables como edad, tiempo de visualización mensual, país, género favorito, plan de suscripción y tickets de soporte.  
Los datos permiten analizar el comportamiento de consumo de contenido digital.  
El dataset fue previamente limpiado quedando un total de 8034 y para eliminar valores nulos, inconsistencias y outliers.  
Se trabajó con variables numéricas y categóricas relevantes para el análisis.

Estructura del repositorio: El repositorio está organizado de la siguiente manera:

- `app/` → Aplicación Streamlit
- `app/Home.py` → Página principal
- `app/pages/` → Páginas del análisis (Dataset, EDA, PCA, Conclusiones)
- `data/` → Dataset crudo y limpio
- `Notebooks/` → Análisis exploratorio y pruebas
- `requirements.txt` → Dependencias del proyecto
- `README.md` → Documentación general

Preparación y calidad de datos: Se realizó un proceso de limpieza del dataset que incluyó tratamiento de valores nulos, corrección de inconsistencias, normalizacion y eliminación de duplicados. 
Las variables categóricas fueron normalizadas para asegurar consistencia en el análisis.  
Las variables numéricas fueron escaladas para su uso en técnicas como PCA.  
Se verificó la calidad general del dataset para garantizar resultados confiables.  
Estas decisiones mejoraron la calidad del análisis posterior.

Resumen del análisis exploratorio: permitió identificar patrones importantes en los usuarios.  
Se observaron diferencias en el tiempo de visualización según el tipo de plan.  
Se analizaron relaciones entre variables como edad, consumo y tickets de soporte.  
Se detectaron segmentos de usuarios con comportamientos diferenciados.  
El EDA permitió comprender la estructura general del dataset y sus relaciones principales.

Reducción de dimensionalidad: el PCA permitió evaluar la estructura de las variables numéricas del conjunto de datos y determinar cuánto de la información puede resumirse en un menor número de dimensiones. Las dos primeras componentes explican el 67,07% de la variabilidad total, mientras que la tercera aporta el 32,93% restante. Dado que la varianza se distribuye de manera equilibrada entre las tres componentes, no existe una reducción significativa de la dimensionalidad sin perder información relevante

Visualización interactiva: El proyecto incluye una aplicación desarrollada en Streamlit.  
Permite explorar el dataset, visualizar análisis exploratorio y resultados del PCA.  
Los gráficos son interactivos y permiten entender mejor el comportamiento de los datos.  
El usuario puede filtrar variables y observar cambios en tiempo real.  
Esto mejora la comprensión del análisis de forma dinámica.

Conclusiones: El proyecto permitió analizar el comportamiento de usuarios de una plataforma de streaming.
Se identificaron patrones claros en el consumo de contenido y diferencias entre planes de suscripción.
El PCA facilitó la visualización de estructuras ocultas en los datos.
Los resultados obtenidos pueden ser utilizados para segmentación de usuarios.
El trabajo demuestra la utilidad de la minería de datos para la toma de decisiones.


Cómo ejecutar localmente:  "1. Clonar el repositorio:
   bass
   git clone https://github.com/Annamalag/PI_Mineria_Datos_1-.git
   2.Instalar dependencias:
   pip install -r requirements.txt
   3.Ejecutar la aplicación:
   python -m streamlit run app/Home.py"



