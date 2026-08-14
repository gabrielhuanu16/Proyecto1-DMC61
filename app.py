import streamlit as st
import numpy as np
import libreria_funciones as lf

st.sidebar.title("Secciones")
modulo = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
