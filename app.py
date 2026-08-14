import streamlit as st
import numpy as np
import libreria_funciones as lf
import pandas as pd

st.sidebar.title("Secciones")
st.sidebar.image("DMC_logo.png", width=100)
modulo = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
if modulo == "Home":
  st.title("Modulo 1 - Especialización en Python for Analytics")
  st.image("DMC_logo.png", width=200)
  st.subheader("Elaborado por: Fabricio Gabriel Huánuco Rivero")
  st.subheader("Python Fundamentals")
  st.divider()
  st.write("**Información General**")
  st.markdown("""
  - Carrera Profesional: Ingenieria de Sistemas e Informatica
  - Universidad: Universidad Continental
  - Ciclo: 6to
  - Especialización: Python for Analytics
  - Año: 2026
  """)
  st.divider()
  st.write("**Descripción del Proyecto**")
  st.write("Este proyecto consiste en desarrollar una aplicación web utilizando Python y Streamlit, aplicando los fundamentos de programación aprendidos en el módulo Python Fundamentals. La aplicación busca presentar de manera interactiva la información y los resultados obtenidos durante el desarrollo del proyecto.")
  st.divider()
  st.write("**Tecnologías Utilizadas**")
  st.markdown("""
  - Python
  - Streamlit
  - GitHub
  - NumPy
  """)
elif modulo == "Ejercicio 1":
  st.title("Ejercicio 1")
  st.divider()
  st.write("**Descripción**")
  st.markdown("Este ejercicio consiste en desarrollar una aplicación interactiva para registrar y gestionar movimientos financieros. El usuario podrá ingresar el concepto, tipo y valor de cada movimiento, clasificándolo como ingreso o gasto. La aplicación permitirá visualizar los movimientos registrados, calcular el total de ingresos y gastos, determinar el saldo final y mostrar si el flujo de caja se encuentra a favor o en contra.")
  st.divider()
  concepto = st.text_input("Ingresar el concepto")
  tipo_mov = st.selectbox("Ingresar el tipo de movimiento",["Ingreso","Gasto"])
  valor = st.number_input("Ingresar el valor")
  boton1 = st.button("Agregar Movimiento")
  if boton1:
    lista1 = {"Concepto":[concepto], "Tipo de Movimiento":[tipo_mov], "Valor":[valor]}
    tabla = st.dataframe(lista1)
  

  

