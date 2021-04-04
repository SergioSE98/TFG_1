# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:00:47 2021

@author: Sergio
"""


import numpy as np

import astropy as astropy 

import pandas as pandas

import seaborn as seaborn

import matplotlib.pyplot as plt

from astropy.table import Table    #Ojo importante aquí importar "Table" con mayuscula

import smatch

#Leo datos (Objetos comunes de SHARKS y DES)
 

dat1=Table.read("fits/sharks_and_des_sig_noise_5_EROS_R_lite.fits", format="fits")  #EROS, objetos con R-Ks mayor a 5.5


mag_SHARKS = dat1["PETROMAG"]
mag_err_SHARKS = dat1["PETROMAGERR"]
mag_DES_I = dat1["MAG_AUTO_I_DERED"]
mag_DES_G = dat1["MAG_AUTO_G_DERED"]
mag_DES_R = dat1["MAG_AUTO_R_DERED"]

mag_y = mag_DES_R - mag_SHARKS

i1 = plt.figure("Magnitudes Sharks and DES objects (R detection) (s/n = 5)")
plt.title("Magnitudes Sharks and DES objects")
imag2 = plt.plot(mag_SHARKS,mag_y, ".")
plt.xlabel("PETROMAG_")
plt.ylabel("MAG_AUTO_R_DERED - PETROMAG_K")

i1.savefig('Mag_R-Mag_K_R_detect.png')   