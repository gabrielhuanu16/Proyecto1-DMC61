import streamlit as st
import numpy as np
import libreria_funciones as lf
import pandas as pd
import libreria_clases_ as lc

st.sidebar.title("Secciones")
st.sidebar.image("DMC_logo.png", width=100)
modulo = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
if modulo == "Home":
  st.title("Modulo 1 - Especialización en Python for Analytics")
  st.image("gabriel_logo.png", width=200)
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
  tipo_mov = st.selectbox("Seleccione el tipo de movimiento",["Ingreso","Gasto"])
  valor = st.number_input("Ingresar el valor")
  boton1 = st.button("Agregar Movimiento")
  st.divider()
  if "movimiento" not in st.session_state:
    st.session_state.movimiento = []
  if boton1:
    movimiento = {"Concepto":concepto, "Tipo de Movimiento":tipo_mov, "Valor":valor}
    st.session_state.movimiento.append(movimiento)
  st.dataframe(st.session_state.movimiento)
  suma_ingreso = sum(x["Valor"] for x in st.session_state.movimiento if x["Tipo de Movimiento"] == "Ingreso")
  suma_gasto = sum(x["Valor"] for x in st.session_state.movimiento if x["Tipo de Movimiento"] == "Gasto")
  st.write("Total de Ingresos: ", suma_ingreso)
  st.write("Total de Gastos: ", suma_gasto)
  saldo_final = suma_ingreso - suma_gasto
  st.write("**Saldo Final:**", saldo_final)
  if saldo_final > 0:
    st.write("**El flujo de caja está A FAVOR**")
  else:
    st.write("**El flujo de caja está EN CONTRA**")

elif modulo == "Ejercicio 2":
  st.title("Ejercicio 2")
  st.divider()
  st.write("**Descripción**")
  st.markdown("Este ejercicio consiste en desarrollar un formulario interactivo para registrar productos utilizando NumPy y Pandas. El usuario podrá ingresar el nombre, categoría, precio y cantidad de cada producto. A partir de estos datos se calculará el total y los registros serán almacenados en arreglos de NumPy para posteriormente convertirlos en un DataFrame, mostrando la información actualizada en pantalla.")
  st.divider()
  nombre_prod = st.text_input("Ingrese el nombre del producto")
  categoria = st.selectbox("Seleccione la categoria", ["Tecnología","Alimentos","Ropa","Bebidas","Deportes","Belleza"])
  precio = st.number_input("Ingrese el precio del producto")
  cantidad = st.number_input("Ingrese la cantidad del producto", min_value=1, step=1)
  precio_total = precio*cantidad
  boton2 = st.button("Agregar Registro")
  st.divider()
  if "nombre" not in st.session_state:
    st.session_state.nombre = np.array([])
  if "cat" not in st.session_state:
    st.session_state.cat = np.array([])
  if "prec" not in st.session_state:
    st.session_state.prec = np.array([])
  if "cant" not in st.session_state:
    st.session_state.cant = np.array([])
  if "total" not in st.session_state:
    st.session_state.total = np.array([])
    
  if boton2:
    st.session_state.nombre = np.append(st.session_state.nombre, nombre_prod)
    st.session_state.cat = np.append(st.session_state.cat, categoria)
    st.session_state.prec = np.append(st.session_state.prec, precio)
    st.session_state.cant = np.append(st.session_state.cant, cantidad)
    st.session_state.total = np.append(st.session_state.total, precio_total)
  registro = pd.DataFrame({"Producto":st.session_state.nombre, "Categoria":st.session_state.cat, "Precio":st.session_state.prec, "Cantidad":st.session_state.cant, "Precio Total":st.session_state.total})
  st.dataframe(registro)

elif modulo == "Ejercicio 3":
  st.title("Ejercicio 3")
  st.divider()
  st.write("**Descripción**")
  st.markdown("Este ejercicio consiste en utilizar una función de una librería externa relacionada con el área de formación, conectándola con una interfaz interactiva en Streamlit. El usuario podrá ingresar los parámetros necesarios, ejecutar la función y visualizar el resultado. Además, los resultados obtenidos se almacenarán en un histórico mostrado mediante un DataFrame.")
  st.divider()
  st.subheader("Punto de Equilibrio")
  costos_fijos = st.number_input("Costos Fijos")
  precio_unitario = st.number_input("Precio de Venta por Unidad")
  costo_variable_unitario = st.number_input("Costo Variable por Unidad")
  impuesto_pct = st.number_input("Impuesto (%)")
  boton3 = st.button("Calcular Punto de Equilibrio")
  if "tabla" not in st.session_state:
    st.session_state.tabla = []
  if boton3:
    resultado = lf.punto_equilibrio(costos_fijos, precio_unitario, costo_variable_unitario, impuesto_pct)
    tabla = {"Costos Fijos":costos_fijos,"Precio Venta Unidad":precio_unitario,"Costo Variable Unidad":costo_variable_unitario,"Impuesto":impuesto_pct,"Punto Equilibrio":resultado}
    st.session_state.tabla.append(tabla)
  st.divider()
  st.dataframe(st.session_state.tabla)

else:
  st.title("Ejercicio 4")
  st.divider()
  st.write("**Descripción**")
  st.markdown("Este ejercicio consiste en utilizar una clase de la librería externa libreria_clases_proyecto1.py e integrarla con Streamlit. La aplicación permitirá crear, visualizar, actualizar y eliminar registros (CRUD) mediante formularios y widgets interactivos.")
  st.divider()
  st.subheader("Tecnología/Informática")
  nombre_serv = st.text_input("Nombre de tu Servidor")
  tiempo_total = st.number_input("Total de Hora a Evaludas", min_value=1, step=1)
  tiempo_caida = st.number_input("Horas que estubo caído", min_value=1, step=1)
  almacenamiento_total = st.number_input("Almacenamiento Total en GB", min_value=1, step=1)
  almacanamiento_usado = st.number_input("Almacenamiento Usado en GB", min_value=1, step=1)
  boton_guardar = st.button("Guardar Servidor")
  if "registro" is not st.session_state:
    st.session_state.registro = []
  if boton_guardar:
    try:
      nuevo_servidor = lc.Servidor(nombre=nombre_serv, tiempo_total_h=tiempo_total,
                               tiempo_caida_h=tiempo_caida, almacenamiento_total_gb=almacenamiento_total,
                               almacenamiento_usado_gb=almacanamiento_usado)
      resumen = nuevo_servidor.resumen()
      st.session_state.registro = st.session_state.registro.append(resumen)
    except ValueError as e:
      st.error(f"Error en los datos: {e}")
    
  
