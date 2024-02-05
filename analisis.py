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

#Ahora borramos las columnas que no necesitamos para el analisis como activado
df.drop(['activado'], axis=1, inplace=True)
#ahora mostramos el dataframe sin la columna activado
df.head()

#Filtramos los equipos que tienen más de 20 de puntaje
umbral_puntaje=20
equipos_con_alto_puntaje=df[df['puntaje']>umbral_puntaje]


#Obtenemos el equipo con el puntaje más alto
equipo_con_mas_puntaje=df[df['puntaje']==df['puntaje'].max()]


#Agrupar por pais y obtener el promedio de puntaje
promedio_puntaje_por_pais=df.groupby('pais')['puntaje'].mean()
#ordenamos los datos de menor a mayor
promedio_puntaje_por_pais.sort_values(ascending=True,inplace=True)

print(promedio_puntaje_por_pais)
#HACEMOS UN GRAFICO DE BARRAS PARA MOSTRAR EL PROMEDIO DE PUNTAJE POR PAIS
promedio_puntaje_por_pais.plot(kind='bar')
plt.show()
#Guardamos el grafico en un archivo
plt.savefig('graficas/promedio_puntaje_por_pais.png')


#Ahora vamos a crear un modelo de regrisión lineal para predecir el puntaje de un equipo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Dividir el conjunto de datos en entrenamiento y prueba
X=df['id'].values.reshape(-1,1)
y=df['puntaje'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Crear el modelo de regresión lineal
modelo=LinearRegression()
modelo.fit(X_train,y_train)

#Hacer predicciones
y_pred=modelo.predict(X_test)

#Calcular el error cuadrático medio
mse=mean_squared_error(y_test,y_pred)
print('Error cuadrático medio:',mse) #COMO EL ERROR CUADRÁTICO MEDIO ES MUY ALTO, EL MODELO NO ES BUENO

#calculamos el R2
r2=modelo.score(X_test,y_test)
print('R2:',r2)
#Como obtenemos un R2 NEGATIVO, el modelo no es bueno para predecir el puntaje de un equipo

#Graficar los datos y la recta de regresión
plt.scatter(X_test,y_test)
plt.plot(X_test,y_pred,color='red')
plt.show()
#Guardamos el grafico en un archivo
plt.savefig('graficas/regresion_lineal.png')


