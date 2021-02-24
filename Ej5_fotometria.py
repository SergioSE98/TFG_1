# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:59:06 2021

@author: Sergio
"""

import numpy as np

import astropy as astropy 

import pandas as pandas

import seaborn as seaborn

import matplotlib.pyplot as plt

from astropy.table import Table    #Ojo importante aquí importar "Table" con mayuscula

import smatch

#Empiezo haciendo matching de los puntos captados en SHARKS y VIKING

dat1=Table.read("Sharks_sgp_e_2_cat_small.fits", format="fits")

dat2=Table.read("VIKING_Ks.fit", format="fits")   

dec1 = dat1["DELTA_J2000"]
ra1 = dat1["ALPHA_J2000"]
mag1 = dat1["MAG_AUTO"]
err_mag1 = dat1["MAGERR_AUTO"]


dec2 = dat2["DEJ2000"]
ra2 = dat2["RAJ2000"]
mag2 = dat2["Kspmag"]   #Kspmag es petrosian magnitude. También: Ksap3, Ksap4, Ksap6 (fuentes puntuales) y Ksapc3, Ksapc4, Ksap6...
err_mag2 = dat2["e_Kspmag"]

rad=0.000277778   #Un segundo sexagesimal (segundo de arco en grados, las unidades en que se expresan ra1...)
nside=4096 # healpix nside
maxmatch=1 # return closest match 

#Uso la función match para hacer el matching de los catálogos, llamando a las funciones antes definidas. 

matches_viking = smatch.match(ra1, dec1, rad, ra2, dec2, nside=nside, maxmatch=maxmatch)  #Matching SHARKS-VIKING

MAG_SHARKS  = mag1[matches_viking['i1']]
MAG_VIKING = mag2[matches_viking['i2']]
ERROR_MAG_SHARKS = err_mag1[matches_viking["i1"]]
ERROR_MAG_VIKING = err_mag2[matches_viking["i2"]]



#Creo mask para evitar valores nulos
mask = (MAG_SHARKS>0)&(MAG_SHARKS<30)&(MAG_VIKING>0)&(MAG_VIKING<30)&(ERROR_MAG_SHARKS<0.3)&(ERROR_MAG_VIKING<0.3)

#MAGNITUDES "NEW" obtenidas una vez pasada la mask

MAG_SHARKS_NEW = MAG_SHARKS[mask]

MAG_VIKING_NEW = MAG_VIKING[mask]

ERROR_MAG_SHARKS_NEW = ERROR_MAG_SHARKS[mask]

ERROR_MAG_VIKING_NEW = ERROR_MAG_VIKING[mask]


#print(MAG_SHARKS_NEW)

#print(MAG_VIKING_NEW)

dif=MAG_VIKING_NEW-MAG_SHARKS_NEW

#seaborn.distplot(dif)
#seaborn.scatterplot(MAG_SHARKS_NEW, dif, s=10)
#seaborn.scatterplot(MAG_SHARKS_NEW, MAG_VIKING_NEW, s=10)
#plt.plot(MAG_SHARKS_NEW, dif, "o")
#plt.plot(MAG_SHARKS_NEW, MAG_VIKING_NEW, "o")

#Figura 1
plt.figure()
plt.plot(MAG_VIKING_NEW,MAG_SHARKS_NEW,".")
hola=np.polyfit(MAG_VIKING_NEW,MAG_SHARKS_NEW,1)
print(hola)
"""
#Figura 2
plt.figure()
plt.plot(MAG_SHARKS_NEW, MAG_VIKING_NEW, ".")
hola1=np.polyfit(MAG_SHARKS_NEW,MAG_VIKING_NEW,1)
print(hola1)
"""
print(hola[1])
MAG_SHARKS_NEW_2= MAG_SHARKS_NEW-hola[1]

#print(MAG_SHARKS_NEW_2)

plt.plot([10,24],[10,24],MAG_SHARKS_NEW_2,MAG_VIKING_NEW,"g.")

#Figura 3
plt.figure()

xerr_=ERROR_MAG_SHARKS_NEW
yerr_=ERROR_MAG_VIKING_NEW

plt.errorbar(MAG_SHARKS_NEW, MAG_VIKING_NEW, xerr=xerr_, yerr=yerr_,fmt="g.")


print(np.polyfit(MAG_SHARKS_NEW,MAG_VIKING_NEW,1,w=yerr_))





















