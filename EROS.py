# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:00:46 2021

@author: Sergio
"""

import numpy as np

import astropy as astropy 

import pandas as pandas

import seaborn as seaborn

import matplotlib.pyplot as plt

from astropy.table import Table    #Ojo importante aquí importar "Table" con mayuscula

#Leo datos (Objetos comunes de SHARKS y DES)
 

df=Table.read("fits/sharks_and_des_sig_noise_5_lite.fits", format="fits")  #EROS, objetos con R-Ks mayor a 5.5


mag_sharks = df["PETROMAG"]   #Consultar si debería cambiar esto por magnitud de otra apertura.
mag_err_sharks = df["PETROMAGERR"]
mag_des_i = df["MAG_AUTO_I_DERED"]
mag_des_g = df["MAG_AUTO_G_DERED"]
mag_des_r = df["MAG_AUTO_R_DERED"]

eros_mask = ((mag_des_r - mag_sharks) > 4.32)

df_eros = df[eros_mask]   #Cambio mi df y lo acoto a EROS

mag_sharks_eros = df_eros["PETROMAG"]   #Consultar si debería cambiar esto por magnitud de otra apertura.
mag_err_sharks_eros = df_eros["PETROMAGERR"]
mag_des_i_eros = df_eros["MAG_AUTO_I_DERED"]
mag_des_g_eros = df_eros["MAG_AUTO_G_DERED"]
mag_des_r_eros = df_eros["MAG_AUTO_R_DERED"]

print("Número de EROS: %d" %len(df_eros))

not_r_detection_mask = (mag_des_r_eros > 95)

r_detection_mask = (mag_des_r_eros < 95)

df_eros_not_r = df_eros[not_r_detection_mask]

df_eros_r = df_eros[r_detection_mask]

print("Número de EROS sin detección en r: %d" %len(df_eros_not_r))

print("Número de EROS con detección en r: %d" %len(df_eros_r))


#Utilizo los EROS que tienen detección en r.

mag_sharks_eros_r = df_eros_r["PETROMAG"]   #Consultar si debería cambiar esto por magnitud de otra apertura.
mag_err_sharks_eros_r = df_eros_r["PETROMAGERR"]
mag_des_i_eros_r = df_eros_r["MAG_AUTO_I_DERED"]
mag_des_g_eros_r = df_eros_r["MAG_AUTO_G_DERED"]
mag_des_r_eros_r = df_eros_r["MAG_AUTO_R_DERED"]

"""
mag_y = mag_des_r_eros_r - mag_sharks_eros_r

i1 = plt.figure("Magnitudes Sharks and DES objects (s/n = 5)")
plt.title("Magnitudes Sharks and DES objects")
imag2 = plt.plot(mag_sharks_eros_r,mag_y, ".")
plt.xlabel("PETROMAG_")
plt.ylabel("MAG_AUTO_R_DERED - PETROMAG_K")
i1.savefig('Mag_R-Mag_K.png') 
"""

#El límite de detección de Sharks es 22.7 en banda Ks (AB, 5 sigma, lo que tengo yo), no hace falta acotarlo, las medidas llegan approx hasta ahí
#Voy a acotar distintos rangos de magnitud y ver cuántos objetos detecto en cada uno. 

#La mínima magnitud la tomo como en el artículo de daddi, que es 11.7+1.83 = 13.5 (La tomo = 13.7, mucha presencia de contaminación por difracción)

#Establezco entonces rangos 13.7-14.2,    ...,   22.2-22.7

#Creo también un array con el valor intermedio de cada intervalo 
"""
mask_0 = (mag_sharks_eros_r >= 13.7)&(mag_sharks_eros_r < 14.2)
mask_1 = (mag_sharks_eros_r >= 14.2)&(mag_sharks_eros_r < 14.7)
mask_2 = (mag_sharks_eros_r >= 14.7)&(mag_sharks_eros_r < 15.2)
mask_3 = (mag_sharks_eros_r >= 15.2)&(mag_sharks_eros_r < 15.7)
mask_4 = (mag_sharks_eros_r >= 15.7)&(mag_sharks_eros_r < 16.2)
mask_5 = (mag_sharks_eros_r >= 16.2)&(mag_sharks_eros_r < 16.7)
mask_6 = (mag_sharks_eros_r >= 16.7)&(mag_sharks_eros_r < 17.2)
mask_7 = (mag_sharks_eros_r >= 17.2)&(mag_sharks_eros_r < 17.7)
mask_8 = (mag_sharks_eros_r >= 17.7)&(mag_sharks_eros_r < 18.2)
mask_9 = (mag_sharks_eros_r >= 18.2)&(mag_sharks_eros_r < 18.7)
mask_10 = (mag_sharks_eros_r >= 18.7)&(mag_sharks_eros_r < 19.2)
mask_11 = (mag_sharks_eros_r >= 19.2)&(mag_sharks_eros_r < 19.7)
mask_12 = (mag_sharks_eros_r >= 19.7)&(mag_sharks_eros_r < 20.2)
mask_13 = (mag_sharks_eros_r >= 20.2)&(mag_sharks_eros_r < 20.7)
mask_14 = (mag_sharks_eros_r >= 20.7)&(mag_sharks_eros_r < 21.2)
mask_15 = (mag_sharks_eros_r >= 21.2)&(mag_sharks_eros_r < 21.7)
mask_16 = (mag_sharks_eros_r >= 21.7)&(mag_sharks_eros_r < 22.2)
mask_17 = (mag_sharks_eros_r >= 22.2)&(mag_sharks_eros_r < 22.7)
"""

ks_mitad_intervalos = ([13.95, 14.45, 14.95, 15.45, 15.95, 16.45, 16.95, 17.45, 17.95, 18.45, 18.95, 19.45, 19.95, 20.45, 20.95, 21.45, 21.95, 22.45])

ks_mitad_intervalos_estrellas = ks_mitad_intervalos[0:14]


"""
df_0 = df_eros_r[mask_0]
df_1 = df_eros_r[mask_1]
df_2 = df_eros_r[mask_2]
df_3 = df_eros_r[mask_3]
df_4 = df_eros_r[mask_4]
df_5 = df_eros_r[mask_5]
df_6 = df_eros_r[mask_6]
df_7 = df_eros_r[mask_7]
df_8 = df_eros_r[mask_8]
df_9 = df_eros_r[mask_9]
df_10 = df_eros_r[mask_10]
df_11 = df_eros_r[mask_11]
df_12 = df_eros_r[mask_12]
df_13 = df_eros_r[mask_13]
df_14 = df_eros_r[mask_14]
df_15 = df_eros_r[mask_15]
df_16 = df_eros_r[mask_16]
df_17 = df_eros_r[mask_17]
"""

#Para la clasificación de objetos en estrella/galaxia, la tomo valida para ks menor igual que 20  (sería 19.33 realmente), y r menor igual que 24.2 (no considero esto)

#Los objetos con mag mayor son muy tenues y pueden considerarse directamente galaxias, con una pequeña contaminación de enanas marrones (por ser tan tenues)

#Realizo entonces el acotado, ya no pondré lo de eros_r, estoy trabajando solo con esos.


mask_classstat = (mag_sharks_eros_r<=20.5)#&(mag_des_r_eros_r <= 24.2)
mask_all_galaxies = (mag_sharks_eros_r>20.5)#&(mag_des_r_eros_r > 24.2)


df_classstat = df_eros_r[mask_classstat]
df_all_galaxies = df_eros_r[mask_all_galaxies]

print("Número de objetos a clasificar entre estrellas y galaxias: %d" %len(df_classstat))
print("Número de objetos que tomamos directamente como galaxias: %d" %len(df_all_galaxies))

classstat = df_classstat["CLASSSTAT"]

#A su vez, acoto los del classtat entre galaxias y estrellas

mask_classstat_galaxies = (classstat < 0.5)
mask_classstat_stars = (classstat >= 0.5)

df_classstat_galaxies = df_classstat[mask_classstat_galaxies]
df_classstat_stars = df_classstat[mask_classstat_stars]



print("Número de objetos que clasificamos como galaxias: %d" %len(df_classstat_galaxies))
print("Número de objetos que clasificamos como estrellas: %d" %len(df_classstat_stars))


#Ya tengo diferenciadas galaxias y estrellas

#Ahora puedo empezar a usar los dataframes que diferencian galaxias y estrellas con las máscaras numeradas, y sacar lo que me interesa.

#Al tener los df_classtat solo magnitudes Ks menores a 20.5, aplico hasta la mask_13, incluida
#el df_all galaxies  lo aplico desde la mask_13, incluida

mag_sharks_eros_r = df_classstat_galaxies["PETROMAG"]

mask_0 = (mag_sharks_eros_r >= 13.7)&(mag_sharks_eros_r < 14.2)
mask_1 = (mag_sharks_eros_r >= 14.2)&(mag_sharks_eros_r < 14.7)
mask_2 = (mag_sharks_eros_r >= 14.7)&(mag_sharks_eros_r < 15.2)
mask_3 = (mag_sharks_eros_r >= 15.2)&(mag_sharks_eros_r < 15.7)
mask_4 = (mag_sharks_eros_r >= 15.7)&(mag_sharks_eros_r < 16.2)
mask_5 = (mag_sharks_eros_r >= 16.2)&(mag_sharks_eros_r < 16.7)
mask_6 = (mag_sharks_eros_r >= 16.7)&(mag_sharks_eros_r < 17.2)
mask_7 = (mag_sharks_eros_r >= 17.2)&(mag_sharks_eros_r < 17.7)
mask_8 = (mag_sharks_eros_r >= 17.7)&(mag_sharks_eros_r < 18.2)
mask_9 = (mag_sharks_eros_r >= 18.2)&(mag_sharks_eros_r < 18.7)
mask_10 = (mag_sharks_eros_r >= 18.7)&(mag_sharks_eros_r < 19.2)
mask_11 = (mag_sharks_eros_r >= 19.2)&(mag_sharks_eros_r < 19.7)
mask_12 = (mag_sharks_eros_r >= 19.7)&(mag_sharks_eros_r < 20.2)
mask_13 = (mag_sharks_eros_r >= 20.2)&(mag_sharks_eros_r < 20.7)
mask_14 = (mag_sharks_eros_r >= 20.7)&(mag_sharks_eros_r < 21.2)
mask_15 = (mag_sharks_eros_r >= 21.2)&(mag_sharks_eros_r < 21.7)
mask_16 = (mag_sharks_eros_r >= 21.7)&(mag_sharks_eros_r < 22.2)
mask_17 = (mag_sharks_eros_r >= 22.2)&(mag_sharks_eros_r < 22.7)

df_classstat_galaxies_0 = df_classstat_galaxies[mask_0]
df_classstat_galaxies_1 = df_classstat_galaxies[mask_1]
df_classstat_galaxies_2 = df_classstat_galaxies[mask_2]
df_classstat_galaxies_3 = df_classstat_galaxies[mask_3]
df_classstat_galaxies_4 = df_classstat_galaxies[mask_4]
df_classstat_galaxies_5 = df_classstat_galaxies[mask_5]
df_classstat_galaxies_6 = df_classstat_galaxies[mask_6]
df_classstat_galaxies_7 = df_classstat_galaxies[mask_7]
df_classstat_galaxies_8 = df_classstat_galaxies[mask_8]
df_classstat_galaxies_9 = df_classstat_galaxies[mask_9]
df_classstat_galaxies_10 = df_classstat_galaxies[mask_10]
df_classstat_galaxies_11 = df_classstat_galaxies[mask_11]
df_classstat_galaxies_12 = df_classstat_galaxies[mask_12]
df_classstat_galaxies_13 = df_classstat_galaxies[mask_13]

mag_sharks_eros_r = df_classstat_stars["PETROMAG"]

mask_0 = (mag_sharks_eros_r >= 13.7)&(mag_sharks_eros_r < 14.2)
mask_1 = (mag_sharks_eros_r >= 14.2)&(mag_sharks_eros_r < 14.7)
mask_2 = (mag_sharks_eros_r >= 14.7)&(mag_sharks_eros_r < 15.2)
mask_3 = (mag_sharks_eros_r >= 15.2)&(mag_sharks_eros_r < 15.7)
mask_4 = (mag_sharks_eros_r >= 15.7)&(mag_sharks_eros_r < 16.2)
mask_5 = (mag_sharks_eros_r >= 16.2)&(mag_sharks_eros_r < 16.7)
mask_6 = (mag_sharks_eros_r >= 16.7)&(mag_sharks_eros_r < 17.2)
mask_7 = (mag_sharks_eros_r >= 17.2)&(mag_sharks_eros_r < 17.7)
mask_8 = (mag_sharks_eros_r >= 17.7)&(mag_sharks_eros_r < 18.2)
mask_9 = (mag_sharks_eros_r >= 18.2)&(mag_sharks_eros_r < 18.7)
mask_10 = (mag_sharks_eros_r >= 18.7)&(mag_sharks_eros_r < 19.2)
mask_11 = (mag_sharks_eros_r >= 19.2)&(mag_sharks_eros_r < 19.7)
mask_12 = (mag_sharks_eros_r >= 19.7)&(mag_sharks_eros_r < 20.2)
mask_13 = (mag_sharks_eros_r >= 20.2)&(mag_sharks_eros_r < 20.7)
mask_14 = (mag_sharks_eros_r >= 20.7)&(mag_sharks_eros_r < 21.2)
mask_15 = (mag_sharks_eros_r >= 21.2)&(mag_sharks_eros_r < 21.7)
mask_16 = (mag_sharks_eros_r >= 21.7)&(mag_sharks_eros_r < 22.2)
mask_17 = (mag_sharks_eros_r >= 22.2)&(mag_sharks_eros_r < 22.7)

df_classstat_stars_0 = df_classstat_stars[mask_0]
df_classstat_stars_1 = df_classstat_stars[mask_1]
df_classstat_stars_2 = df_classstat_stars[mask_2]
df_classstat_stars_3 = df_classstat_stars[mask_3]
df_classstat_stars_4 = df_classstat_stars[mask_4]
df_classstat_stars_5 = df_classstat_stars[mask_5]
df_classstat_stars_6 = df_classstat_stars[mask_6]
df_classstat_stars_7 = df_classstat_stars[mask_7]
df_classstat_stars_8 = df_classstat_stars[mask_8]
df_classstat_stars_9 = df_classstat_stars[mask_9]
df_classstat_stars_10 = df_classstat_stars[mask_10]
df_classstat_stars_11 = df_classstat_stars[mask_11]
df_classstat_stars_12 = df_classstat_stars[mask_12]
df_classstat_stars_13 = df_classstat_stars[mask_13]

mag_sharks_eros_r = df_all_galaxies["PETROMAG"]

mask_0 = (mag_sharks_eros_r >= 13.7)&(mag_sharks_eros_r < 14.2)
mask_1 = (mag_sharks_eros_r >= 14.2)&(mag_sharks_eros_r < 14.7)
mask_2 = (mag_sharks_eros_r >= 14.7)&(mag_sharks_eros_r < 15.2)
mask_3 = (mag_sharks_eros_r >= 15.2)&(mag_sharks_eros_r < 15.7)
mask_4 = (mag_sharks_eros_r >= 15.7)&(mag_sharks_eros_r < 16.2)
mask_5 = (mag_sharks_eros_r >= 16.2)&(mag_sharks_eros_r < 16.7)
mask_6 = (mag_sharks_eros_r >= 16.7)&(mag_sharks_eros_r < 17.2)
mask_7 = (mag_sharks_eros_r >= 17.2)&(mag_sharks_eros_r < 17.7)
mask_8 = (mag_sharks_eros_r >= 17.7)&(mag_sharks_eros_r < 18.2)
mask_9 = (mag_sharks_eros_r >= 18.2)&(mag_sharks_eros_r < 18.7)
mask_10 = (mag_sharks_eros_r >= 18.7)&(mag_sharks_eros_r < 19.2)
mask_11 = (mag_sharks_eros_r >= 19.2)&(mag_sharks_eros_r < 19.7)
mask_12 = (mag_sharks_eros_r >= 19.7)&(mag_sharks_eros_r < 20.2)
mask_13 = (mag_sharks_eros_r >= 20.2)&(mag_sharks_eros_r < 20.7)
mask_14 = (mag_sharks_eros_r >= 20.7)&(mag_sharks_eros_r < 21.2)
mask_15 = (mag_sharks_eros_r >= 21.2)&(mag_sharks_eros_r < 21.7)
mask_16 = (mag_sharks_eros_r >= 21.7)&(mag_sharks_eros_r < 22.2)
mask_17 = (mag_sharks_eros_r >= 22.2)&(mag_sharks_eros_r < 22.7)

df_all_galaxies_13 = df_all_galaxies[mask_13]
df_all_galaxies_14 = df_all_galaxies[mask_14]
df_all_galaxies_15 = df_all_galaxies[mask_15]
df_all_galaxies_16 = df_all_galaxies[mask_16]
df_all_galaxies_17 = df_all_galaxies[mask_17]


#Ahora calculo el num de estrellas y galaxias, para cada rango.

star_0 = len(df_classstat_stars_0)
star_1 = len(df_classstat_stars_1)
star_2 = len(df_classstat_stars_2)
star_3 = len(df_classstat_stars_3)
star_4 = len(df_classstat_stars_4)
star_5 = len(df_classstat_stars_5)
star_6 = len(df_classstat_stars_6)
star_7 = len(df_classstat_stars_7)
star_8 = len(df_classstat_stars_8)
star_9 = len(df_classstat_stars_9)
star_10 = len(df_classstat_stars_10)
star_11 = len(df_classstat_stars_11)
star_12 = len(df_classstat_stars_12)
star_13 = len(df_classstat_stars_13)

stars_list = ([star_0, star_1, star_2, star_3, star_4, star_5, star_6, star_7, star_8, star_9, star_10, star_11, star_12, star_13])

print(stars_list)
plt.figure()
plt.plot(ks_mitad_intervalos_estrellas,stars_list, "*" ,label="Estrellas")
plt.xlabel("Ks")
plt.ylabel("Estrellas")
plt.legend()











  