import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Estadísticas del Agua en México")

st.write("En esta sección encontrarás datos y estadísticas relevantes sobre la situación hídrica en México. (Datos de ejemplo)")

# --- 1. Gráfica de Barras (st.bar_chart) ---
st.subheader("Disponibilidad de Agua por Región (Ejemplo)")

# Creamos datos de ejemplo (reemplazar con datos reales)
chart_data = pd.DataFrame(
    {
        "Región": ["Norte", "Centro", "Sur", "Sureste"],
        "Disponibilidad (m³/hab/año)": [1500, 2500, 5000, 15000]
    }
)
chart_data = chart_data.set_index("Región")

# Usamos st.bar_chart
st.bar_chart(chart_data)

st.caption("Gráfica generada con `st.bar_chart`.")

# --- 2. Métricas (st.metric) ---
st.subheader("Indicadores Clave (KPIs de Ejemplo)")

# Usamos st.columns para ordenar las métricas
col1, col2, col3 = st.columns(3)

# Métrica 1
with col1:
    # Usamos st.metric
    st.metric(
        label="Cobertura de Agua Potable", 
        value="91.5%", 
        delta="0.5%",
        delta_color="normal" # 'normal' (verde), 'inverse' (rojo)
    )

# Métrica 2
with col2:
    st.metric(
        label="Agua Tratada (Nacional)", 
        value="67%", 
        delta="-1.2%",
        delta_color="inverse"
    )

# Métrica 3
with col3:
    st.metric(
        label="Nivel Presa 'El Cuchillo' (Ejemplo)",
        value="52%",
        delta="3.1%",
        delta_color="normal"
    )

st.caption("Métricas generadas con `st.metric`.")
