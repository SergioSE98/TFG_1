# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 00:29:05 2021

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

dat1=Table.read("sharks_and_des_lite.fits", format="fits")


mag_SHARKS = dat1["PETROMAG"]
mag_err_SHARKS = dat1["PETROMAGERR"]
mag_DES_I = dat1["MAG_AUTO_I_DERED"]
mag_DES_G = dat1["MAG_AUTO_G_DERED"]

mag_x = mag_DES_I - mag_SHARKS
mag_y = mag_DES_G - mag_DES_I

i1 = plt.figure("Magnitudes Sharks and DES objects")
plt.title("Magnitudes Sharks and DES objects")
imag2 = plt.plot(mag_x,mag_y, ",")
plt.xlabel("MAG_AUTO_I_DERED - PETROMAG")
plt.ylabel("MAG_AUTO_G_DERED - MAG_AUTO_I_DERED")
plt.xlim(-5,10)
plt.ylim(-5,15)
i1.savefig('MAG_SHARKS_AND_DES.png')   
