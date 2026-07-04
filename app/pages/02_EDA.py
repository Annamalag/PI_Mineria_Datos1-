import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Configuración
# -----------------------------
st.set_page_config(
    page_title="EDA",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# Cargar dataset
# -----------------------------
df = pd.read_csv("data/cleaned_dataset.csv")

st.title("📈 Análisis Exploratorio de Datos (EDA)")

st.write("""
En esta sección se presentan las principales visualizaciones obtenidas durante el
Análisis Exploratorio de Datos (EDA). Cada gráfico incluye su interpretación para
facilitar la comprensión de los resultados.
""")

st.divider()

st.subheader("1️⃣ Distribución de la Edad")

fig, ax = plt.subplots(figsize=(8,4))

sns.histplot(df["age"], bins=20, kde=True, ax=ax)

st.pyplot(fig)

st.info("""
La mayor parte de los usuarios se concentra en edades intermedias, mientras que
los valores extremos aparecen con menor frecuencia. Esto indica que la plataforma
es utilizada principalmente por una población adulta joven.
""")

st.divider()

st.subheader("2️⃣ Usuarios por Plan de Suscripción")

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(data=df, x="subscription_plan", ax=ax)

st.pyplot(fig)

st.info("""
El plan Estándar es el más utilizado por los usuarios del conjunto de datos,
seguido por los planes Básico y Premium.
""")

st.divider()

st.subheader("3️⃣ Plan vs Tiempo de Visualización")

fig, ax = plt.subplots(figsize=(8,4))

sns.boxplot(
    data=df,
    x="subscription_plan",
    y="monthly_watch_time_mins",
    ax=ax
)

st.pyplot(fig)

st.info("""
Los usuarios del plan Premium presentan, en general, mayores tiempos de
visualización mensual que los usuarios de los planes Básico y Estándar.
""")

st.divider()

st.subheader("4️⃣ Edad vs Tiempo de Visualización")

fig, ax = plt.subplots(figsize=(8,4))

sns.scatterplot(
    data=df,
    x="age",
    y="monthly_watch_time_mins",
    alpha=0.6,
    ax=ax
)

st.pyplot(fig)

st.info("""
No se observa una relación lineal clara entre la edad y el tiempo de visualización.
Usuarios de diferentes edades presentan comportamientos de consumo muy variados.
""")

st.divider()

st.subheader("5️⃣ Matriz de Correlación")

corr = df[
    [
        "age",
        "monthly_watch_time_mins",
        "customer_support_tickets"
    ]
].corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(6,5))

sns.heatmap(
    corr,
    annot=True,
    cmap="Blues",
    ax=ax
)

st.pyplot(fig)

st.info("""
Las correlaciones entre las variables numéricas son bajas, indicando que no
existen relaciones lineales fuertes entre ellas. Esto sugiere que otros factores,
como el plan de suscripción o el género favorito, podrían explicar mejor el
comportamiento de los usuarios.
""")

