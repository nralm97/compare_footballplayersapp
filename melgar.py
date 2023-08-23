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

#-------------- FILTRO------------
filter_player = st.selectbox('Jugador', df['Jugador'].unique())
df_filtrado = df.copy()
if filter_player != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Jugador'] == filter_player]

#------------- PASES - GRAFICO DE BARRAS----
# Define los colores que deseas asignar a cada valor
metricas = ['Pases/90',
            'Pases laterales/90','Pases hacia adelante/90', 'Pases hacia atrás/90',
            'Pases largos/90']
colores = ['#F71B05','#20F712','#1CC511','#118D09', '#1E06B4']
color_discrete_map = {key: value for key, value in zip(metricas, colores)}
# Crea el gráfico de barras múltiples con colores asignados
fig = px.bar(df_filtrado, y='Jugador', x=metricas, barmode='group', orientation='h',
             color_discrete_map=color_discrete_map)
# Agrega título y etiquetas de ejes
fig.update_layout(title='PASES',
                  xaxis_title='Valor/90 min',
                  yaxis_title='Jugador')
st.plotly_chart(fig)


#------------- DUELOS - GRAFICO DE BARRAS----
metricas2 = ['Duelos defensivos/90', 'Duelos ofensivos/90', 'Duelos aéreos/90']
colores2 = ['#A72DCA','#1BE2E5', '#17096E']
color_discrete_map2 = {key: value for key, value in zip(metricas2, colores2)}
# Crea el gráfico de barras múltiples con colores asignados
fig2 = px.bar(df_filtrado, y='Jugador', x=metricas2, barmode='group', orientation='h',
             color_discrete_map=color_discrete_map2)
# Agrega título y etiquetas de ejes
fig2.update_layout(title='DUELOS',
                  xaxis_title='Valor/90 min',
                  yaxis_title='Jugador')
st.plotly_chart(fig2)

#----------------
# Crear el gráfico de tacómetro
fig_gauge = go.Figure(go.Indicator(
    domain={'x': [0.6, 1], 'y': [0.2, 0.8]},
    value=75,
    mode="gauge+number",
    title={'text': "Tacómetro"},
    gauge={'axis': {'range': [None, 100]},
           'bar': {'color': "darkblue"},
           'steps': [
               {'range': [0, 50], 'color': "lightgray"},
               {'range': [50, 100], 'color': "gray"}]
           }
))

st.plotly_chart(fig_gauge)


