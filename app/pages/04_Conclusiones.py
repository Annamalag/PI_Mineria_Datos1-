import streamlit as st

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(page_title="Conclusiones", page_icon="📌", layout="wide")

st.title("📌 Conclusiones del Proyecto")

st.write("Resumen final del análisis del dataset de streaming.")

# =========================
# INTRO
# =========================
st.subheader("🧠 Resumen general")

st.markdown("""
Este proyecto permitió analizar el comportamiento de usuarios de una plataforma de streaming
mediante un proceso completo de análisis de datos:

- Limpieza y preparación del dataset  
- Análisis exploratorio (EDA)  
- Reducción de dimensionalidad (PCA)  
- Visualización de patrones de usuarios  
""")

# =========================
# HALLAZGOS PRINCIPALES
# =========================
st.subheader("📊 Hallazgos principales")

st.markdown("""
✔️ Los usuarios presentan distintos niveles de consumo de contenido mensual.  

✔️ El tiempo de visualización es una variable clave para identificar patrones de comportamiento.  

✔️ Los tickets de soporte permiten detectar posibles usuarios con problemas o baja satisfacción.  

✔️ Existen diferencias claras entre planes de suscripción en términos de uso.  

✔️ El PCA permitió reducir variables y visualizar agrupamientos naturales entre usuarios.  
""")

# =========================
# PCA
# =========================
st.subheader("📉 Aporte del PCA")

st.markdown("""
El análisis de componentes principales permitió:

- Reducir la dimensionalidad del dataset  
- Identificar relaciones ocultas entre variables  
- Visualizar usuarios con comportamientos similares  
- Facilitar futuras tareas de clustering o machine learning  
""")

# =========================
# INSIGHTS DE NEGOCIO
# =========================
st.subheader("💡 Insights de negocio")

st.markdown("""
📌 Los usuarios con mayor tiempo de visualización representan el núcleo más activo de la plataforma.  

📌 El tipo de plan influye directamente en el comportamiento de consumo.  

📌 Los tickets de soporte pueden ser un indicador de riesgo de cancelación.  

📌 Existen segmentos claros de usuarios que podrían usarse para campañas de marketing personalizadas.  
""")

# =========================
# RECOMENDACIONES
# =========================
st.subheader("🚀 Recomendaciones")

st.markdown("""
- Implementar segmentación de usuarios (clustering futuro).  
- Personalizar recomendaciones según comportamiento de visualización.  
- Analizar usuarios con alto número de tickets para mejorar retención.  
- Optimizar planes de suscripción según patrones de consumo.  
""")

# =========================
# CIERRE
# =========================
st.success("✔️ Proyecto finalizado correctamente")

st.markdown("📌 Este análisis sirve como base para modelos predictivos y estrategias de negocio.")
