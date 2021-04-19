# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:25:18 2021

@author: Sergio
"""

import numpy as np

import astropy as astropy 

import pandas as pd

import seaborn as seaborn

import matplotlib.pyplot as plt

from astropy.table import Table, vstack    #Ojo importante aquí importar "Table" con mayuscula

from openpyxl import Workbook

#Leo datos (Objetos comunes de SHARKS y DES)
 

df=Table.read("fits/sharks_sgpe.fits", format="fits")  #Obj en sharks y des, con 5sigma

#Acoto objetos con signal/noise superior a 5 sigma.

#Para ello considero solo valores de magerr menores a 1.086/5

ks_mag = df["PETROMAG"]
ks_mag_error = df["PETROMAGERR"]

mask_5_sigma = (ks_mag_error <= 1.086/5)

#Filtro mi dataframe y lo renombro, ahora solo con objetos que considero validos (con signal/noise mayor que 5)

df_5 = df[mask_5_sigma]



#Creo lista con mis magnitudes que considero para crear intervalos

"""
ks_mag_list = ([13.7, 14.2, 14.7, 15.2, 15.7, 16.2, 16.7, 17.2, 17.7, 18.2, 18.7, 19.2, 19.7, 20.2, 20.7, 21.2, 21.7, 22.2, 22.7])
suma = 0
numero_list =([])

for i in range(len(ks_mag_list)-1):
    for j in range(len(df_5)-1):
        if (ks_mag[j]  >= ks_mag_list[i])&(ks_mag[j] < ks_mag_list[i+1]):
            suma=suma+1
    numero_list.append(suma)
    suma=0
    
    
print(numero_list)
"""  

#Defino mis variables en el dataframe de objetos de sharks con 5 sigma

classstat = df_5["CLASSSTAT"]


mask_galaxies = (classstat < 0.5)

mask_stars = (classstat >= 0.5)

df_galaxies = df_5[mask_galaxies]

df_stars = df_5[mask_stars]


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
df_galaxies_9 = df_galaxies[mask_9_g]
df_galaxies_10 = df_galaxies[mask_10_g]
df_galaxies_11 = df_galaxies[mask_11_g]
df_galaxies_12 = df_galaxies[mask_12_g]
df_galaxies_13 = df_galaxies[mask_13_g]
df_galaxies_14 = df_galaxies[mask_14_g]
df_galaxies_15 = df_galaxies[mask_15_g]
df_galaxies_16 = df_galaxies[mask_16_g]
df_galaxies_17 = df_galaxies[mask_17_g]

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
galaxie_9 = len(df_galaxies_9)
galaxie_10 = len(df_galaxies_10)
galaxie_11 = len(df_galaxies_11)
galaxie_12 = len(df_galaxies_12)
galaxie_13 = len(df_galaxies_13)
galaxie_14 = len(df_galaxies_14)
galaxie_15 = len(df_galaxies_15)
galaxie_16 = len(df_galaxies_16)
galaxie_17 = len(df_galaxies_17)

galaxies_list = ([galaxie_0, galaxie_1, galaxie_2, galaxie_3, galaxie_4, galaxie_5, galaxie_6, galaxie_7, galaxie_8, galaxie_9, galaxie_10, galaxie_11, galaxie_12, galaxie_13, galaxie_14, galaxie_15, galaxie_16, galaxie_17])


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


stars_list = ([star_0, star_1, star_2, star_3, star_4, star_5, star_6, star_7, star_8, star_9, star_10, star_11, star_12, star_13, star_14, star_15, star_16, star_17])


#ks_mitad_intervalos = ([13.95, 14.45, 14.95, 15.45, 15.95, 16.45, 16.95, 17.45, 17.95, 18.45, 18.95, 19.45, 19.95, 20.45, 20.95, 21.45, 21.95, 22.45])
ks_mitad_intervalos = ([14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5])
#Plots sencillitos, hago los más complejos luego

area = 7.23 #revisar, este dato no lo recuero y perdí el correo que me decía Aurelio, es en grados de arco

N_stars = list(map(lambda x: x/area, stars_list))
N_galaxies = list(map(lambda x: x/area, galaxies_list))

#xticks = np.arange(min(ks_mitad_intervalos),max(ks_mitad_intervalos),0.5 )

plt.figure()
plt.plot(ks_mitad_intervalos,np.log(N_stars), "*" ,label="Stars")
plt.plot(ks_mitad_intervalos,np.log(N_galaxies), "." ,label="Galaxies")
#plt.yscale("log")
plt.xlabel("Ks")
plt.ylabel(r"$log N ~ (objects/deg^2/ 0.5 mag)$")
#plt.ylim(0,10)
#plt.xlim(13.45,22.95)
plt.xticks(ks_mitad_intervalos)
plt.legend()
plt.savefig("Stars_galaxies_all_sharks.png")

wb = Workbook()
ruta = 'salida_ALL.xlsx'

hoja = wb.active
hoja.title = "ALL"

fila = 1 #Fila donde empezamos
col_stars = 1 #Columna donde guardo los valores
col_galaxies = 2

for stars, galaxies in zip(stars_list, galaxies_list):  #Aquí pongo en "in" el valor que quiero sacar como columna
    hoja.cell(column=col_stars, row=fila, value=stars)
    hoja.cell(column=col_galaxies, row=fila, value=galaxies)
    fila+=1

wb.save(filename = ruta)


#Con esto sacaría la tabla y grafica 1, ahora puedo calcular el total de galaxias usando la restriccion de considerar todo galaxias por encima del 21.2 mag

















    

