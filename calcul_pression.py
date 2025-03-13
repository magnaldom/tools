#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:40:04 2021

@author: magnaldom
"""

import netCDF4 as nc
from netCDF4 import Dataset
import numpy as np
from datetime import datetime


def calcul_pression(date):
	t = date.hour
	fichier = "/cnrm/phynh/data1/magnaldom/AROME/A_B_AROME.nc"
	A_B = Dataset(fichier, "r", format="NETCDF4")
	A = A_B.variables["A"][:]
	B = A_B.variables["B"][:]
	A = A[::-1]
	B = B[::-1]
	A_B.close()

	fichier_AROME = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))
	arome= Dataset(fichier_AROME, "r", format="NETCDF4")
	surfpression = arome.variables["SURFPRESSION"][t,:]
	arome.close()

	ground_pressure = np.exp(surfpression)

	nhlev = 91
	nlev = 90
	nlat = 1429
	nlon = 1525
	press_ref_half_level = np.zeros([nlat,nlon,nhlev])
	press_ref_level= np.zeros([nlat,nlon,nlev])

	for N in range(len(press_ref_half_level[0,:,0])):
		for M in range(len(press_ref_half_level[:,0,0])):
			for niv in range(len(press_ref_half_level[0,0,:])):
				press_ref_half_level[M,N,niv] = A[niv] + B[niv] * ground_pressure[M,N]
	for it in range(0,nlev):
		press_ref_level[:,:,it] = np.sqrt(press_ref_half_level[:,:,it]*press_ref_half_level[:,:,it+1])

	return press_ref_level

def calcul_pression_up(A, B, surfpression):

	ground_pressure = np.exp(surfpression)

	nhlev = 91
#	nlev = 90
	nlat = 1429
	nlon = 1525
	press_ref_half_level = np.zeros([nlat,nlon,nhlev])
	#press_ref_level= np.zeros([nlat,nlon,nlev])

	ground_pressure = np.repeat(ground_pressure[..., np.newaxis], 91, axis=-1)
#	A = A[::-1]
#	B = B[::-1]
	A = np.repeat(A[np.newaxis, ... ], nlon, axis=0)
	A = np.repeat(A[np.newaxis, ... ], nlat, axis=0)
	B = np.repeat(B[np.newaxis, ... ], nlon, axis=0)
	B = np.repeat(B[np.newaxis, ... ], nlat, axis=0)
	#print(np.shape(A), np.shape(ground_pressure))


	press_ref_half_level[:] = A[:] + (B[:] *  ground_pressure[:])
#	for it in range(0,nlev):
#		press_ref_level[:,:,it] = np.sqrt(press_ref_half_level[:,:,it]*press_ref_half_level[:,:,it+1])

	return press_ref_half_level

def calcul_pression_M_N_up(A, B, surfpression,M,N):

	ground_pressure = np.exp(surfpression)

	nhlev = 91
#	nlev = 90
	press_ref_half_level = np.zeros([nhlev])
	#press_ref_level= np.zeros([nlat,nlon,nlev])

	press_ref_half_level[:] = A[:] + (B[:] *  ground_pressure)
#	for it in range(0,nlev):
#		press_ref_level[:,:,it] = np.sqrt(press_ref_half_level[:,:,it]*press_ref_half_level[:,:,it+1])

	return press_ref_half_level

def calcul_pression_M_N(M,N,date):
	t = date.hour
	fichier = "/cnrm/phynh/data1/magnaldom/AROME/A_B_AROME.nc"
	A_B = Dataset(fichier, "r", format="NETCDF4")
	A = A_B.variables["A"][:]
	B = A_B.variables["B"][:]
#	A = A[::-1]
#	B = B[::-1]
	A_B.close()

	fichier_AROME = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))
	arome= Dataset(fichier_AROME, "r", format="NETCDF4")
	surfpression = arome.variables["SURFPRESSION"][t,M,N]
	arome.close()

	ground_pressure = np.exp(surfpression)
#	print(ground_pressure)

	nhlev = 91
	nlev = 90
	press_ref_half_level = np.zeros([nhlev])
	press_ref_level= np.zeros([nlev])


	for niv in range(len(press_ref_half_level[:])):
		press_ref_half_level[niv] = A[niv] + B[niv] * ground_pressure
	for it in range(0,nlev):
		press_ref_level[it] = np.sqrt(press_ref_half_level[it]*press_ref_half_level[it+1])

	return press_ref_level

def calcul_pression_M_N_opt(arome,h,M,N):
	t = h
	fichier = "/cnrm/phynh/data1/magnaldom/AROME/A_B_AROME.nc"
	A_B = Dataset(fichier, "r", format="NETCDF4")
	A = A_B.variables["A"][:]
	B = A_B.variables["B"][:]
#	A = A[::-1]
#	B = B[::-1]
	A_B.close()

	surfpression = arome.variables["SURFPRESSION"][t,M,N]


	ground_pressure = np.exp(surfpression)
#	print(ground_pressure)

	nhlev = 91
	nlev = 90
	press_ref_half_level = np.zeros([nhlev])
	press_ref_level= np.zeros([nlev])


	for niv in range(len(press_ref_half_level[:])):
		press_ref_half_level[niv] = A[niv] + B[niv] * ground_pressure
	for it in range(0,nlev):
		press_ref_level[it] = np.sqrt(press_ref_half_level[it]*press_ref_half_level[it+1])

	return press_ref_level

def calcul_pression_M_N_contour(M,N,date):

	fichier = "/cnrm/phynh/data1/magnaldom/AROME/A_B_AROME.nc"
	A_B = Dataset(fichier, "r", format="NETCDF4")
	A = A_B.variables["A"][:]
	B = A_B.variables["B"][:]
#	A = A[::-1]
#	B = B[::-1]
	A_B.close()

	fichier_AROME = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))
	arome= Dataset(fichier_AROME, "r", format="NETCDF4")
	surfpression = arome.variables["SURFPRESSION"][:,M,N]
	L = len(surfpression[:])
	arome.close()

	ground_pressure = np.exp(surfpression)
#	print(ground_pressure)

	nhlev = 91
	nlev = 90
	press_ref_half_level = np.zeros([L,nhlev])
	press_ref_level= np.zeros([L,nlev])

	for t in range(L):
		for niv in range(len(press_ref_half_level[t,:])):
			press_ref_half_level[t,niv] = A[niv] + B[niv] * ground_pressure[t]
		for it in range(0,nlev):
			press_ref_level[t,it] = np.sqrt(press_ref_half_level[t,it]*press_ref_half_level[t,it+1])

	return press_ref_level

def calcul_pression_M_N_hl(M,N,date):
	t = date.hour
	fichier = "/cnrm/phynh/data1/magnaldom/AROME/A_B_AROME.nc"
	A_B = Dataset(fichier, "r", format="NETCDF4")
	A = A_B.variables["A"][:]
	B = A_B.variables["B"][:]
#	A = A[::-1]
#	B = B[::-1]
	A_B.close()

	fichier_AROME = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))
	arome= Dataset(fichier_AROME, "r", format="NETCDF4")
	surfpression = arome.variables["SURFPRESSION"][t,M,N]
	arome.close()

	ground_pressure = np.exp(surfpression)
	#print("gp", ground_pressure)
#	print(ground_pressure)

	nhlev = 91
	nlev = 90
	press_ref_half_level = np.zeros([nhlev])
	press_ref_level= np.zeros([nlev])


	for niv in range(len(press_ref_half_level[:])):
		press_ref_half_level[niv] = A[niv] + B[niv] * ground_pressure
	for it in range(0,nlev):
		press_ref_level[it] = np.sqrt(press_ref_half_level[it]*press_ref_half_level[it+1])

	return press_ref_half_level

#print(calcul_pression_M_N(700,800,datetime(2020,8,5,12)))
