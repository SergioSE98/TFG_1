# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 22:07:32 2021

@author: Sergio
"""

import numpy as np

import astropy as astropy 

import pandas as pd

import seaborn as seaborn

import matplotlib.pyplot as plt

from astropy.table import Table, vstack    #Ojo importante aquí importar "Table" con mayuscula

from openpyxl import Workbook


df_1=Table.read("fits/sharks_and_des_sig_noise_5_lite.fits", format="fits")  #Obj en sharks y des, con 5sigma

df_2 = Table.read("fits/sharks_only_not_des_lite.fits", format="fits") #Obj solo en Sharks, muestra ya limpiada de difracciones y grandes errores

#El dataframe 1 ya está limpio de sig/noise menor a 5, el 2 lo limpio ahora.

ks_mag_error = df_2["PETROMAGERR"]
mask_5_sigma = (ks_mag_error <= 1.086/5)

#Filtro mi dataframe y lo renombro, ahora solo con objetos que considero validos (con signal/noise mayor que 5)

df_2 = df_2[mask_5_sigma]

#Ahora diferencio EROS en el dataframe1, los del taframe 2 son todo EROS.

mag_sharks = df_1["PETROMAG"]   #Consultar si debería cambiar esto por magnitud de otra apertura.
mag_err_sharks = df_1["PETROMAGERR"]
mag_des_i = df_1["MAG_AUTO_I_DERED"]
mag_des_g = df_1["MAG_AUTO_G_DERED"]
mag_des_r = df_1["MAG_AUTO_R_DERED"]

eros_mask = ((mag_des_r - mag_sharks) > 4.32)   #En primer lugar filtro los EROS del df con obj en sharks y des, los de solo sharks es pq directamente ya se pueden tratar como eros (no se detectan en optico)

df_eros = df_1[eros_mask]   #Cambio mi df y lo acoto a EROS



#Filtro los objetos que tienen detección en r

mag_des_r = df_eros["MAG_AUTO_R_DERED"]

mask_r_detec = (mag_des_r < 95)

df = df_eros[mask_r_detec]  #Esto lo llamo al final del programa 



mag_ks = df["PETROMAG"]

mask_05 = (mag_ks<19.2)#&(mag_des_r <= 24.65)  #Si aplico las dos condiciones, se limita el numero de objetos (pierdo objetos)
mask_098 = (mag_ks>=19.2)#&(mag_des_r > 24.65)

df_098 = df[mask_098]
df_05 = df[mask_05]

#Empiezo con 0.5

classstat = df_05["CLASSSTAT"]

mask_galaxies = (classstat < 0.5)

mask_stars = (classstat >= 0.5)

df_galaxies = df_05[mask_galaxies]

df_stars = df_05[mask_stars]

#Ya tengo diferenciadas galaxias y estrellas

#Ahora puedo empezar a usar los dataframes que diferencian galaxias y estrellas con las máscaras numeradas, y sacar lo que me interesa.

#El sufijo "g" lo uso de ahora en adelante para considerar galaxias, y el sufijo "s" para estrellas (stars)

mag_ks_g = df_galaxies["PETROMAG"]

mask_0_g = (mag_ks_g >= 13.7)&(mag_ks_g < 14.2)
mask_1_g = (mag_ks_g >= 14.2)&(mag_ks_g < 14.7)
mask_2_g = (mag_ks_g >= 14.7)&(mag_ks_g < 15.2)
mask_3_g = (mag_ks_g >= 15.2)&(mag_ks_g < 15.7)
mask_4_g = (mag_ks_g >= 15.7)&(mag_ks_g < 16.2)
mask_5_g = (mag_ks_g >= 16.2)&(mag_ks_g < 16.7)
mask_6_g = (mag_ks_g >= 16.7)&(mag_ks_g < 17.2)
mask_7_g = (mag_ks_g >= 17.2)&(mag_ks_g < 17.7)
mask_8_g = (mag_ks_g >= 17.7)&(mag_ks_g < 18.2)
mask_9_g = (mag_ks_g >= 18.2)&(mag_ks_g < 18.7)  #A partir de 18.2 para EROs
mask_10_g = (mag_ks_g >= 18.7)&(mag_ks_g < 19.2)
mask_11_g = (mag_ks_g >= 19.2)&(mag_ks_g < 19.7)
mask_12_g = (mag_ks_g >= 19.7)&(mag_ks_g < 20.2)
mask_13_g = (mag_ks_g >= 20.2)&(mag_ks_g < 20.7)
mask_14_g = (mag_ks_g >= 20.7)&(mag_ks_g < 21.2)
mask_15_g = (mag_ks_g >= 21.2)&(mag_ks_g < 21.7)
mask_16_g = (mag_ks_g >= 21.7)&(mag_ks_g < 22.2)
mask_17_g = (mag_ks_g >= 22.2)&(mag_ks_g < 22.7)

df_galaxies_0 = df_galaxies[mask_0_g]
df_galaxies_1 = df_galaxies[mask_1_g]
df_galaxies_2 = df_galaxies[mask_2_g]
df_galaxies_3 = df_galaxies[mask_3_g]
df_galaxies_4 = df_galaxies[mask_4_g]
df_galaxies_5 = df_galaxies[mask_5_g]
df_galaxies_6 = df_galaxies[mask_6_g]
df_galaxies_7 = df_galaxies[mask_7_g]
df_galaxies_8 = df_galaxies[mask_8_g]
df_galaxies_9_05 = df_galaxies[mask_9_g]
df_galaxies_10_05 = df_galaxies[mask_10_g]
df_galaxies_11_05 = df_galaxies[mask_11_g]
df_galaxies_12_05 = df_galaxies[mask_12_g]
df_galaxies_13_05 = df_galaxies[mask_13_g]
df_galaxies_14_05 = df_galaxies[mask_14_g]
df_galaxies_15_05 = df_galaxies[mask_15_g]
df_galaxies_16_05 = df_galaxies[mask_16_g]
df_galaxies_17_05 = df_galaxies[mask_17_g]

#Calculo los R-Ks de cada sección 





mag_ks_s = df_stars["PETROMAG"]

mask_0_s = (mag_ks_s >= 13.7)&(mag_ks_s < 14.2)
mask_1_s =  (mag_ks_s >= 14.2)&(mag_ks_s < 14.7)
mask_2_s = (mag_ks_s >= 14.7)&(mag_ks_s < 15.2)
mask_3_s = (mag_ks_s >= 15.2)&(mag_ks_s < 15.7)
mask_4_s = (mag_ks_s >= 15.7)&(mag_ks_s < 16.2)
mask_5_s = (mag_ks_s >= 16.2)&(mag_ks_s < 16.7)
mask_6_s = (mag_ks_s >= 16.7)&(mag_ks_s < 17.2)
mask_7_s = (mag_ks_s >= 17.2)&(mag_ks_s < 17.7)
mask_8_s = (mag_ks_s >= 17.7)&(mag_ks_s < 18.2)
mask_9_s = (mag_ks_s >= 18.2)&(mag_ks_s < 18.7)
mask_10_s = (mag_ks_s >= 18.7)&(mag_ks_s < 19.2)
mask_11_s = (mag_ks_s >= 19.2)&(mag_ks_s < 19.7)
mask_12_s = (mag_ks_s >= 19.7)&(mag_ks_s < 20.2)
mask_13_s = (mag_ks_s >= 20.2)&(mag_ks_s < 20.7)
mask_14_s = (mag_ks_s >= 20.7)&(mag_ks_s < 21.2)
mask_15_s = (mag_ks_s >= 21.2)&(mag_ks_s < 21.7)
mask_16_s = (mag_ks_s >= 21.7)&(mag_ks_s < 22.2)
mask_17_s = (mag_ks_s >= 22.2)&(mag_ks_s < 22.7)

df_stars_0 = df_stars[mask_0_s]
df_stars_1 = df_stars[mask_1_s]
df_stars_2 = df_stars[mask_2_s]
df_stars_3 = df_stars[mask_3_s]
df_stars_4 = df_stars[mask_4_s]
df_stars_5 = df_stars[mask_5_s]
df_stars_6 = df_stars[mask_6_s]
df_stars_7 = df_stars[mask_7_s]
df_stars_8 = df_stars[mask_8_s]
df_stars_9 = df_stars[mask_9_s]
df_stars_10 = df_stars[mask_10_s]
df_stars_11 = df_stars[mask_11_s]
df_stars_12 = df_stars[mask_12_s]
df_stars_13 = df_stars[mask_13_s]
df_stars_14 = df_stars[mask_14_s]
df_stars_15 = df_stars[mask_15_s]
df_stars_16 = df_stars[mask_16_s]
df_stars_17 = df_stars[mask_17_s]



#Ahora calculo el num de estrellas y galaxias, para cada rango.

galaxie_0 = len(df_galaxies_0)
galaxie_1 = len(df_galaxies_1)
galaxie_2 = len(df_galaxies_2)
galaxie_3 = len(df_galaxies_3)
galaxie_4 = len(df_galaxies_4)
galaxie_5 = len(df_galaxies_5)
galaxie_6 = len(df_galaxies_6)
galaxie_7 = len(df_galaxies_7)
galaxie_8 = len(df_galaxies_8)
galaxie_9 = len(df_galaxies_9_05)
galaxie_10 = len(df_galaxies_10_05)
galaxie_11 = len(df_galaxies_11_05)
galaxie_12 = len(df_galaxies_12_05)
galaxie_13 = len(df_galaxies_13_05)
galaxie_14 = len(df_galaxies_14_05)
galaxie_15 = len(df_galaxies_15_05)
galaxie_16 = len(df_galaxies_16_05)
galaxie_17 = len(df_galaxies_17_05)



galaxies_list_05 = np.array([galaxie_0, galaxie_1, galaxie_2, galaxie_3, galaxie_4, galaxie_5, galaxie_6, galaxie_7, galaxie_8, galaxie_9, galaxie_10, galaxie_11, galaxie_12, galaxie_13, galaxie_14, galaxie_15, galaxie_16, galaxie_17])



star_0 = len(df_stars_0)
star_1 = len(df_stars_1)
star_2 = len(df_stars_2)
star_3 = len(df_stars_3)
star_4 = len(df_stars_4)
star_5 = len(df_stars_5)
star_6 = len(df_stars_6)
star_7 = len(df_stars_7)
star_8 = len(df_stars_8)
star_9 = len(df_stars_9)
star_10 = len(df_stars_10)
star_11 = len(df_stars_11)
star_12 = len(df_stars_12)
star_13 = len(df_stars_13)
star_14 = len(df_stars_14)
star_15 = len(df_stars_15)
star_16 = len(df_stars_16)
star_17 = len(df_stars_17)


stars_list_05 = np.array([star_0, star_1, star_2, star_3, star_4, star_5, star_6, star_7, star_8, star_9, star_10, star_11, star_12, star_13, star_14, star_15, star_16, star_17])



#Sigo con 0.98


classstat = df_098["CLASSSTAT"]

mask_galaxies = (classstat < 0.975)

mask_stars = (classstat >= 0.975)

df_galaxies = df_098[mask_galaxies]

df_stars = df_098[mask_stars]

#Ya tengo diferenciadas galaxias y estrellas

#Ahora puedo empezar a usar los dataframes que diferencian galaxias y estrellas con las máscaras numeradas, y sacar lo que me interesa.

#El sufijo "g" lo uso de ahora en adelante para considerar galaxias, y el sufijo "s" para estrellas (stars)

mag_ks_g = df_galaxies["PETROMAG"]

mask_0_g = (mag_ks_g >= 13.7)&(mag_ks_g < 14.2)
mask_1_g = (mag_ks_g >= 14.2)&(mag_ks_g < 14.7)
mask_2_g = (mag_ks_g >= 14.7)&(mag_ks_g < 15.2)
mask_3_g = (mag_ks_g >= 15.2)&(mag_ks_g < 15.7)
mask_4_g = (mag_ks_g >= 15.7)&(mag_ks_g < 16.2)
mask_5_g = (mag_ks_g >= 16.2)&(mag_ks_g < 16.7)
mask_6_g = (mag_ks_g >= 16.7)&(mag_ks_g < 17.2)
mask_7_g = (mag_ks_g >= 17.2)&(mag_ks_g < 17.7)
mask_8_g = (mag_ks_g >= 17.7)&(mag_ks_g < 18.2)
mask_9_g = (mag_ks_g >= 18.2)&(mag_ks_g < 18.7)
mask_10_g = (mag_ks_g >= 18.7)&(mag_ks_g < 19.2)
mask_11_g = (mag_ks_g >= 19.2)&(mag_ks_g < 19.7)
mask_12_g = (mag_ks_g >= 19.7)&(mag_ks_g < 20.2)
mask_13_g = (mag_ks_g >= 20.2)&(mag_ks_g < 20.7)
mask_14_g = (mag_ks_g >= 20.7)&(mag_ks_g < 21.2)
mask_15_g = (mag_ks_g >= 21.2)&(mag_ks_g < 21.7)
mask_16_g = (mag_ks_g >= 21.7)&(mag_ks_g < 22.2)
mask_17_g = (mag_ks_g >= 22.2)&(mag_ks_g < 22.7)

df_galaxies_0 = df_galaxies[mask_0_g]
df_galaxies_1 = df_galaxies[mask_1_g]
df_galaxies_2 = df_galaxies[mask_2_g]
df_galaxies_3 = df_galaxies[mask_3_g]
df_galaxies_4 = df_galaxies[mask_4_g]
df_galaxies_5 = df_galaxies[mask_5_g]
df_galaxies_6 = df_galaxies[mask_6_g]
df_galaxies_7 = df_galaxies[mask_7_g]
df_galaxies_8 = df_galaxies[mask_8_g]
df_galaxies_9_098 = df_galaxies[mask_9_g]
df_galaxies_10_098 = df_galaxies[mask_10_g]
df_galaxies_11_098 = df_galaxies[mask_11_g]
df_galaxies_12_098 = df_galaxies[mask_12_g]
df_galaxies_13_098 = df_galaxies[mask_13_g]
df_galaxies_14_098 = df_galaxies[mask_14_g]
df_galaxies_15_098 = df_galaxies[mask_15_g]
df_galaxies_16_098 = df_galaxies[mask_16_g]
df_galaxies_17_098 = df_galaxies[mask_17_g]








mag_ks_s = df_stars["PETROMAG"]

mask_0_s = (mag_ks_s >= 13.7)&(mag_ks_s < 14.2)
mask_1_s =  (mag_ks_s >= 14.2)&(mag_ks_s < 14.7)
mask_2_s = (mag_ks_s >= 14.7)&(mag_ks_s < 15.2)
mask_3_s = (mag_ks_s >= 15.2)&(mag_ks_s < 15.7)
mask_4_s = (mag_ks_s >= 15.7)&(mag_ks_s < 16.2)
mask_5_s = (mag_ks_s >= 16.2)&(mag_ks_s < 16.7)
mask_6_s = (mag_ks_s >= 16.7)&(mag_ks_s < 17.2)
mask_7_s = (mag_ks_s >= 17.2)&(mag_ks_s < 17.7)
mask_8_s = (mag_ks_s >= 17.7)&(mag_ks_s < 18.2)
mask_9_s = (mag_ks_s >= 18.2)&(mag_ks_s < 18.7)
mask_10_s = (mag_ks_s >= 18.7)&(mag_ks_s < 19.2)
mask_11_s = (mag_ks_s >= 19.2)&(mag_ks_s < 19.7)
mask_12_s = (mag_ks_s >= 19.7)&(mag_ks_s < 20.2)
mask_13_s = (mag_ks_s >= 20.2)&(mag_ks_s < 20.7)
mask_14_s = (mag_ks_s >= 20.7)&(mag_ks_s < 21.2)
mask_15_s = (mag_ks_s >= 21.2)&(mag_ks_s < 21.7)
mask_16_s = (mag_ks_s >= 21.7)&(mag_ks_s < 22.2)
mask_17_s = (mag_ks_s >= 22.2)&(mag_ks_s < 22.7)

df_stars_0 = df_stars[mask_0_s]
df_stars_1 = df_stars[mask_1_s]
df_stars_2 = df_stars[mask_2_s]
df_stars_3 = df_stars[mask_3_s]
df_stars_4 = df_stars[mask_4_s]
df_stars_5 = df_stars[mask_5_s]
df_stars_6 = df_stars[mask_6_s]
df_stars_7 = df_stars[mask_7_s]
df_stars_8 = df_stars[mask_8_s]
df_stars_9 = df_stars[mask_9_s]
df_stars_10 = df_stars[mask_10_s]
df_stars_11 = df_stars[mask_11_s]
df_stars_12 = df_stars[mask_12_s]
df_stars_13 = df_stars[mask_13_s]
df_stars_14 = df_stars[mask_14_s]
df_stars_15 = df_stars[mask_15_s]
df_stars_16 = df_stars[mask_16_s]
df_stars_17 = df_stars[mask_17_s]



#Ahora calculo el num de estrellas y galaxias, para cada rango.

galaxie_0 = len(df_galaxies_0)
galaxie_1 = len(df_galaxies_1)
galaxie_2 = len(df_galaxies_2)
galaxie_3 = len(df_galaxies_3)
galaxie_4 = len(df_galaxies_4)
galaxie_5 = len(df_galaxies_5)
galaxie_6 = len(df_galaxies_6)
galaxie_7 = len(df_galaxies_7)
galaxie_8 = len(df_galaxies_8)
galaxie_9 = len(df_galaxies_9_098)
galaxie_10 = len(df_galaxies_10_098)
galaxie_11 = len(df_galaxies_11_098)
galaxie_12 = len(df_galaxies_12_098)
galaxie_13 = len(df_galaxies_13_098)
galaxie_14 = len(df_galaxies_14_098)
galaxie_15 = len(df_galaxies_15_098)
galaxie_16 = len(df_galaxies_16_098)
galaxie_17 = len(df_galaxies_17_098)



galaxies_list_098 = np.array([galaxie_0, galaxie_1, galaxie_2, galaxie_3, galaxie_4, galaxie_5, galaxie_6, galaxie_7, galaxie_8, galaxie_9, galaxie_10, galaxie_11, galaxie_12, galaxie_13, galaxie_14, galaxie_15, galaxie_16, galaxie_17])



star_0 = len(df_stars_0)
star_1 = len(df_stars_1)
star_2 = len(df_stars_2)
star_3 = len(df_stars_3)
star_4 = len(df_stars_4)
star_5 = len(df_stars_5)
star_6 = len(df_stars_6)
star_7 = len(df_stars_7)
star_8 = len(df_stars_8)
star_9 = len(df_stars_9)
star_10 = len(df_stars_10)
star_11 = len(df_stars_11)
star_12 = len(df_stars_12)
star_13 = len(df_stars_13)
star_14 = len(df_stars_14)
star_15 = len(df_stars_15)
star_16 = len(df_stars_16)
star_17 = len(df_stars_17)


stars_list_098 = np.array([star_0, star_1, star_2, star_3, star_4, star_5, star_6, star_7, star_8, star_9, star_10, star_11, star_12, star_13, star_14, star_15, star_16, star_17])


stars_total = stars_list_05 + stars_list_098
galaxies_total = galaxies_list_05 + galaxies_list_098



#Haciendo esto tengo ya clasificados en estrella/galaxia mis EROs con detección en r


area_sharks = 7.23 #revisar, este dato no lo recuero y perdí el correo que me decía Aurelio, es en grados de arco

N_stars = stars_total/area_sharks
N_galaxies = galaxies_total/area_sharks

area_sharks_mins = 7.23*3600 #revisar, este dato no lo recuero y perdí el correo que me decía Aurelio, es en grados de arco

N_stars_mins = stars_total/area_sharks_mins
N_galaxies_mins = galaxies_total/area_sharks_mins


ks_mitad_intervalos = ([14.2, 14.7, 15.2, 15.7, 16.2, 16.7, 17.2, 17.7, 18.2, 18.7, 19.2, 19.7, 20.2, 20.7, 21.2, 21.7, 22.2, 22.7])




#Junto todas las galaxias que me interesan de cada rango en dataframes

df_galaxies_9 = vstack([df_galaxies_9_05, df_galaxies_9_098])
df_galaxies_10 = vstack([df_galaxies_10_05, df_galaxies_10_098])
df_galaxies_11 = vstack([df_galaxies_11_05, df_galaxies_11_098])
df_galaxies_12 = vstack([df_galaxies_12_05, df_galaxies_12_098])
df_galaxies_13 = vstack([df_galaxies_13_05, df_galaxies_13_098])
df_galaxies_14 = vstack([df_galaxies_14_05, df_galaxies_14_098])
df_galaxies_15 = vstack([df_galaxies_15_05, df_galaxies_15_098])
df_galaxies_16 = vstack([df_galaxies_16_05, df_galaxies_16_098])
df_galaxies_17 = vstack([df_galaxies_17_05, df_galaxies_17_098])

df_galaxies_all = vstack([df_galaxies_9, df_galaxies_10, df_galaxies_11, df_galaxies_12, df_galaxies_13, df_galaxies_14, df_galaxies_15, df_galaxies_16, df_galaxies_17])
#Con esto


r_Ks_9 = df_galaxies_9["MAG_AUTO_R_DERED"] - df_galaxies_9["PETROMAG"]
r_Ks_10 = df_galaxies_10["MAG_AUTO_R_DERED"] - df_galaxies_10["PETROMAG"]
r_Ks_11 = df_galaxies_11["MAG_AUTO_R_DERED"] - df_galaxies_11["PETROMAG"]
r_Ks_12 = df_galaxies_12["MAG_AUTO_R_DERED"] - df_galaxies_12["PETROMAG"]
r_Ks_13= df_galaxies_13["MAG_AUTO_R_DERED"] - df_galaxies_13["PETROMAG"]
r_Ks_14 = df_galaxies_14["MAG_AUTO_R_DERED"] - df_galaxies_14["PETROMAG"]
r_Ks_15 = df_galaxies_15["MAG_AUTO_R_DERED"] - df_galaxies_15["PETROMAG"]
r_Ks_16 = df_galaxies_16["MAG_AUTO_R_DERED"] - df_galaxies_16["PETROMAG"]
r_Ks_17 = df_galaxies_17["MAG_AUTO_R_DERED"] - df_galaxies_17["PETROMAG"]

plt.figure()
plt.subplot(421)
plt.xlim(4,10)
plt.hist(r_Ks_10,bins = 10)
plt.subplot(422)
plt.xlim(4,10)
plt.hist(r_Ks_11,bins = 25)
plt.subplot(423)
plt.xlim(4,10)
plt.hist(r_Ks_12,bins = 25)
plt.subplot(424)
plt.xlim(4,10)
plt.hist(r_Ks_13,bins = 25)
plt.subplot(425)
plt.xlim(4,10)
plt.hist(r_Ks_14,bins = 25)
plt.subplot(426)
plt.xlim(4,10)
plt.hist(r_Ks_15,bins = 25)
plt.subplot(427)
plt.xlim(4,10)
plt.hist(r_Ks_16,bins = 25)
plt.subplot(428)
plt.xlim(4,10)
plt.hist(r_Ks_17,bins = 25)
plt.show()


plt.figure()
plt.plot(df_galaxies_all["PETROMAG"], df_galaxies_all["MAG_AUTO_R_DERED"] - df_galaxies_all["PETROMAG"], marker = ".", markersize = 1, linestyle="None")

#Puedo sacar tmbn las medias de cada R-Ks  en cada intervalo

r_Ks_medios = [np.mean(r_Ks_10), np.mean(r_Ks_11), np.mean(r_Ks_12), np.mean(r_Ks_13), np.mean(r_Ks_14), np.mean(r_Ks_15), np.mean(r_Ks_16), np.mean(r_Ks_17)]
print(r_Ks_medios)













