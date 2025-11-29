import pandas as pd
import plotly.express as px
import streamlit as st
import os

# --- Configuración Inicial de la Aplicación ---
st.set_page_config(
    page_title="Análisis Exploratorio de Anuncios de Coches",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Encabezado ---
st.header('Análisis de Anuncios de Venta de Vehículos en EE. UU.')
st.write(
    'Esta aplicación web te permite realizar un Análisis Exploratorio de Datos (EDA) '
    'interactivo sobre el conjunto de datos de anuncios de venta de coches.'
)

# --- Carga de Datos ---
# Obtener la ruta del archivo CSV. Asume que está en el directorio raíz.
csv_file_path = os.path.join(os.path.dirname(__file__), 'vehicles_us.csv')

try:
    # Leer los datos del archivo CSV
    car_data = pd.read_csv(csv_file_path)
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no se encontró en el directorio del proyecto.")
    st.stop()
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")
    st.stop()


# --- Opciones Interactivas con Checkboxes ---
st.subheader('Selecciona las visualizaciones que deseas generar:')

# Casilla de verificación para el Histograma
build_histogram = st.checkbox('Construir un Histograma de Kilometraje (Odometer)')

# Casilla de verificación para el Gráfico de Dispersión
build_scatter = st.checkbox('Construir un Gráfico de Dispersión de Precio vs. Kilometraje')


# --- Lógica de Visualización (Histograma) ---
if build_histogram:
    st.markdown('### Histograma: Distribución del Kilometraje')
    st.write(
        'Este gráfico muestra la frecuencia (conteo) de vehículos para diferentes '
        'rangos de kilometraje (odometer). Observa cómo se agrupan la mayoría de los vehículos.'
    )
    
    # Crear el histograma con Plotly Express
    fig_hist = px.histogram(
        car_data, 
        x="odometer",
        title="Distribución de Kilometraje",
        labels={'odometer': 'Kilometraje (Millas)'},
        color_discrete_sequence=['#FF7F0E'] # Color naranja
    )
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)


# --- Lógica de Visualización (Gráfico de Dispersión) ---
if build_scatter:
    st.markdown('### Gráfico de Dispersión: Precio vs. Kilometraje')
    st.write(
        'Este gráfico visualiza la relación entre el precio del vehículo y su kilometraje. '
        'Generalmente, se espera una correlación negativa: a mayor kilometraje, menor precio.'
    )
    
    # Crear el gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(
        car_data, 
        x="odometer", 
        y="price",
        title="Relación entre Precio y Kilometraje",
        labels={
            'odometer': 'Kilometraje (Millas)', 
            'price': 'Precio ($)'
        },
        opacity=0.6,
        color='condition' # Opcional: añade color por la condición del coche
    )

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- Mensaje Final ---
if not build_histogram and not build_scatter:
    st.info('Selecciona una de las casillas de verificación para comenzar el análisis.')

st.markdown('---')
st.markdown('**Fuente de Datos:** `vehicles_us.csv`')