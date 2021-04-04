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
dat=Table.read("fits/sharks_sgpe.fits", format="fits")
df=dat.to_pandas()

#Asigno variables a las columnas que me interesa usar
RA = df["RA"]
DEC = df["DEC"]
SKYVAR = df["SKYVAR"]
CLASSSTAT = df["CLASSSTAT"]
APERMAG3ERR = df["APERMAG3ERR"]
ELL = df["ELL"]

mask1 = (CLASSSTAT>0.95) #Estrellas
mask2 = (CLASSSTAT<0.05) #Galaxias
ELL_masked1 = ELL[mask1]
ELL_masked2 = ELL[mask2]
RA_mask1 = RA[mask1]
DEC_mask1 = DEC[mask1]
RA_mask2 = RA[mask2]
DEC_mask2 = DEC[mask2]



#Imprimo las gráficas de dispersión de interés.
i1=plt.figure("Local estimate of variation in sky level")
plt.title("Local estimate of variation in sky level")
imag1 = seaborn.scatterplot(RA, DEC, SKYVAR, s=7, legend ="brief")  #Ese "s" que añado en "size" cambia tamaño de puntos


i2=plt.figure("Ellipticity of stars")
plt.title("Ellipticity of stars")
imag2 = seaborn.scatterplot(RA_mask1, DEC_mask1, ELL_masked1, s=7, legend = "brief")

i3=plt.figure("Ellipticity of galaxies")
plt.title("Ellipticity of galaxies")
imag3 = seaborn.scatterplot(RA_mask2, DEC_mask2, ELL_masked2, s=7, legend = "brief")

i4=plt.figure("1.086/Magnitude_Error (Signal to noise ratio)")   
plt.title("1.086/Magnitude error (Signal to noise ratio)")
imag4 = seaborn.scatterplot(RA, DEC,1.086/APERMAG3ERR, s=7, legend = "brief")   #Importante que la leyenda está mal, sale la señal/ruido, no la APERMAG3ERR


#Guardo las imágenes en formato png

i1.savefig('Local estimate of variation in sky level.png')  
i2.savefig('Ellipticity of stars.png')  
i3.savefig("Ellipticity of galaxies.png")
i4.savefig('1.086_Magnitude_Error (Signal to noise ratio).png')    #La leyenda en esta figura no muestra el 1.086/, pero va dividiendo.
