#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri 20 Nov 2020

@author: magnaldom
"""
##Tracer des champs pour AROME

import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
from datetime import datetime
from calcul_pression import calcul_pression_M_N_contour, calcul_pression_M_N_opt
from calcul_z import calcul_z
import matplotlib.pyplot as plt


#fichier = "netcdf_2020_08_02_ray"
def plot_AROME(i,j,date):

	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA_light/%s%s/AROME_%s%s%s_light.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	var = "SURFRAYT_SOLA_DE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	data = []
	time = []
	diff = 0
	data.append(0)
	time.append(datetime(annee,mois,jour,0,0,0))

	#print("test", arome1250m.variables[var][23,i,j])

	for e in range(1,24):
			Z = arome1250m.variables[var][e,i,j]
			data.append((Z-diff)/3600)

			#data.append(Z)
			time.append(datetime(annee,mois,jour,e,0,0))
			diff = Z
	arome1250m.close()

	return time, data

def plot_AROME_expe(i,j,date,expe):

	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/%s/%s%s/AROME_%s%s%s.nc" %(expe,str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	var = "SURFRAYT_SOLA_DE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	data = []
	time = []
	diff = 0
	data.append(0)
	time.append(datetime(annee,mois,jour,0,0,0))

	#print("test", arome1250m.variables[var][23,i,j])

	for e in range(1,24):
			Z = arome1250m.variables[var][e,i,j]
			data.append((Z-diff)/3600)

			#data.append(Z)
			time.append(datetime(annee,mois,jour,e,0,0))
			diff = Z
	arome1250m.close()

	return time, data

def plot_AROME_cumul(i,j,date):

	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA_light/%s%s/AROME_%s%s%s_light.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	var = "SURFRAYT_SOLA_DE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")


	Z = arome1250m.variables[var][23,i,j]
	data = Z

	#data.append(Z)
	arome1250m.close()

	return date, data

def plot_AROME_ins(i,j,date):
	fichier_albedo = Dataset("/cnrm/phynh/data1/magnaldom/AROME/albedo_AROME_aout.nc", 'r')
	albedo = fichier_albedo.variables['albedo'][:]
#	fichier_albedo =  Dataset("/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_ECRAD/albedo_0105.nc", 'r')
#	albedo = fichier_albedo.variables['albedo'][:]/100
	fichier_albedo.close()
	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	var = "SURFRAYT_SOLAIRE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	data = []
	time = []

	data.append(0)
	time.append(datetime(annee,mois,jour,0,0,0))
	#print(albedo[int(i),int(j)])


	for e in range(1,24):

		Z = arome1250m.variables[var][e,i,j]
		data.append(Z/(1-albedo[int(i),int(j)]))
		#data.append(Z/(1-albedo[int(j),int(i)]))
		time.append(datetime(annee,mois,jour,e,0,0))

	arome1250m.close()

	return time, data

def plot_AROME_cc(i,j,date):
	fichier_albedo = Dataset("/cnrm/phynh/data1/magnaldom/AROME/albedo_AROME_aout.nc", 'r')
	albedo = fichier_albedo.variables['albedo'][:]
	fichier_albedo.close()
	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	var = "S090RAYT_SOL_CL"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	data = []
	time = []

	data.append(0)
	time.append(datetime(annee,mois,jour,0,0,0))
	diff = 0

	#print("test", arome1250m.variables[var][23,i,j])

	for e in range(1,24):
			Z = arome1250m.variables[var][e,i,j]
			data.append(((Z-diff)/3600)/(1-albedo[i,j]))
			diff = Z

			#data.append(Z)
			time.append(datetime(annee,mois,jour,e,0,0))

	arome1250m.close()

	return time, data

def plot_AROME_var(i,j,date,var):

	#print(date)
	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	#var = "SURFRAYT_SOLA_DE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	data = []
	data.append(np.inf)
	time = []
	time.append(datetime(annee,mois,jour,0,0,0))


	#print("test", arome1250m.variables[var][23,i,j])

	for e in range(1,24):
			Z = arome1250m.variables[var][e,i,j]
			data.append(Z)
			time.append(datetime(annee,mois,jour,e,0,0))

	arome1250m.close()

	return time, data

def plot_AROME_var_expe(i,j,date,var,expe):

	#print(date)
	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/%s/%s%s/AROME_%s%s%s.nc" %(expe,str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	#var = "SURFRAYT_SOLA_DE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	data = []
	data.append(np.inf)
	time = []
	time.append(datetime(annee,mois,jour,0,0,0))


	#print("test", arome1250m.variables[var][23,i,j])

	for e in range(1,24):
			Z = arome1250m.variables[var][e,i,j]
			data.append(Z)
			time.append(datetime(annee,mois,jour,e,0,0))

	arome1250m.close()

	return time, data

def plot_AROME_var_cumul(i,j,date,var):

	#print(date)
	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA_light/%s%s/AROME_%s%s%s_light.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	#var = "SURFRAYT_SOLA_DE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	data = []
	data.append(np.inf)
	time = []
	time.append(datetime(annee,mois,jour,0,0,0))
	diff = 0


	#print("test", arome1250m.variables[var][23,i,j])

	for e in range(1,24):
			Z = arome1250m.variables[var][e,i,j]
			data.append((Z-diff)/3600)
			diff = Z
			time.append(datetime(annee,mois,jour,e,0,0))

	arome1250m.close()

	return time, data

def plot_AROME_var_cumul_expe(i,j,date,var,expe):

	#print(date)
	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/%s/%s%s/AROME_%s%s%s.nc" %(expe,str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	#var = "SURFRAYT_SOLA_DE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	data = []
	data.append(np.inf)
	time = []
	time.append(datetime(annee,mois,jour,0,0,0))
	diff = 0


	#print("test", arome1250m.variables[var][23,i,j])

	for e in range(1,24):
			Z = arome1250m.variables[var][e,i,j]
			data.append((Z-diff)/3600)
			diff = Z
			time.append(datetime(annee,mois,jour,e,0,0))

	arome1250m.close()

	return time, data

def plot_AROME_var_3D(i,j,t,date,var):

	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	#var = "SURFRAYT_SOLA_DE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")

	data = arome1250m.variables[var][t,i,j,:]

	arome1250m.close()

	return data

def plot_AROME_var_3D_expe(i,j,t,date,var,expe):

	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/%s/%s%s/AROME_%s%s%s.nc" %(expe,str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	#var = "SURFRAYT_SOLA_DE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")

	data = arome1250m.variables[var][t,i,j,:]

	arome1250m.close()

	return data

def plot_AROME_var_3D_contour(i,j,date,var):

	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	#var = "SURFRAYT_SOLA_DE"
	p = calcul_pression_M_N_contour(i,j,date)

	arome1250m = Dataset(fichier, "r", format="NETCDF4")

	data = arome1250m.variables[var][0:24,i,j,:]

	arome1250m.close()
	#print("verif",data[13])

	return data, p

def plot_AROME_var_3D_contour_expe(i,j,date,var,expe):

	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/%s/%s%s/AROME_%s%s%s.nc" %(expe,str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	#var = "SURFFLU_RAY_SOLA"
	#var = "SURFRAYT_SOLA_DE"
	p = calcul_pression_M_N_contour(i,j,date)

	arome1250m = Dataset(fichier, "r", format="NETCDF4")

	data = arome1250m.variables[var][0:24,i,j,:]

	arome1250m.close()
	#print("verif",data[13])

	return data, p

def altitude_nuage(i,j,date):

	data, p = plot_AROME_var_3D_contour(i,j,date,"CLOUD_FRACTI")
	alti = np.zeros(len(data))
	#print("ici",p[13])
	#print(data[13][:])
#	print(len(data))
#	print(len(data[0]))
	rho = 1.292
	p0 = 101325
	HS = plot_AROME_var_3D(i,j,1,date,"HUMI_SPECIFI")
	temp = plot_AROME_var_3D(i,j,1,date,"TEMPERATURE")
	for t in range(len(data)):
		check = 0

		z = np.zeros((len(p[t])))
#		for k in range(len(p[t])):
#			#print("ici")
#			z[k]=(-(p[t][k]-p0)/(rho*9.81))

		for l in range(0,90):

			#print(data[t][l])
			if data[t][l]>0.01 and check == 0:
				alti[t] = p[t][l]
				#alti[t] = z[l]
				check = 1
		if check==0:
			alti[t]=np.inf

	return alti

def altitude_nuage_opt(arome,i,j, h):

	var = "CLOUD_FRACTI"
	data = arome.variables[var][h,i,j,:]
	p = calcul_pression_M_N_opt(arome,h,i,j)

	for t in range(len(data)):
		check = 0
		for l in range(0,90):
			#print(data[t][l])
			if data[l]>0.01 and check == 0:
				alti = p[l]
				#alti[t] = z[l]
				check = 1
		if check==0:
			alti=np.inf

	return alti


def zone_M_N(i,j, date, t, K):

	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	var  = "SURFRAYT_SOLA_DE"

	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	diff = arome1250m.variables[var][t-1,i-K:i+K+1,j-K:j+K+1]
	Z = arome1250m.variables[var][t,i-K:i+K+1,j-K:j+K+1]
	Z = (Z-diff)/3600


	arome1250m.close()

	return Z

def zone_M_N_lon_lat(i,j, date, t, K):

	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA_light/%s%s/AROME_%s%s%s_light.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))

	var  = "SURFRAYT_SOLA_DE"
	i = int(i)
	j = int(j)

	arome1250m = Dataset(fichier, "r", format="NETCDF4")
	#print(t, K, i, j)
	diff = arome1250m.variables[var][t-1,i-K:i+K+1,j-K:j+K+1]
	Z = arome1250m.variables[var][t,i-K:i+K+1,j-K:j+K+1]
	lon = arome1250m.variables["Longitude"][i-K:i+K+1,j-K:j+K+1]
	lat= arome1250m.variables["Latitude"][i-K:i+K+1,j-K:j+K+1]
	Z = (Z-diff)/3600


	arome1250m.close()

	return Z, lon, lat

#Pareil que dessus mais optimiser pour l'ouverture du fichier netcdf
def zone_M_N_lon_lat_opt(arome,i,j, date, t, K):

	var  = "SURFRAYT_SOLA_DE"
	i = int(i)
	j = int(j)
	K = int(K)
	t = int(t)


	#print(t, K, i, j)
	diff = arome.variables[var][t-1,i-K:i+K+1,j-K:j+K+1]
	Z = arome.variables[var][t,i-K:i+K+1,j-K:j+K+1]
	lon = arome.variables["Longitude"][i-K:i+K+1,j-K:j+K+1]
	lat= arome.variables["Latitude"][i-K:i+K+1,j-K:j+K+1]
	Z = (Z-diff)/3600

	return Z, lon, lat

def zone_M_N_lon_lat_opt_assim(arome,i,j, date, t, K):

	var  = "SURFRAYT_SOLA_DE"
	i = int(i)
	j = int(j)


	#print(t, K, i, j)

	Z = arome.variables[var][t,i-K:i+K+1,j-K:j+K+1]
	lon = arome.variables["Longitude"][i-K:i+K+1,j-K:j+K+1]
	lat= arome.variables["Latitude"][i-K:i+K+1,j-K:j+K+1]
	Z = (Z)/3600

	return Z, lon, lat

def zone_M_N_lon_lat_var(arome,i,j, date, t, K, var):

	annee = date.year
	mois = date.month
	jour = date.day


	diff = arome.variables[var][t-1,i-K:i+K+1,j-K:j+K+1]
	Z = arome.variables[var][t,i-K:i+K+1,j-K:j+K+1]
	lon = arome.variables["Longitude"][i-K:i+K+1,j-K:j+K+1]
	lat= arome.variables["Latitude"][i-K:i+K+1,j-K:j+K+1]
	Z = (Z-diff)/3600



	return Z, lon, lat

def zone_M_N_3D_var(i,j, date, K, var):

	annee = date.year
	mois = date.month
	jour = date.day
	fichier = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))


	arome1250m = Dataset(fichier, "r", format="NETCDF4")

	Z = arome1250m.variables[var][0:24,i-K:i+K+1,j-K:j+K+1,:]



	arome1250m.close()

	return Z

def temperature_pression(i,j,t,date):
	fichier = "/cnrm/phynh/data1/magnaldom/AROME/A_B_AROME.nc"
	A_B = Dataset(fichier, "r", format="NETCDF4")
	A = A_B.variables["A"][:]
	B = A_B.variables["B"][:]
#	A = A[::-1]
#	B = B[::-1]
	A_B.close()

	nhlev = 91
	nlev = 90
	press_ref_half_level = np.zeros([nhlev])
	temp_ref_half_level = np.zeros([nhlev])
	press_ref_level= np.zeros([nlev])
	temp_ref_level = np.zeros([nlev])

	fichier_AROME = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/DATA/%s%s/AROME_%s%s%s.nc" %(str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))
	arome= Dataset(fichier_AROME, "r", format="NETCDF4")
	surfpression = arome.variables["SURFPRESSION"][t,i,j]
	ground_temp = arome.variables["SURFTEMPERATURE"][t,i,j]

	for alt in range(nlev):
		temp_ref_half_level[alt] = arome.variables["TEMPERATURE"][t,i,j,alt]
	#temp_ref_half_level = np.ma.getdata(temp_ref_half_level)

	#temp_ref_half_level[nlev] = ground_temp
	temp_ref_half_level[-1] = ground_temp
	ground_pressure = np.exp(surfpression)



	for niv in range(len(press_ref_half_level[:])):
		press_ref_half_level[niv] = A[niv] + B[niv] * ground_pressure
	for it in range(0,nlev):
		press_ref_level[it] = np.sqrt(press_ref_half_level[it]*press_ref_half_level[it+1])


	temp_ref_level[:] = np.interp(press_ref_level[:],press_ref_half_level[:],temp_ref_half_level[:])

	arome.close()

	return temp_ref_half_level, temp_ref_level, press_ref_half_level, press_ref_level

def temperature_pression_expe(i,j,t,date,expe):
	fichier = "/cnrm/phynh/data1/magnaldom/AROME/A_B_AROME.nc"
	A_B = Dataset(fichier, "r", format="NETCDF4")
	A = A_B.variables["A"][:]
	B = A_B.variables["B"][:]
#	A = A[::-1]
#	B = B[::-1]
	A_B.close()

	nhlev = 91
	nlev = 90
	press_ref_half_level = np.zeros([nhlev])
	temp_ref_half_level = np.zeros([nhlev])
	press_ref_level= np.zeros([nlev])
	temp_ref_level = np.zeros([nlev])

	fichier_AROME = "/cnrm/phynh/data1/magnaldom/STOCKAGE_AROME_UP/%s/%s%s/AROME_%s%s%s.nc" %(expe,str(date.year).zfill(4),str(date.month).zfill(2), str(date.year).zfill(4),str(date.month).zfill(2),str(date.day).zfill(2))
	arome= Dataset(fichier_AROME, "r", format="NETCDF4")
	surfpression = arome.variables["SURFPRESSION"][t,i,j]
	ground_temp = arome.variables["SURFTEMPERATURE"][t,i,j]

	for alt in range(nlev):
		temp_ref_half_level[alt] = arome.variables["TEMPERATURE"][t,i,j,alt]
	#temp_ref_half_level = np.ma.getdata(temp_ref_half_level)

	#temp_ref_half_level[nlev] = ground_temp
	temp_ref_half_level[-1] = ground_temp
	ground_pressure = np.exp(surfpression)



	for niv in range(len(press_ref_half_level[:])):
		press_ref_half_level[niv] = A[niv] + B[niv] * ground_pressure
	for it in range(0,nlev):
		press_ref_level[it] = np.sqrt(press_ref_half_level[it]*press_ref_half_level[it+1])


	temp_ref_level[:] = np.interp(press_ref_level[:],press_ref_half_level[:],temp_ref_half_level[:])

	arome.close()

	return temp_ref_half_level, temp_ref_level, press_ref_half_level, press_ref_level

#data =  plot_AROME_var_3D(600,600,5,datetime(2020,8,5),"HUMI_SPECIFI")
#print(data)