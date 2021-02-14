# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:45:44 2021

@author: Sergio
"""

import numpy as np

import astropy as astropy 

import pandas as pandas

import seaborn as seaborn

import matplotlib.pyplot as plt

from astropy.table import Table    #Ojo importante aquí importar "Table" con mayuscula

import smatch

#Leo los tres catálogos que voy a comparar.

dat1=Table.read("Sharks_sgp_e_2_cat_small.fits", format="fits")
df1=dat1.to_pandas()

dat2=Table.read("2mass.fit", format="fits")
df2=dat2.to_pandas()

dat3=Table.read("GAIA_2018_lite.fit", format="fits")
df3=dat3.to_pandas()

#Nombro las variables que voy a usar para hacer matching (declinación y ascención recta).

dec1 = df1["DELTA_J2000"]
ra1 = df1["ALPHA_J2000"]

dec2 = df2["DEJ2000"]
ra2 = df2["RAJ2000"]

dec3 = df3["DE_ICRS"]
ra3 =  df3["RA_ICRS"]

#Nombro las variables que uso en la función "match".

rad=0.000277778   #Un segundo sexagesimal (segundo de arco en grados, las unidades en que se expresan ra1...)
nside=4096 # healpix nside
maxmatch=1 # return closest match 

#Uso la función match para hacer el matching de los catálogos, llamando a las funciones antes definidas. 

matches_2mass = smatch.match(ra1, dec1, rad, ra2, dec2, nside=nside, maxmatch=maxmatch)  #Matching SHARKS-2MASS
matches_gaia = smatch.match(ra1, dec1, rad, ra3, dec3, nside=nside, maxmatch=maxmatch)   #Matching SHARKS-GAIA


#Imprimo las tablas con los valores de ascención recta y declinación que han hecho match:
    
"""
#Quitando estre entrecomillado se imprimen los matches (redondea el coseno de la distancia angular a uno, por eso lo calculo usando un loop)

print("\n Matches SHARKS-2MASS: ")
print(matches_2mass)
print("\n Matches SHARKS-GAIA: ")
print(matches_gaia)
"""

#Puedo adicionalmente imprimir las columnas por separado para ver más claro qué valores de ascención recta y declinación han hecho match entre los catálogos.
#(Esto último se puede comentar para sacar solo las tablas completas y no generar las columnas por separado.)


#Columnas de RA y DEC que hacen match entre SHARKS y 2MASS:

ra1matched_2mass  = ra1[ matches_2mass['i1'] ]
dec1matched_2mass = dec1[ matches_2mass['i1'] ]
ra2matched_2mass  = ra2[ matches_2mass['i2'] ]
dec2matched_2mass = dec2[ matches_2mass['i2'] ]

"""
#Quitando este entrecomillado se imprimen los valores de RA y DEC que hacen match.

print("\nSHARKS RA matched with 2MASS")
print(ra1matched_2mass)
print("\nSHARKS DEC matched with 2MASS")
print(dec1matched_2mass)
print("\n2MASS RA matched with SHARKS")
print(ra2matched_2mass)
print("\n2MASS DEC matched with SHARKS")
print(dec2matched_2mass)
"""

#Columnas de RA y DEC que hacen match entre SHARKS y GAIA:

ra1matched_gaia  = ra1[ matches_gaia['i1'] ]
dec1matched_gaia = dec1[ matches_gaia['i1'] ]
ra3matched_gaia  = ra3[ matches_gaia['i2'] ]
dec3matched_gaia = dec3[ matches_gaia['i2'] ]

"""
#Quitando este entrecomillado se imprimen los valores de RA y DEC que hacen match.

print("\nSHARKS RA matched with GAIA")
print(ra1matched_gaia)
print("\nSHARKS RA matched with GAIA")
print(dec1matched_gaia)
print("\nGAIA RA matched with SHARKS")
print(ra3matched_gaia)
print("\nGAIA DEC matched with SHARKS")
print(dec3matched_gaia)
"""

#Utilizo loops para calcular las diferencias entre los valores de RA y DEC que hacen matching, así comola distancia angular entre los puntos (gamma)

#SHARKS-2MASS.

#Diferencia entre valores de RA de SHARKS y 2MASS que hacen match (en valor absoluto)

dif_ra_2mass=[]
for r1,r2 in zip(ra1matched_2mass,ra2matched_2mass):
    #print(r1,r2)
    dif_ra_2mass.append(np.abs((r1-r2)*3600))  #multi por 3600 para pasar a grados
    
#print(dif_ra_2mass)
#print(np.mean(dif_ra_2mass))
#print(np.std(dif_ra_2mass))

#Diferencia entre valores de DEC de SHARKS y 2MASS que hacen match

dif_dec_2mass=[]
for d1,d2 in zip(dec1matched_2mass,dec2matched_2mass):
    #print(r1,r2)
    dif_dec_2mass.append(np.abs((d1-d2)*3600))  
    
#print(dif_dec_2mass)
#print(np.mean(dif_dec_2mass))
#print(np.std(dif_dec_2mass))


#Distancia angular entre puntos que hacen match entre SHARKS y 2MASS

gamma_2mass=[]
for r1,r2,d1,d2 in zip(ra1matched_2mass, ra2matched_2mass, dec1matched_2mass, dec2matched_2mass):
    gamma_2mass.append(np.arccos(np.cos(90-d1)*np.cos(90-d2)+np.sin(90-d1)*np.sin(90-d2)*np.cos(r1-r2))*3600)  #Esta formula en bibliografía
    
#print(gamma_2mass)
print("El valor medio de la distancia angular para SHARKS-2MASS es: %f" %np.mean(gamma_2mass))
print("La desviación estándar de la distancia angular para SHARKS-2MASS es: %f"  %np.std(gamma_2mass))

image1 = plt.figure("Photometry histogramas SHARKS-2MASS")
plt.title("SHARKS-2MASS matched point sources histogram")
seaborn.distplot(dif_ra_2mass,bins=60, label= "Absolute value of RA diferences between matched point sources")
seaborn.distplot(dif_dec_2mass,bins=60, label= "Absolute value of DEC diferences between matched point sources")
seaborn.distplot(gamma_2mass,bins=60, label= "Angular distance between matched point sources") 
plt.legend()
plt.xlabel("Seconds of arc")
plt.tight_layout()
plt.show()


#Procedo ahora exactamente igual a como hice con SHARKS-2MASS para obtener los valores de distancia angular entre matches.

#SHARKS-GAIA

dif_ra_gaia=[]
for r1,r3 in zip(ra1matched_gaia,ra3matched_gaia):
    #print(r1,r2)
    dif_ra_gaia.append(np.abs((r1-r3)*3600))
#print(dif_ra_2mass)
#print(np.mean(dif_ra_2mass))
#print(np.std(dif_ra_2mass))

dif_dec_gaia=[]
for d1,d3 in zip(dec1matched_gaia,dec3matched_gaia):
    #print(r1,r2)
    dif_dec_gaia.append(np.abs((d1-d3)*3600))
#print(dif_dec_2mass)
#print(np.mean(dif_dec_2mass))
#print(np.std(dif_dec_2mass))


#Distancia angular entre puntos que hacen match entre SHARKS y 2MASS

gamma_gaia=[]

for r1,r3,d1,d3 in zip(ra1matched_gaia, ra3matched_gaia, dec1matched_gaia, dec3matched_gaia):
    gamma_gaia.append(np.arccos(np.cos(90-d1)*np.cos(90-d3)+np.sin(90-d1)*np.sin(90-d3)*np.cos(r1-r3))*3600)
    
    
#print(gamma_gaia)
print("El valor medio de la distancia angular para SHARKS-GAIA es: %f" %np.mean(gamma_gaia))
print("La desviación estándar de la distancia angular para SHARKS-GAIA es: %f" %np.std(gamma_gaia))


image2 = plt.figure("Photometry histogramas SHARKS-GAIA")
plt.title("SHARKS-GAIA matched point sources histogram")
seaborn.distplot(dif_ra_gaia,bins=60, label= "Absolute value of RA diferences between matched point sources")
seaborn.distplot(dif_dec_gaia,bins=60, label= "Absolute value of DEC diferences between matched point sources")
seaborn.distplot(gamma_gaia,bins=60, label= "Angular distance between matched point sources") 
plt.legend()
plt.xlabel("Seconds of arc")
plt.tight_layout()
plt.show()


#Por último creo una última figura donde mostrar las distancias angulares obtenidas tanto en SHARKS-2MASS como en SHARKS-GAIA.


image3 = plt.figure("Angular distances between matched point sources for SHARKS-2MASS and SHARKS-GAIA")
plt.title("Angular distances between matched point sources for SHARKS-2MASS and SHARKS-GAIA")
seaborn.distplot(gamma_2mass,bins=60, label= "Angular distance between matched point sources for SHARKS-2MASS") 
seaborn.distplot(gamma_gaia,bins=60, label= "Angular distance between matched point sources for SHARKS-GAIA") 
plt.legend()
plt.xlabel("Seconds of arc")
plt.tight_layout()
plt.show()


image1.savefig('Photometry histograms SHARKS-2MASS.png')
image2.savefig('Photometry histograms SHARKS-GAIA.png')   
image3.savefig("Angular distances between matched point sources for SHARKS-2MASS and SHARKS-GAIA.png")