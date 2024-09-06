import pandas as pd
import plotly.express as px
import streamlit as st

# Load the data
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox to create a histogram
build_histogram = st.checkbox('Construir histograma')

if build_histogram:  # When the checkbox is selected
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")  # Create a histogram of the odometer data
    st.plotly_chart(fig, use_container_width=True)  # Display the histogram

# Button to create a scatter plot
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # When the scatter plot button is clicked
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")  # Create a scatter plot with odometer vs. price
    st.plotly_chart(fig, use_container_width=True)  # Display the scatter plot
