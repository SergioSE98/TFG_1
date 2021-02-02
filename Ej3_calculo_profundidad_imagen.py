# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:58:16 2021

@author: Sergio
"""

import numpy as np

import astropy as astropy 

import pandas as pandas

import seaborn as seaborn

import matplotlib.pyplot as plt

from astropy.table import Table    #Ojo importante aquí importar "Table" con mayuscula

#Voy a leer el archivo fits
dat=Table.read("Sharks_sgp_e_2_cat_small.fits", format="fits")
df=dat.to_pandas()

#Asigno variables a las columnas que me interesa usar
ALPHA_J2000 = df["ALPHA_J2000"]
DELTA_J2000 = df["DELTA_J2000"]
THRESHOLD = df["THRESHOLD"]
BACKGROUND = df["BACKGROUND"]
MAGERR_AUTO = df["MAGERR_AUTO"]
FWHM_WORLD = df["FWHM_WORLD"]



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


result = [(MAGERR_AUTO<=(x+0.005)) & (MAGERR_AUTO>=(x-0.005))]


print(result)

positions = np.flatnonzero(result)
filtered_df=df.iloc[positions]
print(filtered_df)

filtrado=filtered_df["MAGERR_AUTO"]
print(filtrado)

media=np.mean(filtrado)
print(media)
plt.figure("filtrado")
imag1 = seaborn.distplot(filtrado)

