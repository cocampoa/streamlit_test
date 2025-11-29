Análisis Exploratorio de Anuncios de Vehículos (EDA)

Este proyecto implementa una aplicación web interactiva utilizando Streamlit para realizar un Análisis Exploratorio de Datos (EDA) básico sobre un conjunto de datos de anuncios de venta de vehículos.

Propósito de la Aplicación Web

La aplicación web sirve como un cuadro de mandos simple y accesible que permite a los usuarios visualizar rápidamente las principales características del conjunto de datos vehicles_us.csv sin necesidad de escribir código. Es una herramienta introductoria para el análisis de datos.

Funcionalidad Proporcionada

La aplicación proporciona la siguiente funcionalidad interactiva:

Carga de Datos: Lee y procesa el conjunto de datos vehicles_us.csv.

Visualización Interactiva: Utiliza Plotly Express para generar gráficos de alta calidad.

Gráfico de Histograma: Permite al usuario generar un histograma de la columna odometer (kilometraje) para entender su distribución.

Gráfico de Dispersión: Permite al usuario generar un gráfico de dispersión de price (precio) vs. odometer (kilometraje) para visualizar la correlación entre estas dos variables.

Los gráficos se activan mediante casillas de verificación (st.checkbox) para permitir una visualización selectiva y dinámica del análisis.

Configuración del Entorno

Para ejecutar esta aplicación, asegúrate de tener instalados los paquetes listados en requirements.txt en tu entorno virtual.

requirements.txt:

pandas
plotly_express
streamlit