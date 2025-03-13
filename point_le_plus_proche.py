
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 12 11:29:31 2021

@author: Adèle
"""


##Programme qui renvoie les indices des mailles de MNH ou AROME les plus proches de la position des sites

#Importations
import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
import datetime as dt
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree


def point_plus_proche(LON, LAT, lon, lat):
	coord = list(zip(LAT.flatten(),LON.flatten()))
	tree = cKDTree(coord)
	d, i = tree.query((lat,lon), k = 1)
	nlon = len(LON[0,:])
	nlat = len(LAT)
	i_lat = i//nlon
	i_lon = i%nlon
	return i_lat, i_lon, LAT[i_lat,i_lon], LON[i_lat,i_lon]





