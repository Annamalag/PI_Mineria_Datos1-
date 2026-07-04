import streamlit as st
import pandas as pd

# ==================================
# Configuración de la página
# ==================================
st.set_page_config(
    page_title="Dataset",
    page_icon="📊",
    layout="wide"
)

# ==================================
# Cargar dataset
# ==================================
df = pd.read_csv("data/cleaned_dataset.csv")

# ==================================
# Título
# ==================================
st.title("📊 Dataset")

st.markdown("""
En esta sección se presenta una descripción general del conjunto de datos utilizado en el proyecto,
incluyendo sus dimensiones, estructura, calidad y las principales transformaciones realizadas durante
la etapa de preparación.
""")

st.divider()

# ==================================
# Métricas
# ==================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Registros", df.shape[0])

with col2:
    st.metric("📋 Variables", df.shape[1])

with col3:
    st.metric("🌎 Países", df["country"].nunique())

with col4:
    st.metric("💳 Planes", df["subscription_plan"].nunique())

st.divider()

# ==================================
# Vista previa
# ==================================

st.subheader("Vista previa del dataset")

st.dataframe(df.head())

st.divider()

# ==================================
# Información
# ==================================

st.subheader("Información de las variables")

info = pd.DataFrame({
    "Variable": df.columns,
    "Tipo de dato": df.dtypes.astype(str),
    "Valores nulos": df.isna().sum().values
})

st.dataframe(info)

st.divider()

# ==================================
# Calidad
# ==================================

st.subheader("Resumen de calidad")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Valores faltantes",
        int(df.isna().sum().sum())
    )

with col2:

    st.metric(
        "Registros duplicados",
        int(df.duplicated().sum())
    )

st.divider()

# ==================================
# Transformaciones
# ==================================

st.subheader("Transformaciones realizadas")

st.success("""

✅ Eliminación de registros duplicados.

✅ Corrección de categorías inconsistentes.

✅ Normalización de texto.

✅ Conversión de fechas al formato datetime.

✅ Tratamiento de valores faltantes.

✅ Tratamiento de valores atípicos mediante IQR.

✅ Generación del dataset limpio utilizado en el proyecto.

""")