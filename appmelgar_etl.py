import streamlit as st
import numpy as np
import pandas as pd
import boto3
from io import BytesIO
#----------------------------- LEER DATA --------------------------
# Configurar las credenciales de AWS
s3 = boto3.client('s3',
                  aws_access_key_id='AKIAR7OO4KTVM3CTOPHQ',
                  aws_secret_access_key='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')
# Nombre del archivo y nombre del bucket en S3
bucket_name = 'bucket-melgar'
file_name = 'Search results.xlsx'
# Leer el archivo Excel desde S3
obj = s3.get_object(Bucket=bucket_name, Key=file_name)
excel_data = obj['Body'].read()
# Utilizar BytesIO para crear un buffer en memoria
buffer = BytesIO(excel_data)
# Leer el archivo Excel desde el buffer
df2 = pd.read_excel(buffer)

#-----------------------LIMPIAR DATA ---------
#Cambiar de nombre las columnas
columnas = ['Jugador', 'Equipo', 'Equipo actual', 'Posición específica', 'Edad', 'Valor de mercado',
 'Vencimiento contrato', 'Partidos jugados', 'Minutos jugados', 'Goles', 'xG', 'Asistencias', 'xA', 'Duelos/90',
 'Duelos ganados, %', 'País de nacimiento', 'Pasaporte', 'Pie', 'Altura', 'Peso', 'En préstamo',
 'Acciones defensivas realizadas/90', 'Duelos defensivos/90', 'Duelos defensivos ganados, %', 'Duelos aéreos/90',
 'Duelos aéreos ganados, %', 'Entradas/90', 'Entradas(ajustado por posesión)', 'Tiros interceptados/90',
 'Interceptaciones/90', 'Interceptaciones(ajustado por posesión)', 'Faltas/90', 'Tarjetas amarillas',
 'Tarjetas amarillas/90', 'Tarjetas rojas', 'Tarjetas rojas/90', 'Acciones de ataque exitosas/90', 'Goles/90',
 'Goles (excepto los penaltis)', 'Goles, excepto los penaltis/90', 'xG/90', 'Goles de cabeza', 'Goles de cabeza/90',
 'Tiros', 'Tiros/90', 'Tiros a portería, %', 'Goles hechos, %', 'Asistencias/90', 'Centros/90',
 'Precisión centros, %', 'Centros desde la banda izquierda/90', 'Precisión centros desde la banda izquierda, %',
 'Centros desde la banda derecha/90', 'Precisión centros desde la banda derecha, %', 'Centros al área pequeña/90',
 'Regates/90', 'Regates realizados, %', 'Duelos ofensivos/90', 'Duelos ofensivos ganados, %',
 'Toques en el área de penalti/90', 'Carreras progresivas/90', 'Aceleraciones/90', 'Pases recibidos /90',
 'Pases largos recibidos/90', 'Faltas recibidas/90', 'Pases/90', 'Precisión pases, %', 'Pases hacia adelante/90',
 'Precisión pases hacia adelante, %', 'Pases hacia atrás/90', 'Precisión pases hacia atrás, %', 'Pases laterales/90',
 'Precisión pases laterales, %', 'Pases cortos/medios /90', 'Precisión pases cortos/medios, %', 'Pases largos/90',
 'Precisión pases largos, %', 'Longitud media pases, m', 'Longitud media pases largos, m', 'xA/90', 'Asistencias/90',
 'Segundas asistencias/90', 'Terceras asistencias/90', 'Desmarques/90', 'Precisión desmarques, %', 'Jugadas claves/90',
 'Pases al último tercio/90', 'Precisión pases al último tercio, %', 'Pases al área penalti/90',
 'Pases hacia el área penalti, %', 'Pases en profundidad/90', 'Precisión pases en profundidad, %',
 'Ataque en profundidad/90', 'Centros al último tercio/90', 'Pases progresivos/90', 'Precisión pases progresivos, %',
 'Goles recibidos', 'Goles recibidos/90', 'Tiros en contra', 'Tiros en contra/90', 'Porterías imbatidas/90',
 'Paradas, %', 'xG en contra', 'xG en contra/90', 'Goles evitados', 'Goles evitados/90',
 'Pases hacia atrás recibidos por el arquero/90', 'Salidas/90', 'Duelos aéreos en los 90.1', 'Tiros libres/90',
 'Tiros libres directos/90', 'Tiros libres directos, %', 'Córneres/90', 'Penaltis a favor', 'Penaltis realizados, %']
col_antiguas = list(df2.columns)
dic_columns = dict(zip(col_antiguas,columnas))
df2 = df2.rename(columns=dic_columns)

seleccion = ['Jugador', 'Equipo actual','Minutos jugados','Posición específica',
             'Duelos defensivos/90','Duelos aéreos/90','Duelos ofensivos/90', 
             'Duelos defensivos ganados, %', 'Duelos aéreos ganados, %', 'Duelos ofensivos ganados, %',
             'Acciones defensivas realizadas/90','Interceptaciones/90', 'Tiros interceptados/90', 'Entradas/90', 'Faltas/90',
             'Entradas(ajustado por posesión)','Interceptaciones(ajustado por posesión)',
              'Pases cortos/medios /90', 'Pases largos/90', 'Pases progresivos/90', 'Pases al último tercio/90', 'Carreras progresivas/90',
              'Precisión pases cortos/medios, %','Precisión pases largos, %', 'Precisión pases progresivos, %', 'Precisión pases al último tercio, %',
        ]
df = df2[seleccion]
df = df[df['Minutos jugados']>350]
#-------------------------------------------------------------------------------------------------------------

#AÑADIR UNA COLUMNA DE LA POSICION MÁS UTILIZADA O LA QUE SE CONSIDERARÁ PARA ESTE JUGADOR
df = df.dropna(subset=['Posición específica'])

pos_central = ['RCB', 'LCB', 'CB']
pos_carril = ['LB', 'LWB', 'RB', 'RWB', 'RW', 'RWF', 'LW', 'LWF']
pos_vol_def = ['RDMF', 'LDMF', 'DMF', 'RCMF', 'LCMF']
pos_vol_of = ['RAMF', 'LAMF', 'AMF']
pos_del = ['CF']

def comparar_listaystr(lista, cadena):
    valores_str = cadena.split(',') #si le coloco (', ') aparecerían en mas de una posicion los jugadores
    # Compara los valores de la lista con los valores de la cadena
    for valor in valores_str:
        if valor in lista:
            return True
    return False
posiciones = ['Defensa central', 'Carrilero/extemo', 'Mediocampista 1era línea', 'Mediocampista 2da línea', 'Delantero centro']

df[posiciones[0]] = df['Posición específica'].apply(lambda x: comparar_listaystr(pos_central, x))
df[posiciones[1]] = df['Posición específica'].apply(lambda x: comparar_listaystr(pos_carril, x))
df[posiciones[2]] = df['Posición específica'].apply(lambda x: comparar_listaystr(pos_vol_def, x))
df[posiciones[3]] = df['Posición específica'].apply(lambda x: comparar_listaystr(pos_vol_of, x))
df[posiciones[4]] = df['Posición específica'].apply(lambda x: comparar_listaystr(pos_del, x))
#--------------------------------------------------------------------------------------------------------------

#FUNCION PARA HALLAR LA MEDIA: SERVIRA PARA LA MEDIA DE MELGAR Y DEL TORNEO EN GENERAL
def mean_metrics(df,name_col):
    columnas_numericas = df.select_dtypes(include='number')
    promedios = columnas_numericas.mean().to_dict()
    promedios = {clave: [valor] for clave, valor in promedios.items()} #colocar el valor en una lista para poder crear un dataframe con esto
    promedios['Jugador'] = name_col
    df_promedios = pd.DataFrame(promedios)
    return df_promedios









