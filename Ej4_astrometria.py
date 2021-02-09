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

#Voy a leer el archivo fits

dat1=Table.read("Sharks_sgp_e_2_cat_small.fits", format="fits")
df1=dat1.to_pandas()

#dat2=Table.read("GAIA_2018.fit", format="fits")
#df2=dat2.to_pandas()

dat2=Table.read("2mass.fit", format="fits")
df2=dat2.to_pandas()


dec1 = df1["DELTA_J2000"]
ra1 = df1["ALPHA_J2000"]

dec2 = df2["DEJ2000"]
ra2 = df2["RAJ2000"]

rad=0.000277778   #Un segundo sexagesimal (segundo de arco en grados, las unidades en que se expresan ra1...)
nside=4096 # healpix nside
maxmatch=1 # return closest match

matches = smatch.match(ra1, dec1, rad, ra2, dec2, nside=nside, maxmatch=maxmatch)

ra1matched  = ra1[ matches['i1'] ]
dec1matched = dec1[ matches['i1'] ]
ra2matched  = ra2[ matches['i2'] ]
dec2matched = dec2[ matches['i2'] ]

print(ra1matched)
print(dec1matched)
print(ra2matched)
print(dec2matched)
print(matches)