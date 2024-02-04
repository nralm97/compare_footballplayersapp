import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import boto3
from io import BytesIO

import appmelgar_etl
import appmelgar_graficos
from appmelgar_etl import df
from appmelgar_etl import posiciones

# Configurar la página para usar el ancho completo
st.set_page_config(
    page_title="Player performance data",
    layout="centered",  # Wide: Usa todo el ancho de la pantalla
)

# ENCABEZADO: escudo Melgar + escudo Liga1
colA, colB, colC = st.columns([1, 7, 1])
with colA:
    st.image('escudo.jpg', use_column_width=True)
with colB:
    pass
    #st.write("Aquí van tus datos, como texto o gráficos")
with colC:
    st.image('liga1.jpg', use_column_width=True)
#--------------------------------------------------------------------------------------------------


#FILTRO POR POSICION Y POR JUGADOR
#posiciones = ['Defensa central', 'Carrilero', 'Volante defensivo', 'Volante ofensivo', 'Delantero centro']
posicion = st.selectbox(
    'Posición',
     posiciones)
#
for pos in posiciones:
    if posicion == pos:
        df_pos = df[df[pos]==True]
#
df_pos_mel = df_pos[df_pos['Equipo actual'] =='Melgar']
jugador = st.selectbox(
    'Jugador',
     df_pos_mel['Jugador'].unique())

df_filtrado = df_pos_mel[df_pos_mel['Jugador']==jugador]
#----------------------------------------------------------------------------------
df_team = df[df['Equipo actual'] =='Melgar']
#PROMEDIOS DE METRICAS
df_mean_mel = appmelgar_etl.mean_metrics(df_team,'mean_melgar')
df_mean = appmelgar_etl.mean_metrics(df_pos,'mean')

df_filtrado = df_filtrado.reset_index(drop=True)
df_mean_mel = df_mean_mel.reset_index(drop=True)
df_mean = df_mean.reset_index(drop=True)

df_filtro_mean = pd.concat([df_filtrado, df_mean_mel, df_mean], ignore_index=True)

#------------------------------------------------------------------------
#-----------------------------  GENERACIÓN DE GRAFICOS ---------------
#------- DUELOS/90 | GRAFICO DE BARRAS
metricas1 = ['Jugador','Duelos defensivos/90', 'Duelos aéreos/90','Duelos ofensivos/90']
title1 ='Duelos/90 | Melgar'
fig_barras_duelos =  appmelgar_graficos.graf_barras(metricas1, df_filtro_mean, title1)
#---- DUELOS % | GRAFICO DE BARRAS
metricas2 = ['Jugador','Duelos defensivos ganados, %', 'Duelos aéreos ganados, %', 'Duelos ofensivos ganados, %']
title2 ='Duelos, % éxito | Melgar'
fig_barras_duelos2 =  appmelgar_graficos.graf_barras(metricas2, df_filtro_mean, title2)
#DUELOS| GRAFICO DE DISPERSION
titleA ='Efectividad duelos | Liga1'
varx = 'Duelos defensivos ganados, %'
vary = 'Duelos aéreos ganados, %'
fig_disp_duelos = appmelgar_graficos.graf_dispersion(df_pos, varx, vary, titleA, df_filtrado, df_filtro_mean)

#---- METRICAS DEFENSIVAS | GRAFICO DE BARRAS
metricas3 = ['Jugador','Acciones defensivas realizadas/90','Interceptaciones/90', 'Faltas/90']
title3='Acciones defensivas A | Melgar'
fig_barras_def =  appmelgar_graficos.graf_barras(metricas3, df_filtro_mean, title3)
#---- DEFENSA AJUSTADA POR POSESIÓN | GRAFICO DE BARRAS
metricas4 = ['Jugador','Tiros interceptados/90', 'Entradas/90',]
title4='Acciones defensivas B | Melgar'
fig_barras_def2 =  appmelgar_graficos.graf_barras(metricas4, df_filtro_mean, title4)
#METRICAS DEFENSIVAS| GRAFICO DE DISPERSION
titleB ='Acciones defensivas ajustadas por posesión | Liga1' 
varx = 'Entradas(ajustado por posesión)'
vary = 'Interceptaciones(ajustado por posesión)'
fig_disp_def = appmelgar_graficos.graf_dispersion(df_pos, varx, vary, titleB, df_filtrado, df_filtro_mean)

#---- PASES /90 | GRAFICO DE BARRAS
metricas5 = ['Jugador','Pases cortos/medios /90', 'Pases largos/90', 'Pases progresivos/90', 'Pases al último tercio/90']
title5='Pases / 90 | Melgar'
fig_barras_pases =  appmelgar_graficos.graf_barras(metricas5, df_filtro_mean, title5)
#---- PASES, % | GRAFICO DE BARRAS
metricas6 = ['Jugador','Precisión pases cortos/medios, %','Precisión pases largos, %', 'Precisión pases progresivos, %',
              'Precisión pases al último tercio, %']
title6='Efectividad en los pases | Melgar'
fig_barras_pases2 =  appmelgar_graficos.graf_barras(metricas6, df_filtro_mean, title6)
# PASES %| GRAFICO DE DISPERSION
titleC ='Pases / contrucción | Liga1' 
varx = 'Precisión pases progresivos, %'
vary = 'Precisión pases largos, %'
fig_disp_pases = appmelgar_graficos.graf_dispersion(df_pos, varx, vary, titleC, df_filtrado, df_filtro_mean)

#----------------------- DISEÑO DE LA PAGINA -----------
#st.subheader('METRICAS 1')
col11, col12= st.columns([1, 1])
with col11:
    st.plotly_chart(fig_barras_duelos)
    st.plotly_chart(fig_barras_duelos2)

with col12:
    st.plotly_chart(fig_disp_duelos)

#
st.write("<hr>", unsafe_allow_html=True)
col21, col22= st.columns([1, 1])
with col21:
    st.plotly_chart(fig_barras_def)
    st.plotly_chart(fig_barras_def2)

with col22:
    st.plotly_chart(fig_disp_def)

#----
col31, col32= st.columns([1, 1])
with col31:
    st.plotly_chart(fig_barras_pases)
    st.plotly_chart(fig_barras_pases2)

with col32:
    st.plotly_chart(fig_disp_pases)


