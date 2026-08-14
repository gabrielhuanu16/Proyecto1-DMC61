import streamlit as st
import numpy as np
import libreria_funciones as lf

st.sidebar.title("Secciones")
st.sidebar.image("DMC_logo.png", width=100)
modulo = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
if modulo == "Home":
  st.title("Modulo 1 - Especialización en Python for Analytics")
  st.image("DMC_logo.png", width=200)
  st.subheader("**Elaborado por:**"" Fabricio Gabriel Huánuco Rivero")
  st.markdown("Carrera Profesional: Ingenieria de Sistemas e Informatica")

