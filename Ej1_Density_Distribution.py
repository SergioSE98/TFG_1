# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:03:51 2021

@author: Sergio
"""

#Importo librerías a utilizar
import 	astropy as astropy

import pandas as pandas

import seaborn as seaborn

import matplotlib.pyplot as plt

import matplotlib.image as mpimg

from astropy.table import Table                        #Esto lo uso para leer la tabla de datos
from astropy import units as u                         #Estos dos los uso para cambiar de coordenadas espaciales a galácticas
from astropy.coordinates import SkyCoord


#Voy a leer el archivo fits
dat=Table.read("fits/sharks_sgpe.fits", format="fits")
df=dat.to_pandas()

#Asigno variables a las columnas que me interesa usar
RA = df["RA"]
DEC = df["DEC"]
L = df["L"]
B = df["B"]
#Ploteo la distribución de densidad de las fuentes contenidas en el archivo fits (añado título y nombre a ejes)
imagen1 = seaborn.jointplot(RA, DEC, kind="hex")
imagen1.fig.suptitle("Density distribution (ALPHA_J2000, DELTA_J2000) in spacial coordinates", fontsize=11)
imagen1.set_axis_labels('ALPHA_J2000 (Right ascension)', 'DELTA_J2000 (Declination)', fontsize=11)



#Ahora uso astropy para convertir las unidades espaciales de los parámetros ploteados a coordenadas galácticas
c = SkyCoord(RA, DEC, unit="deg")     #Con esto denoto las unidades de las que parto (grados)
RA_galact= c.galactic.l                      #Ahora paso a unidades galacticas
DEC_galact= c.galactic.b
"""
#Ploteo ahora la distribución en coordenadas galácticas (con su correspondiente título y nombre de ejes)
imagen2 = seaborn.jointplot(RA_galact, DEC_galact, kind="hex" )   #Vuelvo a plotear, ahora en uds galacticas
imagen2.fig.suptitle("Density distribution (L,B) in galactic coordinates", fontsize=11)
imagen2.set_axis_labels('L (Right ascension)', 'B (Declination)', fontsize=11)
"""
#Ploteo ahora la distribución en coordenadas galácticas (con su correspondiente título y nombre de ejes)
imagen3 = seaborn.jointplot(L,B, kind="hex" )   #Vuelvo a plotear, ahora en uds galacticas
imagen3.fig.suptitle("Density distribution (L,B) in galactic coordinates", fontsize=11)
imagen3.set_axis_labels('L (Right ascension)', 'B (Declination)', fontsize=11)


#Guardo ahora las imagenes con las distintas representaciones del paralaje
imagen1.savefig('ej1_sharks_sgpe_distribution_in_spacial_coords.png')  
#plt.close(imagen1.fig)  Esto podría activarlo si solo quisiera mostrar la imágen con ambas representaciones a la vez.
"""
imagen2.savefig('Density distribution (L,B) in galactic coordinates.png')
#plt.close(imagen2.fig)
"""
imagen3.savefig("ej1_sharks_sgpe_distribution_in_galactic_coords.png")

#A continuación creo una figura con dos subplots, y en cada uno de ellos añadiré las dos imágenes antes obtenidas
f, axarr = plt.subplots(1,2)
axarr[0].imshow(mpimg.imread('Density distribution (ALPHA_J2000, DELTA_J2000) in spacial coordinates.png'))
axarr[1].imshow(mpimg.imread('Density distribution (L,B) in galactic coordinates.png'))

# turn off x and y axis, lo uso para quitar los ejes que el propio subplot introduce.
[ax.set_axis_off() for ax in axarr.ravel()]



#Por último guardo la figura que contiene ambas distribuciones de densidad
f.savefig("ej1_sharks_sgpe_distribution_in_both_coords.png")
plt.show()
plt.tight_layout()