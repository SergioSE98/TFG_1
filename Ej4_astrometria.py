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

print("\n Matches SHARKS-2MASS: ")
print(matches_2mass)
print("\n Matches SHARKS-GAIA: ")
print(matches_gaia)


#Puedo adicionalmente imprimir las columnas por separado para ver más claro qué valores de ascención recta y declinación han hecho match entre los catálogos.
#(Esto último se puede comentar para sacar solo las tablas completas y no generar las columnas por separado.)


#Columnas de RA y DEC que hacen match entre SHARKS y 2MASS:

ra1matched_2mass  = ra1[ matches_2mass['i1'] ]
dec1matched_2mass = dec1[ matches_2mass['i1'] ]
ra2matched_2mass  = ra2[ matches_2mass['i2'] ]
dec2matched_2mass = dec2[ matches_2mass['i2'] ]

print("\nSHARKS RA matched with 2MASS")
print(ra1matched_2mass)
print("\nSHARKS DEC matched with 2MASS")
print(dec1matched_2mass)
print("\n2MASS RA matched with SHARKS")
print(ra2matched_2mass)
print("\n2MASS DEC matched with SHARKS")
print(dec2matched_2mass)


#Columnas de RA y DEC que hacen match entre SHARKS y GAIA:

ra1matched_gaia  = ra1[ matches_gaia['i1'] ]
dec1matched_gaia = dec1[ matches_gaia['i1'] ]
ra3matched_gaia  = ra3[ matches_gaia['i2'] ]
dec3matched_gaia = dec3[ matches_gaia['i2'] ]

print("\nSHARKS RA matched with GAIA")
print(ra1matched_gaia)
print("\nSHARKS RA matched with GAIA")
print(dec1matched_gaia)
print("\nGAIA RA matched with SHARKS")
print(ra3matched_gaia)
print("\nGAIA DEC matched with SHARKS")
print(dec3matched_gaia)


