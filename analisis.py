import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Conectarse a la base de datos SQLite
conn=sqlite3.connect('bookmaker.db')

#leer la tabla de equipos
query='SELECT * FROM equipos'
df=pd.read_sql(query,conn)

#ANALISIS DE DATOS

#Mostramos la informacion de la tabla
df.info()

#Ahora borramos las columnas que no necesitamos para el analisis como 