# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:35:31 2021

@author: Sergio
"""


import numpy as np

import astropy as astropy 

import pandas as pandas

import seaborn as seaborn

import matplotlib.pyplot as plt

from astropy.table import Table    #Ojo importante aquí importar "Table" con mayuscula

import smatch


#Empiezo haciendo matching de los puntos captados en SHARKS y VIKING

dat1=Table.read("sharks_sgpe.fits", format="fits")
dat2=Table.read("viking_ks.fit", format="fits")   

dec1 = dat1["DEC"]
ra1 = dat1["RA"]
mag1 = dat1["APERMAG3"]
err_mag1 = dat1["APERMAG3ERR"]


dec2 = dat2["DEJ2000"]
ra2 = dat2["RAJ2000"]
mag2 = dat2["Kspmag"]   #Kspmag es petrosian magnitude. También: Ksap3, Ksap4, Ksap6 (fuentes puntuales) y Ksapc3, Ksapc4, Ksap6...
err_mag2 = dat2["e_Kspmag"]

rad=0.000277778   #Un segundo sexagesimal (segundo de arco en grados, las unidades en que se expresan ra1...)
nside=4096 # healpix nside
maxmatch=1 # return closest match 

#Uso la función match para hacer el matching de los catálogos, llamando a las funciones antes definidas. 
matches_viking = smatch.match(ra1, dec1, rad, ra2, dec2, nside=nside, maxmatch=maxmatch)  #Matching SHARKS-VIKING

MAG_SHARKS  = mag1[matches_viking['i1']]
MAG_VIKING = mag2[matches_viking['i2']]
ERROR_MAG_SHARKS = err_mag1[matches_viking["i1"]]
ERROR_MAG_VIKING = err_mag2[matches_viking["i2"]]




#Creo mask para evitar valores nulos
mask = (MAG_SHARKS>0)&(MAG_SHARKS<30)&(MAG_VIKING>0)&(MAG_VIKING<30)&(ERROR_MAG_SHARKS<0.3)&(ERROR_MAG_VIKING<0.3)

#MAGNITUDES "NEW" obtenidas una vez pasada la mask
MAG_SHARKS_NEW = MAG_SHARKS[mask]
MAG_VIKING_NEW = MAG_VIKING[mask]
ERROR_MAG_SHARKS_NEW = ERROR_MAG_SHARKS[mask]
ERROR_MAG_VIKING_NEW = ERROR_MAG_VIKING[mask]

#print(MAG_SHARKS_NEW)
#print(MAG_VIKING_NEW)

dif=MAG_VIKING_NEW-MAG_SHARKS_NEW


#Figura 1 (Viking eje x, sharks eje y)
image1 = plt.figure("Photometry for SHARKS-VIKING")
plt.title("Photometry for SHARKS-VIKING")
plt.plot([10,24],[10,24])
plt.plot(MAG_VIKING_NEW,MAG_SHARKS_NEW,"r,", label="SHARKS magnitude not corrected")
ajuste=np.polyfit(MAG_VIKING_NEW,dif,0)
#print(ajuste)
#print(ajuste[1])
MAG_SHARKS_corrected= MAG_SHARKS_NEW+ajuste[0]
plt.plot(MAG_VIKING_NEW,MAG_SHARKS_corrected, "g,", label ="SHARKS magnitude corrected")
plt.xlabel("VIKING magnitude")
plt.ylabel("SHARKS magnitude")
plt.legend()



#Figura 2 Repito el proceso de la figura 2 considerando errores 
xerr_=ERROR_MAG_SHARKS_NEW
yerr_=ERROR_MAG_VIKING_NEW
#Calculo el error total con la media aritmética de los errores de ambos surveys
err_total= np.sqrt(xerr_**2 + yerr_**2)
peso=1/err_total

image2 = plt.figure("Photometry for SHARKS-VIKING with error bars")
plt.title("Photometry for SHARKS-VIKING with error bars")
plt.plot([10,24],[10,24])
plt.errorbar(MAG_VIKING_NEW, MAG_SHARKS_NEW, xerr=xerr_, yerr=yerr_,fmt="r,", label="SHARKS magnitude not corrected")
ajuste_err = np.polyfit(MAG_VIKING_NEW,dif,0,w=peso)
#print(ajuste_err)
MAG_SHARKS_corrected_errors = MAG_SHARKS_NEW+ajuste_err[0]
plt.errorbar(MAG_VIKING_NEW, MAG_SHARKS_corrected_errors, xerr=xerr_, yerr=yerr_,fmt="g,", label ="SHARKS magnitude corrected")
plt.xlabel("VIKING magnitude")
plt.ylabel("SHARKS magnitude")
plt.legend()



#Guardo las figuras
image1.savefig('Photometry for SHARKS-VIKING.png')
image2.savefig('Photometry for SHARKS-VIKING with error bars.png')   

