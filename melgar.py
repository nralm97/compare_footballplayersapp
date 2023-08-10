import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import boto3


st.write('Hello world')


'''
#----------------------LECTURA DE DATOS DESDE BUCKET S3
# Configurar las credenciales de AWS
aws_access_key_id = 'AKIAZTXLOUXDGLBX4VQZ'
aws_secret_access_key = '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'
region_name = 'us-west-2'
# Nombre del bucket de S3 y nombre del archivo Excel
bucket_name = 'prueba2007'
file_name = 'Team Stats Melgar.xlsx'
# Crear una instancia del cliente de S3
s3_client = boto3.client('s3')
# Leer el archivo Excel desde S3
response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
data = response['Body'].read()
# Crear un DataFrame de pandas con los datos del archivo Excel
df = pd.read_excel(data)

#---------------limpieza de datos
df = df.drop(0) #eliminar primera fila
metricas = ['Fecha', 'Localia','Partido', 'Competición', 'Duración', 'Seleccionar esquema', 'Goles', 'xG', 'Tiros', 'Tiros a puerta',
            '% Tiros a puerta', 'Pases', 'Pases logrados', '% Pases logrados', '% Posesión del balón','Balones perdidos total', 'Balones perdidos Bajos', 'Balones perdidos Medios', 'Balones perdidos Altos',
            'Balones recuperados total', 'Balones recuperados zona Baja', 'Balones recuperados zona Media',
            'Balones recuperados Alta',
            'Duelos', 'Duelos ganados', '% Duelos ganados', 'Tiros de fuera del área', 'Tiros de fuera del área con éxito',
            '% Tiros de fuera del área a puerta', 'Ataques posicionales', 'Ataques posicionales con remate',
            '% Ataques posicionales con remate', 'Contraataques', 'Contraataques con remate', '% Contraataques con remate',
            'Jugadas a balón parado', 'Jugadas a balón parado con remate', '% Jugadas a balón parado con remate', 'Córneres',
            'Córneres con remate', '% Córneres con remate', 'Tiros libres', 'Tiros libres con remate',
            '% Tiros libres con remate', 'Penaltis', 'Penaltis marcados', '% Penaltis marcados', 'Centros',
            'Centros precisos', '% Centros precisos', 'Centros en profundidad completados',
            'Pases en profundidad completados', 'Entradas al área de penalti', 'Entradas al área de penalti (Carreras)',
            'Entradas al área de penalti (Centros)', 'Toques en el área de penalti', 'Duelos ofensivos',
            'Duelos ofensivos ganados', '% Duelos ofensivos ganados', 'Fuera de juego', 'Goles recibidos', 'Tiros en contra',
            'Tiros en contra a la portería', '% Tiros en contra a la portería', 'Duelos defensivos',
            'Duelos defensivos ganados', '% Duelos defensivos ganados', 'Duelos aéreos', 'Duelos aéreos ganados',
            '% Duelos aéreos ganados', 'Entradas a ras de suelo', 'Entradas a ras de suelo logradas',
            '% Entradas a ras de suelo logradas', 'Interceptaciones', 'Despejes', 'Faltas', 'Tarjetas amarillas',
            'Tarjetas rojas', 'Pases hacia adelante', 'Pases hacia adelante logrados', '% Pases hacia adelante logrados',
            'Pases hacia atrás', 'Pases hacia atrás logrados', '% Pases hacia atrás logrados', 'Pases laterales',
            'Pases laterales logrados', '% Pases laterales logrados', 'Pases largos', 'Pases largos logrados',
            '% Pases largos logrados', 'Pases en el último tercio', 'Pases en el último tercio logrados',
            '% Pases en el último tercio logrados', 'Pases progresivos', 'Pases progresivos completados',
            '% Pases progresivos completados', 'Pases inteligentes', 'Pases inteligentes logrados',
            '% Pases inteligentes logrados', 'Saques laterales',
            'Saques laterales logrados', '% Saques laterales logrados', 'Saques de meta', 'Ritmo de juego (pases/min)',
            'Promedio pases por posesión de balón', 'Lanzamiento largo %', 'Distancia media de tiro', 'Longitud media pases',
            'PPDA']
col_antiguas = list(df.columns)
dic_columns = dict(zip(col_antiguas,metricas))
df = df.rename(columns=dic_columns)
df_temp = df[['xG', 'Goles']]

#-----------------graficando y lanzando app con streamlit
st.line_chart(df_temp)

'''
