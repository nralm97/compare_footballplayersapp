import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import boto3
from io import BytesIO

#------------------------------------------------------------------------

def graf_barras(list_metrics, df, titulo):
    df2 = df[list_metrics]
    fig_barras = go.Figure()
    #fila 0 es el jugador, fila 1 es la media de melgar
    # Añadir las barras
    fig_barras.add_trace(go.Bar(x=df2.columns[1:], y=df2.loc[0, df2.columns[1:]], name='jugador', text=df2.loc[0, df2.columns[1:]], marker_color='black'))
    # Añadir las líneas para la fila 'promedio'
    fig_barras.add_trace(go.Scatter(x=df2.columns[1:], y=df2.loc[1, df2.columns[1:]], mode='lines+markers', name='promedio', line=dict(color='red')))
    # Actualizar el diseño del gráfico
    fig_barras.update_layout(
        title=titulo,
        barmode='group'
    )
    fig_barras.update_layout(
        width=350,
        height=280,
    )
    return fig_barras

def graf_dispersion(df, varx, vary,titulo, df_jugador, df_media_pos):
    fig_dispersion = px.scatter(df, x=varx, y=vary, title=titulo,
                 labels={varx: varx, vary: vary},
                 hover_data={'Jugador': True},
                 #size='Minutos jugados',
                color='Minutos jugados',
                color_continuous_scale='greys',
    )
    '''
    fig_dispersion.add_trace(
        px.scatter(df_jugador, x=varx, y=vary,
                    text='Jugador')['data'][0]
                    )
    '''
    fig_dispersion.add_trace(
        go.Scatter(
            x=[df_jugador[varx]][0],
            y=[df_jugador[vary]][0],
            mode='markers',
            marker=dict(color='red', size=7),  # Color verde y tamaño ajustable
            name= df_jugador['Jugador'][0]
            #text='Jugador',  # Texto emergente para el punto especial
        )
    )

    fig_dispersion.update_layout(
        width=480,
        height=580,
        title_x=0.25,  # Centrar el título horizontalmente
    )
    # Agregar una línea vertical constante (punteada) en ek promedio
    fig_dispersion.add_shape(
        dict(
            type="line",
            x0=df_media_pos[varx][2],
            x1=df_media_pos[varx][2],
            y0=min(df[vary])-1.5, #sum
            y1=max(df[vary])+1.5,
            line=dict(color="black", width=1, dash="dash"),
        )
    )
    fig_dispersion.add_shape(
        dict(
            type="line",
            x0=min(df[varx])-1.5,
            x1=max(df[varx])+1.5,
            y0=df_media_pos[vary][2],
            y1=df_media_pos[vary][2],
            line=dict(color="black", width=1, dash="dash"),
        )
    )
    return fig_dispersion








