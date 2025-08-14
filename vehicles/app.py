import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('notebooks/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatt_button = st.button('Contruir Mapa Dispersión') # crear botón

hist_checkbox= st.checkbox('Histograma')
scatt_checkbox= st.checkbox('Dispersión')

# Crear un encabezado
st.header('Análisis de Comportamiento de venta de coches')
# Condición para botón que genera un histograma
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
#condición de botón para crear un diagram de dispersión
if scatt_button:
    # escrbir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    #crear un mapa de dispersión
    fig_scat = px.scatter(car_data, x='odometer', y='price')
    #mostrar gráfico Plotly interactivo y responsivo
    st.plotly_chart(fig_scat, use_container_width=True)

# Condición para checkbox que genera un histograma
if hist_checkbox:
    
    st.write('Histograma')
    fig_hist = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Condición para checkbox que genera un un mapa de dispersión
if scatt_checkbox:
    
    st.write('Dispersión')
    fig_scattered = px.scatter(car_data, x="odometer", y='price')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scattered, use_container_width=True)