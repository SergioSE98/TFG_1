# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:54:05 2021

@author: Sergio
"""


import numpy as np

import astropy as astropy 

import pandas as pandas

import seaborn as seaborn

import matplotlib.pyplot as plt

from astropy.table import Table    #Ojo importante aquí importar "Table" con mayuscula

#Voy a leer el archivo fits
dat=Table.read("fits/sharks_sgpe.fits", format="fits")
df=dat.to_pandas()

#Asigno variables a las columnas que me interesa usar
MAGERR = df["APERMAG3ERR"]

#La profundidad o magnitud límite se da en unidades de 5 veces el error estdístico. Debo por tanto igualar SNR (que era 1.086/magerr_auto) a 5, y despejar 
#el valor del error de la magnitud(magerr), de forma que los objetos que tengan un error en la magnitud de ese valor despejado se detectan con la significancia
#deseada, que es de 5 veces el error estadístico, las unidades usadas para expresar la profundidad o magnitud límite de la imágen. 

#En primer lugar despejo ese valor de MAGERR_AUTO que tiene asociada una significancia de 5 veces el error estadístico.
#1.086/X = 5, luego X = 1.086/5

x=1.086/5

#Ahora selecciono los objetos en el catálogo que se detectan con una significancia de aprox 5 sigma, que es la que asocio a la mag limite o profundidad de la
#imagen (el flujo mínimo que establezco para una significancia, en mi caso 5 sigma). Para ello selecciono los objetos con un error en la magnitud de 
#aprox "X", (entre X-0.005 y X+0.005).

#Con esto sacaremos el valor de la profundidad de la imagen, a partir del cual podré considerar los objetos significativamente brillantes.

#Con "acotado" genero una columna de booleanos (True o False) en función de si se cumple o no la condición establecida, que en
#mi caso es que el valor de MAGERR_AUTO esté comprendido entre x-0.005 y x+0.005

acotado = [(MAGERR<=(x+0.005)) & (MAGERR>=(x-0.005))]  

#print(acotado)

#Ahora lo que hago es crear una misma tabla como la del archivo fits, pero conteniendo solo las filas cuyo MAGERR_AUTO he acotado
#Este trocito de código lo vi en internety funcionó, lo había intentado de otras formas pero no lo conseguía obtener.

positions = np.flatnonzero(acotado)
filtered_df=df.iloc[positions]   #Si quito el corchete en siguiente línea se imprime la tabla completa filtrada.
#print(filtered_df)

#Ahora selecciono de esa tabla (que pasa a tener 408 filas, pues es el número de valores de MAG_AUTO que cumplen la cota establecida)
#la columna MAGERR_AUTO filtrada, con 408 filas, y la llamo "filtrado"

filtrado=filtered_df["APERMAG3"]  #Si quito el corchete en la siguiente línea se imprime la columna MAG_AUTO filtrada.
RA = filtered_df["RA"]
DEC = filtered_df["DEC"]
#print(filtrado)

#Realizo ahora la media de los valores de MAG_AUTO filtrados (los que cumplen la condición establecida), y con eso
#obtengo ya el valor de la profundidad de la imagen.

profundidad_imagen=np.mean(filtrado)
print("The image depth is: %f" % profundidad_imagen)

#Por último realizo un histograma de los valores obtenidos tras el filtrado, aquellos MAG_AUTO que cumplen la condición dada.
#(En internet salía que existía histplot en seaborn, pero a mí no me deja usarlo, así que he usado distplot).

i1 = plt.figure("Magnitude values with an error of approx. 0.21 (to obtain image depth)")    #Ese 0.21 es x=1.086/5
plt.title("Magnitude of objects with $signal/noise \simeq 5$")
imag1 = seaborn.distplot(filtrado,kde=False,norm_hist=False,bins = 60, hist_kws=dict(edgecolor="k", linewidth=2))    #Debo quitar el KDE (un ajuste que hace seaborn) para poder quitar el histograma normalizado
plt.ylabel("Photon counts")
i1.savefig('ej_3_hist_image_depth.png')   #QUitando el hist normalizado ya sí obtengo el núm de cuentas en eje Y.

i2 = plt.figure("Magnitude values with an error of approx 0.21 (to obtain image depth)")
imag2 = seaborn.scatterplot(RA, DEC, filtrado, s=7, legend = "brief")
imag2.set_xlabel("RA [$deg$]" )
imag2.set_ylabel("Dec [$deg$]" )
imag2.invert_xaxis()
#plt.title("Magnitude of objects with $signal/noise \simeq 5$")
i2.savefig("ej_3_scatter_image_depth.png")



imag1 = filtered_df.plot.scatter(x = "RA", y= "DEC", c= "APERMAG3", s=0.1, colormap=cm.jet)
imag1.set_xlabel("RA [$deg$]" )
imag1.set_ylabel("Dec [$deg$]" )
imag1.invert_xaxis()

