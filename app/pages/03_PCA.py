import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(page_title="PCA", page_icon="📉", layout="wide")

st.title("📉 Análisis PCA (Componentes Principales)")
st.write("Reducción de dimensionalidad para entender patrones en los clientes.")

# =========================
# CARGA DE DATOS
# =========================
df = pd.read_csv("data/cleaned_dataset.csv")

st.subheader("📊 Vista previa del dataset")
st.dataframe(df.head())

# =========================
# SELECCIÓN DE VARIABLES
# =========================
st.subheader("⚙️ Selección de variables")

features = st.multiselect(
    "Selecciona variables numéricas para PCA:",
    options=["age", "monthly_watch_time_mins", "customer_support_tickets"],
    default=["age", "monthly_watch_time_mins", "customer_support_tickets"]
)

if len(features) < 2:
    st.warning("Selecciona al menos 2 variables para aplicar PCA.")
    st.stop()

X = df[features]

# =========================
# ESCALADO
# =========================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =========================
# SLIDER DE COMPONENTES
# =========================
n_components = st.slider(
    "Número de componentes principales:",
    min_value=2,
    max_value=len(features),
    value=2
)

pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X_scaled)

# =========================
# VARIANZA EXPLICADA
# =========================
st.subheader("📊 Varianza explicada")

explained = pca.explained_variance_ratio_
cum_explained = np.cumsum(explained)

fig1, ax = plt.subplots()
ax.plot(range(1, len(cum_explained) + 1), cum_explained, marker="o")
ax.set_xlabel("Componentes")
ax.set_ylabel("Varianza acumulada")
ax.set_title("Varianza explicada por PCA")
st.pyplot(fig1)

st.write("Varianza acumulada:", cum_explained)

# =========================
# DATAFRAME PCA
# =========================
cols = [f"PC{i+1}" for i in range(n_components)]
df_pca = pd.DataFrame(X_pca, columns=cols)

# =========================
# AGREGAR VARIABLE CATEGÓRICA (color)
# =========================
color_option = st.selectbox(
    "Color del gráfico:",
    ["subscription_plan", "favorite_genre", "country"]
)

df_pca[color_option] = df[color_option]

# =========================
# GRÁFICO PCA (2D)
# =========================
st.subheader("🎨 Visualización PCA")

if n_components < 2:
    st.warning("Se necesitan al menos 2 componentes para graficar.")
else:
    fig2, ax2 = plt.subplots()

    scatter = ax2.scatter(
        df_pca["PC1"],
        df_pca["PC2"],
        c=pd.factorize(df_pca[color_option])[0],
        cmap="viridis",
        alpha=0.7
    )

    ax2.set_xlabel("PC1")
    ax2.set_ylabel("PC2")
    ax2.set_title("PCA en 2 dimensiones")

    st.pyplot(fig2)

# =========================
# INTERPRETACIÓN AUTOMÁTICA
# =========================
st.subheader("🧠 Interpretación automática")

st.markdown(f"""
- El PCA está usando **{len(features)} variables**.
- El modelo reduce la información a **{n_components} componentes principales**.
- La varianza acumulada explica cómo de bien representan los datos.
- PC1 y PC2 capturan la mayor estructura del comportamiento de los usuarios.
""")

st.success("✔️ PCA ejecutado correctamente")
