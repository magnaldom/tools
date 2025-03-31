#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:22:16 2021

@author: magnaldom
"""
import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
from point_le_plus_proche import point_plus_proche
import h5py
import time

def num_station_glo():
	#On récupère les donnees, etc
	fichier_out = open('station_glo_v2', 'w')
	fichier_in = '/cnrm/phynh/data1/magnaldom/BDClim/BDClim_recup_station_test'
	datas = np.loadtxt(fichier_in, dtype = 'float', delimiter=' ', usecols=(1,2,3,4), unpack=True)
	num = np.loadtxt(fichier_in, dtype = 'str', delimiter=' ', usecols=(0), unpack=True)
	#num = datas[0]
	lon = datas[0]
	lat = datas[1]
	alti = datas[2]
	classe = datas[3]

	#On importe ce qu'il faut pour calculer les points les plus proches AROME
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/202008/AROME_20200801.nc"
	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	LON_a = arome1250m.variables["Longitude"][:]
	LAT_a = arome1250m.variables["Latitude"][:]

 	#On importe ce qu'il faut pour calculer les points les plus proches CEMS
	fi_latlon= h5py.File("/cnrm/phynh/data1/magnaldom/CEMS/latlon_+000.0.h5",'r')
	latt = fi_latlon['latitudes']
	lont = fi_latlon['longitudes']
	nlat = len(latt)
	nlon = len(lont[0,:])
	#print(nlon,nlat)
	LAT_c = np.zeros((nlat,nlon))
	LON_c = np.zeros((nlat,nlon))
	for i in range(nlat):
		for j in range(nlon):
			LAT_c[i,j] = latt[i,j]
			LON_c[i,j] = lont[i,j]
	#print(LAT_c[255:616,1610:2200])
	#Boucle sur les stations
	for i in range(0,len(num)):
		M_a, N_a, lon_v, lat_v = point_plus_proche(LON_a, LAT_a, lon[i], lat[i])
		M_c, N_c, lon_vc, lat_vc = point_plus_proche(LON_c[255:616,1610:2200], LAT_c[255:616,1610:2200], lon[i], lat[i])
		print("Mc", M_c, "Nc", N_c)
		fichier_out.write(num[i]+' ' + str(lon[i]) +' ' + str(lat[i]) + ' ' + str(alti[i]) + ' ' + str(classe[i]) +' ' + str(M_a) + ' ' + str(N_a) +' ' + str(M_c+255) + ' ' + str(N_c+1610) + '\n')
	fichier_out.close()


def AROME():

	#On importe ce qu'il faut pour calculer les points les plus proches AROME
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA_light/202008/AROME_20200801_light.nc"
	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	LON_a = arome1250m.variables["Longitude"][:]
	LAT_a = arome1250m.variables["Latitude"][:]
	

	lat = 48.71
	lon = 2.2

	M_a, N_a, lon_v, lat_v = point_plus_proche(LON_a, LAT_a, lon, lat)

	print("Mc", M_a, "Nc", N_a)


AROME()
