import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Conectarse a la base de datos SQLite
conn=sqlite3.connect('bookmaker.db')

#leer la tabla de equipos
equipos=pd.read_sql_query("SELECT * FROM equipos",conn)

#Empezamos con el análisis de los datos