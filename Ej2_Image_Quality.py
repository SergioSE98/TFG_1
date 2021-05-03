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

from astropy.table import Table, vstack    #Ojo importante aquí importar "Table" con mayuscula

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

"""
i2=plt.figure("Ellipticity of stars")
plt.title("Ellipticity of stars")
imag2 = seaborn.scatterplot(RA_mask1, DEC_mask1, ELL_masked1, s=7, legend = "brief")

i3=plt.figure("Ellipticity of galaxies")
plt.title("Ellipticity of galaxies")
imag3 = seaborn.scatterplot(RA_mask2, DEC_mask2, ELL_masked2, s=7, legend = "brief")
"""
signal_to_noise = 1.086/APERMAG3ERR

i4=plt.figure("1.086/Magnitude_Error (Signal to noise ratio)")   
plt.title("1.086/Magnitude error (Signal to noise ratio)")
imag4 = seaborn.scatterplot(RA, DEC, signal_to_noise, s=7, legend = "brief")   #Importante que la leyenda está mal, sale la señal/ruido, no la APERMAG3ERR
imag4.legend(title = "Signal to noise ratio")
#Guardo las imágenes en formato png

i1.savefig('ej_2_skyvar_scatter.png')  

i4.savefig('ej_2_signal_noise_scatter.png')    #La leyenda en esta figura no muestra el 1.086/, pero va dividiendo.


mag_ks = df["PETROMAG"]

mask_05 = (mag_ks<19.2)#&(mag_des_r <= 24.65)  #Si aplico las dos condiciones, se limita el numero de objetos (pierdo objetos)
mask_098 = (mag_ks>=19.2)#&(mag_des_r > 24.65)

df_098 = df[mask_098]
df_05 = df[mask_05]

#Empiezo con 0.5



mask_galaxies = (df_05["CLASSSTAT"] < 0.5)

mask_stars = (df_05["CLASSSTAT"] >= 0.5)

df_galaxies_05 = df_05[mask_galaxies]

df_stars_05 = df_05[mask_stars]



mask_galaxies = (df_098["CLASSSTAT"] < 0.975)

mask_stars = (df_098["CLASSSTAT"]>= 0.975)

df_galaxies_098 = df_098[mask_galaxies]

df_stars_098 = df_098[mask_stars]





df_stars_all = pandas.concat([df_stars_05, df_stars_098])
df_galaxies_all = pandas.concat([df_galaxies_05, df_galaxies_098])


i2=plt.figure("Ellipticity of stars")
plt.title("Ellipticity of stars")
imag2 = seaborn.scatterplot(df_stars_all["RA"], df_stars_all["DEC"], df_stars_all["ELL"], s=7, legend = "brief")

i3=plt.figure("Ellipticity of galaxies")
plt.title("Ellipticity of galaxies")
imag3 = seaborn.scatterplot(df_galaxies_all["RA"], df_galaxies_all["DEC"], df_galaxies_all["ELL"], s=7, legend = "brief")

i2.savefig('ej2_ellipticity_stars_scatter.png')  
i3.savefig("ej2_ellipticity_of_galaxies_scatter.png")




