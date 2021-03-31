# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:45:29 2021

@author: Sergio
"""

import numpy as np

import astropy as astropy 

import pandas as pandas

import seaborn as seaborn

import matplotlib.pyplot as plt

from astropy.table import Table    #Ojo importante aquí importar "Table" con mayuscula

import smatch

#Leo datos (SHARKS NOT DES)

dat1=Table.read("sharks_only_not_des_nodifrac_sig_noise_3_lite.fits", format="fits")   

DEC = dat1["DEC"]
RA = dat1["RA"]
mag = dat1["PETROMAG"]
mag_err = dat1["PETROMAGERR"]


#Grafico las distintas imágenes de interés
"""
i1 = seaborn.jointplot(RA, DEC, kind="hex")
i1.fig.suptitle("Density distribution of objects in SHARKS and not in DES", fontsize=11)
i1.savefig('Density_distrib_SHARKS_not_DES.png')   
"""

i2 = plt.figure("(RA,DEC) of objects in SHARKS and not in DES")
plt.title("(RA,DEC) of objects in SHARKS and not in DES")
imag2 = plt.plot(RA,DEC, ",")
plt.xlabel("RA")
plt.ylabel("DEC")
i2.savefig('RA_DEC_SHARKS_not_DES.png')   


i3= plt.figure("Petromag histogram")
plt.title("Petromag histogram of objects in SHARKS and not in DES")
imag3 = seaborn.distplot(mag,kde=False,norm_hist=False)    
plt.ylabel("Photon counts")
i3.savefig('petromag_hist_SHARKS_not_DES.png')   

i4= plt.figure("Petromag-Petromagerr")
plt.title("Petromag - Petromagerr of objects in SHARKS and not in DES")
imag4 = plt.plot(mag,mag_err,".")
plt.xlabel("Petromag")
plt.ylabel("Petromagerr")
plt.yscale('log')
#plt.ylim(0,1)
i4.savefig('petromag_petromagerr_SHARKS_not_DES.png')   
