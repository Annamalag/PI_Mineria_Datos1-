import streamlit as st

# -----------------------------
# Configuración de la página
# -----------------------------
st.set_page_config(
    page_title="Plataforma de Streaming",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# Título principal
# -----------------------------
st.title("🎬 Análisis de Usuarios de una Plataforma de Streaming")

st.markdown(
"""
Bienvenido a la aplicación interactiva desarrollada para el proyecto de **Minería de Datos 1**

En esta aplicación podrás explorar el conjunto de datos, conocer el análisis exploratorio realizado,
visualizar los resultados del PCA y consultar las conclusiones finales del estudio.
"""
)

st.divider()

# -----------------------------
# Información general
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("👩‍🎓 Integrantes")

    st.write("""Ana Laura Malagueño""")

with col2:

    st.subheader("📚 Información")

    st.write("""
**Materia:** Minería de Datos

**Trabajo Integrador:** Proyecto Final

**Fecha:** Julio 2026
""")

st.divider()

# -----------------------------
# Objetivo
# -----------------------------

st.subheader("🎯 Objetivo")

st.write("""
Analizar el comportamiento de los usuarios de una plataforma de streaming mediante técnicas de preparación de datos,
Análisis Exploratorio de Datos (EDA) y Análisis de Componentes Principales (PCA), con el fin de identificar patrones
que contribuyan a una mejor comprensión del uso de la plataforma.
""")

st.divider()

# -----------------------------
# Dataset
# -----------------------------

st.subheader("📂 Dataset")

st.info(
"""
El dataset contiene información sobre usuarios de una plataforma de streaming,
incluyendo características demográficas, plan contratado, tiempo de visualización,
género favorito, país y tickets de soporte.
"""
)

st.divider()

# -----------------------------
# GitHub
# -----------------------------

st.subheader("💻 Repositorio")

st.write("https://github.com/Annamalag/PI_Mineria_Datos_1-")

# Ejemplo
# st.markdown("[Repositorio](https://github.com/usuario/repositorio)")

