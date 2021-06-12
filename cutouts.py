# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 12:01:45 2021

@author: Sergi
"""

from astrocut import fits_cut

from astropy.io import fits

from astropy.coordinates import SkyCoord

input_files = [r"F:\TFG\Cutouts\Foto_sharks\sharks_er1_00h37-031d24_mosaic_ks_deepimage_1000000074475.fits", "F:\TFG\Cutouts\Foto_DES\DES0038-3040_r4907p01_r.fits", "F:\TFG\Cutouts\Foto_DES\DES0038-3040_r4907p01_Y.fits", "F:\TFG\Cutouts\Foto_DES\DES0038-3040_r4907p01_z.fits"]
#Aquí vendra una lista con las imágenes de DES en r,i,z y SHARKS en Ks, por ahora puedes probar solo con la imagen de SHARKS



center_coord = SkyCoord("9.286553400858 -30.98515841453", unit='deg')  #Aquí defino la coordenada del objeto, por ejemplo, en este caso, RA=9.213583 y Dec=-30.32642

cutout_size = [100,100]  #Tamaño de la imagen en píxeles, en este caso, creo que 100x100 es suficiente, pero podrás querer jugar con estos valores

cutout_file = fits_cut(input_files, center_coord, cutout_size,
drop_after="", single_outfile=False)   #Esto te generará un archivo fits por cada imagen en input_files.


#A continuación, abrirás el fits file creado en ds9 y modificarás la scale adecuadamente para que se vea mejor, y guardarás la imagen en png o jpg.