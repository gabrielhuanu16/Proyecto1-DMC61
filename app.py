import streamlit as st
import numpy as np
import libreria_funciones as lf

st.sidebar.title("Secciones")
st.sidebar.image("DMC_logo.png", width=100)
modulo = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
if modulo == "Home":
  st.title("Modulo 1 - Especialización en Python for Analytics")
  st.image("DMC_logo.png", width=200)
  st.subheader("Elaborado por: Fabricio Gabriel Huánuco Rivero")
  st.divider()
  st.write("**Información General**")
  st.markdown("""
  - Carrera Profesional: Ingenieria de Sistemas e Informatica
  - Universidad: Universidad Continental
  - Ciclo: 6to ciclo
  - Especialización: Python for Analytics
  - Año: 2026
  """)
  st.divider()
  st.write("**Descripción del Proyecto**")
  st.write("Este proyecto consiste en desarrollar una aplicación web utilizando Python y Streamlit, aplicando los fundamentos de programación aprendidos en el módulo Python Fundamentals. La aplicación busca presentar de manera interactiva la información y los resultados obtenidos durante el desarrollo del proyecto.")
  st.divider()
  st.wirte("**Herramientas usadas**")
  st.markdown("""
  - Python
  - Streamlit
  - GitHub
  - NumPy
  """)
  

