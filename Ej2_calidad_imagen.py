# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:23:09 2021

@author: Sergio
"""

#Vamos a crear un porgrama para caracterizar la calidad de la imágen asociada al archivo fits que ya usamos en el primer ejercicio.

#Import librerías 

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

#Imprimo las gráficas de dispersión de interés.
i1=plt.figure("THRESHOLD")
imag1 = seaborn.scatterplot(ALPHA_J2000, DELTA_J2000, THRESHOLD, s=7)  #Ese "s" que añado en "size" cambia tamaño de puntos

i2=plt.figure("BACKGROUND")
imag2 = seaborn.scatterplot(ALPHA_J2000, DELTA_J2000, BACKGROUND, s=7)

i3=plt.figure("1.086/MAGERR_AUTO")   
imag3 = seaborn.scatterplot(ALPHA_J2000, DELTA_J2000,1.086/MAGERR_AUTO, s=7)

i4=plt.figure("FWHM_WORLD")
imag4 = seaborn.scatterplot(ALPHA_J2000, DELTA_J2000, FWHM_WORLD, s=7)

#Guardo las imágenes en formato png

i1.savefig('THRESHOLD scatter plot.png')  
i2.savefig('BACKGROUND scatter plot.png')  
i3.savefig('1.086_MAGERR_AUTO  scatter plot.png')    #La leyenda en esta figura no muestra el 1.086/, pero va dividiendo.
i4.savefig('FWHM_WORLD scatter plot.png')  