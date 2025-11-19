import streamlit as st
import pandas as pd
import numpy as np

st.title("Estadísticas del agua en México (Noviembre 2025)")

st.write("Aquí encontrarás datos y estadísticas relevantes sobre la situación hídrica en México")

st.subheader("Superficie del país afectada por sequía (Marzo 2025)")

chart_data = pd.DataFrame({
        "Nivel de sequía": ["Anormalmente seco", "Sequía moderada", "Sequía extrema y excepcional"],
        "Superficie Afectada (%)": [35.2, 42.4, 6.5] })
chart_data = chart_data.set_index("Nivel de sequía")

st.bar_chart(chart_data)

st.caption("Fuente: Monitor de Sequía en México, CONAGUA (Marzo 2025)")

st.subheader("Indicadores de almacenamiento (Noviembre 2025)")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Almacenamiento promedio nacional de presas", 
        value="72%", 
        delta="28%", 
        delta_color="normal")

with col2:
    st.metric(
        label="Nivel promedio sistema Cutzamala", 
        value="85%", 
        delta="56.6%", 
        delta_color="normal")

with col3:
    st.metric(
        label="Nivel presa Valle de Bravo",
        value="93.3%",
        delta="40.7%", 
        delta_color="normal")

st.caption("Fuente: Comunicados de CONAGUA sobre niveles de presas (Octubre-Noviembre 2025)")
