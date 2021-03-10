# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:40:22 2021

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
dat=Table.read("Sharks_sgpe.fits", format="fits")
df=dat.to_pandas()

#Asigno variables a las columnas que me interesa usar
RA = df["RA"]
DEC = df["DEC"]
#THRESHOLD = df["THRESHOLD"]
#BACKGROUND = df["BACKGROUND"]
APERMAG3ERR = df["APERMAG3ERR"]
#FWHM_WORLD = df["FWHM_WORLD"]

#Imprimo las gráficas de dispersión de interés.
#i1=plt.figure("THRESHOLD")
#imag1 = seaborn.scatterplot(RA, DEC, THRESHOLD, s=7)  #Ese "s" que añado en "size" cambia tamaño de puntos

#i2=plt.figure("BACKGROUND")
#imag2 = seaborn.scatterplot(RA, DEC, BACKGROUND, s=7)

i3=plt.figure("1.086/Magnitude_Error")   
plt.title("1.086/Magnitude error")
imag3 = seaborn.scatterplot(RA, DEC,1.086/APERMAG3ERR, s=7)

#i4=plt.figure("FWHM_WORLD")
#imag4 = seaborn.scatterplot(RA, DEC, FWHM_WORLD, s=7)

#Guardo las imágenes en formato png

#i1.savefig('THRESHOLD scatter plot.png')  
#i2.savefig('BACKGROUND scatter plot.png')  
i3.savefig('1.086_Magnitude_Error  scatter plot.png')    #La leyenda en esta figura no muestra el 1.086/, pero va dividiendo.
#i4.savefig('FWHM_WORLD scatter plot.png')  