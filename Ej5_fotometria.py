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
df1=dat1.to_pandas()

dat2=Table.read("VIKING_Ks.fit", format="fits")   
df2=dat2.to_pandas()

dec1 = df1["DELTA_J2000"]
ra1 = df1["ALPHA_J2000"]
mag1 = df1["MAG_AUTO"]

dec2 = df2["DEJ2000"]
ra2 = df2["RAJ2000"]
mag2 = df2["Ksap3"]   #Kspmag es petrosian magnitude. También: Ksap3, Ksap4, Ksap6 (fuentes puntuales) y Ksapc3, Ksapc4, Ksap6...

rad=0.000277778   #Un segundo sexagesimal (segundo de arco en grados, las unidades en que se expresan ra1...)
nside=4096 # healpix nside
maxmatch=1 # return closest match 

#Uso la función match para hacer el matching de los catálogos, llamando a las funciones antes definidas. 

matches_viking = smatch.match(ra1, dec1, rad, ra2, dec2, nside=nside, maxmatch=maxmatch)  #Matching SHARKS-VIKING

MAG_SHARKS  = mag1[matches_viking['i1']]
MAG_VIKING = mag2[matches_viking['i2']]

#Creo mask para evitar valores nulos
#mask = (MAG_SHARKS>0)&(MAG_SHARKS<30)&(MAG_VIKING>0)&(MAG_VIKING<30)

MAG_SHARKS_NEW = MAG_SHARKS#[mask]

MAG_VIKING_NEW = MAG_VIKING#[mask]


print(MAG_SHARKS_NEW)

print(MAG_VIKING_NEW)

dif=[]
for r1,r2 in zip(MAG_SHARKS_NEW,MAG_VIKING_NEW):
    #print(r1,r2)
    dif.append(r2-r1)  #multi por 3600 para pasar a grados
    
#seaborn.distplot(dif)
#seaborn.scatterplot(MAG_SHARKS_NEW, dif, s=10)
seaborn.scatterplot(MAG_SHARKS_NEW, MAG_VIKING_NEW, s=10)