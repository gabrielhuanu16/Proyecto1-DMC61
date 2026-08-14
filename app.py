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
  st.markdown("Carrera Profesional: Ingenieria de Sistemas e Informatica")
  st.markdown("Universidad: Universidad Continental")
  st.markdown("Ciclo: 6to ciclo")  
  st.markdown("Especialización: Python for Analytics")
  st.write("Año: 2026")
  st.subheader("Este proyecto consiste en desarrollar una aplicación web utilizando Python y Streamlit, aplicando los fundamentos de programación aprendidos en el módulo Python Fundamentals. La aplicación busca presentar de manera interactiva la información y los resultados obtenidos durante el desarrollo del proyecto.")
  st.markdown("""
  - Python
  - Streamlit
  - GitHub
  """)
  

