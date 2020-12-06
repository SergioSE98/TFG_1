# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:10:19 2020

@author: Sergio
"""

#Importo librerías a utilizar
    
import 	astropy as astropy

import pandas as pandas

import seaborn as seaborn


#Voy a leer el archivo fits

from astropy.table import Table
dat=Table.read("Sharks_sgp_e_2_cat_small.fits", format="fits")
df=dat.to_pandas()

#Asigno variables a las columnas que me interesa usar

ALPHA_J2000 = df["ALPHA_J2000"]
DELTA_J2000 = df["DELTA_J2000"]

#Ploteo la distribución de densidad de las fuentes contenidas en el archivo fits

seaborn.jointplot(ALPHA_J2000, DELTA_J2000, kind="hex")

#Ahora uso astropy para convertir las unidades espaciales de los parámetros ploteados a coordenadas galácticas

from astropy import units as u                 #Importo los módulos necesarios
from astropy.coordinates import SkyCoord

c = SkyCoord(ALPHA_J2000,DELTA_J2000, unit="deg")     #Con esto denoto las unidades de las que parto (grados)
ALPHA_J2000_galact= c.galactic.l                      #Ahora paso a unidades galacticas
DELTA_J2000_galact= c.galactic.b

seaborn.jointplot(ALPHA_J2000_galact, DELTA_J2000_galact, kind="hex")   #Vuelvo a plotear, ahora en uds galacticas

