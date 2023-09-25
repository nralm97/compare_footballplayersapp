import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


#----------------------------- DATA --------------------------
#------------------------------------------------------------
df2 = pd.read_excel('Liga1_2023_080623.xlsx')
#Cambiar de nombre las columnas
columnas = ['Jugador', 'Equipo', 'Equipo durante el periodo seleccionado', 'Posición específica', 'Edad', 'Valor de mercado',
 'Vencimiento contrato', 'Partidos jugados', 'Minutos jugados', 'Goles', 'xG', 'Asistencias', 'xA', 'Duelos/90',
 'Duelos ganados, %', 'País de nacimiento', 'Pasaporte', 'Pie', 'Altura', 'Peso', 'En préstamo',
 'Acciones defensivas realizadas/90', 'Duelos defensivos/90', 'Duelos defensivos ganados, %', 'Duelos aéreos/90',
 'Duelos aéreos ganados, %', 'Entradas/90', 'Posesión conquistada después de una entrada', 'Tiros interceptados/90',
 'Interceptaciones/90', 'Posesión conquistada después de una interceptación', 'Faltas/90', 'Tarjetas amarillas',
 'Tarjetas amarillas/90', 'Tarjetas rojas', 'Tarjetas rojas/90', 'Acciones de ataque exitosas/90', 'Goles/90',
 'Goles (excepto los penaltis)', 'Goles, excepto los penaltis/90', 'xG/90', 'Goles de cabeza', 'Goles de cabeza/90',
 'Tiros', 'Tiros/90', 'Tiros a portería, %', 'Goles hechos, %', 'Asistencias/90', 'Centros/90',
 'Precisión centros, %', 'Centros desde la banda izquierda/90', 'Precisión centros desde la banda izquierda, %',
 'Centros desde la banda derecha/90', 'Precisión centros desde la banda derecha, %', 'Centros al área pequeña/90',
 'Regates/90', 'Regates realizados, %', 'Duelos ofensivos/90', 'Duelos ofensivos ganados, %',
 'Toques en el área de penalti/90', 'Carreras en progresión/90', 'Aceleraciones/90', 'Pases recibidos /90',
 'Pases largos recibidos/90', 'Faltas recibidas/90', 'Pases/90', 'Precisión pases, %', 'Pases hacia adelante/90',
 'Precisión pases hacia adelante, %', 'Pases hacia atrás/90', 'Precision pases hacia atrás, %', 'Pases laterales/90',
 'Precisión pases laterales, %', 'Pases cortos / medios /90', 'Precisión pases cortos / medios, %', 'Pases largos/90',
 'Precisión pases largos, %', 'Longitud media pases, m', 'Longitud media pases largos, m', 'xA/90', 'Asistencias/90',
 'Segundas asistencias/90', 'Terceras asistencias/90', 'Desmarques/90', 'Precisión desmarques, %', 'Jugadas claves/90',
 'Pases en último tercio/90', 'Precisión pases en último tercio, %', 'Pases al área penalti/90',
 'Pases hacia el área penalti, %', 'Pases en profundidad/90', 'Precisión pases en profundidad, %',
 'Ataque en profundidad/90', 'Centros desde el último tercio/90', 'Pases progresivos/90', 'Precisión pases progresivos, %',
 'Goles recibidos', 'Goles recibidos/90', 'Tiros en contra', 'Tiros en contra/90', 'Porterías imbatidas/90',
 'Paradas, %', 'xG en contra', 'xG en contra/90', 'Goles evitados', 'Goles evitados/90',
 'Pases hacia atrás recibidos por el arquero/90', 'Salidas/90', 'Duelos aéreos en los 90.1', 'Tiros libres/90',
 'Tiros libres directos/90', 'Tiros libres directos, %', 'Córneres/90', 'Penaltis a favor', 'Penaltis realizados, %']
col_antiguas = list(df2.columns)
dic_columns = dict(zip(col_antiguas,columnas))
df2 = df2.rename(columns=dic_columns)

df_melgar = df2[df2.Equipo=='Melgar']
seleccion = ['Jugador','Pases/90', 'Precisión pases, %', 'Pases hacia adelante/90','Precisión pases hacia adelante, %',
         'Pases hacia atrás/90', 'Pases laterales/90', 'Pases cortos / medios /90', 'Pases largos/90','Precisión pases largos, %',
        'Longitud media pases, m',
         'Duelos defensivos/90', 'Duelos defensivos ganados, %', 'Duelos aéreos/90','Duelos aéreos ganados, %',
         'Duelos ofensivos/90', 'Duelos ofensivos ganados, %']
df = df_melgar[seleccion]

#---- Promedio de las estadisticas del equipo-
columnas_numericas = df.select_dtypes(include='number')
promedios = columnas_numericas.mean().to_dict()
promedios = {clave: [valor] for clave, valor in promedios.items()} #colocar el valor en una lista para poder crear un dataframe con esto
promedios['Jugador'] = 'Promedio'
df_promedios = pd.DataFrame(promedios)

# ENCABEZADO: escudo Melgar + escudo Liga1
colA, colB, colC = st.columns([1, 6, 1])
with colA:
    st.image('escudo.jpg', use_column_width=True)
with colB:
    pass
    #st.write("Aquí van tus datos, como texto o gráficos")
with colC:
    st.image('liga1.jpg', use_column_width=True)


#-------------- FILTRO------------
filter_player = st.selectbox('Jugador', df['Jugador'].unique())
df_filtrado = df.copy()
if filter_player != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Jugador'] == filter_player]

#---------

df_filtrado = pd.concat([df_filtrado, df_promedios], ignore_index=True)

#-----------------------------  GENERACIÓN DE GRAFICOS ---------------

#---- PASES | GRAFICO DE BARRAS
metricas = ['Jugador','Pases/90','Pases laterales/90','Pases hacia adelante/90', 'Pases hacia atrás/90','Pases largos/90']
df_filtrado1 = df_filtrado[metricas]
# Crear un gráfico de barras y líneas
fig_barras_pases = go.Figure()
# Añadir las barras para la fila 'A'
fig_barras_pases.add_trace(go.Bar(x=df_filtrado1.columns[1:], y=df_filtrado1.loc[0, df_filtrado1.columns[1:]], name='Pases', marker_color='blue'))
# Añadir las líneas para la fila 'promedio'
fig_barras_pases.add_trace(go.Scatter(x=df_filtrado1.columns[1:], y=df_filtrado1.loc[1, df_filtrado1.columns[1:]], mode='lines+markers', name='promedio', line=dict(color='red')))
# Actualizar el diseño del gráfico
fig_barras_pases.update_layout(
    title='Pases/90 según tipo y Promedio del equipo',
    barmode='group'
)
fig_barras_pases.update_layout(
    width=500,
    height=300,
)

#------- DUELOS | GRAFICO DE BARRAS
metricas2 = ['Jugador','Duelos defensivos/90', 'Duelos ofensivos/90', 'Duelos aéreos/90']
df_filtrado2 = df_filtrado[metricas2]
# Crear un gráfico de barras y líneas
fig_barras_duelos = go.Figure()
# Añadir las barras para la fila 'A'
fig_barras_duelos.add_trace(go.Bar(x=df_filtrado2.columns[1:], y=df_filtrado2.loc[0, df_filtrado2.columns[1:]], name='Duelos', marker_color='blue'))
# Añadir las líneas para la fila 'promedio'
fig_barras_duelos.add_trace(go.Scatter(x=df_filtrado2.columns[1:], y=df_filtrado2.loc[1, df_filtrado2.columns[1:]], mode='lines+markers', name='promedio', line=dict(color='red')))
# Actualizar el diseño del gráfico
fig_barras_duelos.update_layout(
    title='Duelos/90 según tipo y Promedio del equipo',
    barmode='group'
)
fig_barras_duelos.update_layout(
    width=500,
    height=260,
)


# ----INDICADOR PASES --- 
fig_percent_pases = go.Figure(go.Indicator(
    mode="gauge+number",
    value= df_filtrado.reset_index(drop=True).loc[0, 'Precisión pases, %'],
    title={'text': "% Precisión pases totales"},
    gauge={'axis': {'range': [0, 100]},
           'bar': {'color': "darkblue"},
           'steps': [
               {'range': [0, 50], 'color': "lightgray"},
               {'range': [50, 100], 'color': "gray"}]
           }
))
fig_percent_pases.update_layout(
    width=250,  # Ancho en píxeles
    height=250,  # Altura en píxeles
)

#------
fig_percent_duelos = go.Figure(go.Indicator(
    mode="gauge+number",
    value= df_filtrado.reset_index(drop=True).loc[0, 'Duelos aéreos ganados, %'],
    title={'text': "% Precisión duelos aéreos"},
    gauge={'axis': {'range': [0, 100]},
           'bar': {'color': "darkblue"},
           'steps': [
               {'range': [0, 50], 'color': "lightgray"},
               {'range': [50, 100], 'color': "gray"}]
           }
))
fig_percent_duelos.update_layout(
    width=250,  # Ancho en píxeles
    height=250,  # Altura en píxeles
)


#----------------------- DISEÑO DE LA PAGINA -----------
col11, col12= st.columns([5, 1])
with col11:
    st.plotly_chart(fig_barras_pases)

with col12:
    st.plotly_chart(fig_percent_pases)

col21, col22= st.columns([5, 1])
with col21:
    st.plotly_chart(fig_barras_duelos)

with col22:
    st.plotly_chart(fig_percent_duelos)


