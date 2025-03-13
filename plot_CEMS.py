#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:29:39 2021

@author: magnaldom
"""

import cProfile
import pstats
import netCDF4 as nc
from netCDF4 import Dataset
from datetime import datetime, time, date, timedelta
import numpy as np
import numpy.ma as ma
from moyenne import moyenne
import time

def plot_CEMS(i,j,date,var):
	if var == 'ctth_alti' or var=='ctth_pres':
		nom_dossier = 'CTTH'
	if var == 'cma':
		nom_dossier = 'CMA'
	if var == 'ct':
		nom_dossier = 'CT'
	if var == 'cmic_phase' or var=='cmic_reff' or var=='cmic_cot'or var=='cmic_lwp' or var=='cmic_iwp':
		nom_dossier = 'CMIC'

	date_cems = []
	data = []
	start = time.time()

	for H in range(0, 24):
		for m in [0]: #,15,30,45]:
			file = 'S_NWC_%s_MSG4_globeM-VISIR_%s%s%sT%s%s00Z.nc'%(nom_dossier, str(date.year), str(date.month).zfill(2), str(date.day).zfill(2),str(H).zfill(2), str(m).zfill(2))
			fichier = "/cnrm/phynh/data1/magnaldom/CEMS/DATA/%s_%s/%s/%s"  %(str(date.year), str(date.month).zfill(2), nom_dossier, file )
			try :

				CEMS = Dataset(fichier, "r", format="NETCDF4")

				Z = CEMS.variables[var][i,j]
				date_cems.append(datetime(date.year, date.month, date.day,H,m,0))
				CEMS.close()
				#print(Z)
				if ma.getmaskarray(Z)==True:
					data.append(0)
				else:
					data.append(float(Z))
#			except :
#				CEMS = Dataset(fichier+".v2018", "r", format="NETCDF4")
#				Z = CEMS.variables[var][i,j]
#				date_cems.append(datetime(date.year, date.month, date.day,H,m,0))
#				#print(Z)
#				if ma.getmaskarray(Z)==True:
#					data.append(0)
#				else:
#					data.append(float(Z))
			except:
				print("Fichier %s n'existe pas" %(fichier))
				data.append(np.inf)
				date_cems.append(datetime(date.year, date.month, date.day,H,m,0))

	end = time.time()
	#print(end-start)
	#print(len(data))


	return date_cems, data

def plot_CEMS_hf(i,j,date,var):
	if var == 'ctth_alti' or var=='ctth_pres':
		nom_dossier = 'CTTH'
	if var == 'cma':
		nom_dossier = 'CMA'
	if var == 'ct':
		nom_dossier = 'CT'
	if var == 'cmic_phase' or var=='cmic_reff' or var=='cmic_cot'or var=='cmic_lwp' or var=='cmic_iwp':
		nom_dossier = 'CMIC'

	date_cems = []
	data = []
	start = time.time()

	for H in range(0, 24):
		for m in [0,15,30,45]:
			file = 'S_NWC_%s_MSG4_globeM-VISIR_%s%s%sT%s%s00Z.nc'%(nom_dossier, str(date.year), str(date.month).zfill(2), str(date.day).zfill(2),str(H).zfill(2), str(m).zfill(2))
			fichier = "/cnrm/phynh/data1/magnaldom/CEMS/DATA/%s_%s/%s/%s"  %(str(date.year), str(date.month).zfill(2), nom_dossier, file )
			try :

				CEMS = Dataset(fichier, "r", format="NETCDF4")

				Z = CEMS.variables[var][i,j]
				date_cems.append(datetime(date.year, date.month, date.day,H,m,0))
				CEMS.close()
				#print(Z)
				if ma.getmaskarray(Z)==True:
					data.append(0)
				else:
					data.append(float(Z))
#			except :
#				CEMS = Dataset(fichier+".v2018", "r", format="NETCDF4")
#				Z = CEMS.variables[var][i,j]
#				date_cems.append(datetime(date.year, date.month, date.day,H,m,0))
#				#print(Z)
#				if ma.getmaskarray(Z)==True:
#					data.append(0)
#				else:
#					data.append(float(Z))
			except:
				print("Fichier %s n'existe pas" %(fichier))
				data.append(np.inf)
				date_cems.append(datetime(date.year, date.month, date.day,H,m,0))

	end = time.time()
	#print(end-start)
	#print(len(data))


	return date_cems, data

def plot_CEMS_moy(i,j,date,var):

	profiler = cProfile.Profile()
	profiler.enable()
	start1 = time.time()
	if var == 'ctth_effectiv':
		nom_dossier = 'CTTH'
	if var == 'cma':
		nom_dossier = 'CMA'
	if var == 'ct':
		nom_dossier = 'CT'
	if var == 'ctth_alti' or var=='ctth_pres':
		nom_dossier = 'CTTH'
	if var == 'cmic_phase' or var=='cmic_reff' or var=='cmic_cot'or var=='cmic_lwp' or var=='cmic_iwp':
		nom_dossier = 'CMIC'

	date_cems = []
	data = []
	data_moy = []
	date_cems_moy = []


	h_cems = 0
	m_cems =0
	file = 'S_NWC_%s_MSG4_globeM-VISIR_%s%s%sT%s%s00Z.nc'%(nom_dossier, str(date.year), str(date.month).zfill(2), str(date.day).zfill(2),str(h_cems).zfill(2), str(m_cems).zfill(2))
	fichier = "/cnrm/phynh/data1/magnaldom/CEMS/DATA/%s_%s/%s/%s"  %(str(date.year), str(date.month).zfill(2), nom_dossier, file )
	try :
		CEMS = Dataset(fichier, "r", format="NETCDF4")
		Z = CEMS.variables[var][i,j]
		date_cems.append(datetime(date.year, date.month, date.day,h_cems,m_cems,0))
		CEMS.close()
		if ma.getmaskarray(Z)==True:
			data.append(0)
		else:
			data.append(float(Z))
	except:
		print("Fichier %s n'existe pas" %(fichier))
		data.append(np.inf)
		date_cems.append(datetime(date.year, date.month, date.day,h_cems,m_cems,0))



	for H in range(1, 24):
		for m in [15,30,45,0]:
			if H >0:
				if m != 0:
					h_cems = H-1
					m_cems = m
				else :
					h_cems = H
					m_cems = m
			else :
				h_cems = 0
				m_cems = 0
			file = 'S_NWC_%s_MSG4_globeM-VISIR_%s%s%sT%s%s00Z.nc'%(nom_dossier, str(date.year), str(date.month).zfill(2), str(date.day).zfill(2),str(h_cems).zfill(2), str(m_cems).zfill(2))
			fichier = "/cnrm/phynh/data1/magnaldom/CEMS/DATA/%s_%s/%s/%s"  %(str(date.year), str(date.month).zfill(2), nom_dossier, file )
			try :
				CEMS = Dataset(fichier, "r", format="NETCDF4")
#				Z_mat = CEMS.variables[var][:]
#				Z = Z_mat[i,j]
				Z = CEMS.variables[var][i,j]
				date_cems.append(datetime(date.year, date.month, date.day,h_cems,m_cems,0))
				CEMS.close()

				#print(Z)
				if ma.getmaskarray(Z)==True:
					data.append(0)
				else:
					data.append(float(Z))
#			except :
#				CEMS = Dataset(fichier+".v2018", "r", format="NETCDF4")
			except:
				print("Fichier %s n'existe pas" %(fichier))
				data.append(np.inf)
				date_cems.append(datetime(date.year, date.month, date.day,h_cems,m_cems,0))
#
	data_moy.append(data[0])
	date_cems_moy.append(date_cems[0])
	for i in range(1,24):
		moy = moyenne(data[(i*4)-3:i*4+1])
		#print(data[(i*4)-3:i*4+1])
		date_cems_moy.append(date_cems[i*4])
		data_moy.append(moy)


	return date_cems_moy, data_moy

def plot_CEMS_moy4points(date,var, M, N, M1, N1, M2, N2, M3, N3):

	start1 = time.time()
	if var == 'ctth_effectiv' or var == 'ctth_alti' or var=='ctth_pres':
		nom_dossier = 'CTTH'
	if var == 'cma':
		nom_dossier = 'CMA'

	date_cems = []
	date_cems_moy = []
	data = []
	data_moy = []
	data1 = []
	data_moy1 = []
	data2 = []
	data_moy2 = []
	data3 = []
	data_moy3 = []



	for H in range(0, 24):

		for m in [0,15,30,45]:
			file = 'S_NWC_%s_MSG4_globeM-VISIR_%s%s%sT%s%s00Z.nc'%(nom_dossier, str(date.year), str(date.month).zfill(2), str(date.day).zfill(2),str(H).zfill(2), str(m).zfill(2))
			fichier = "/cnrm/phynh/data1/magnaldom/CEMS/DATA/%s_%s/%s/%s"  %(str(date.year), str(date.month).zfill(2), nom_dossier, file )
			start = time.time()
			try :


				CEMS = Dataset(fichier, "r", format="NETCDF4")
#				Z_mat = CEMS.variables[var][:]
#				Z = Z_mat[i,j]
				Z = CEMS.variables[var][M,N]
				Z1 = CEMS.variables[var][M1,N1]
				Z2 = CEMS.variables[var][M2,N2]
				Z3 = CEMS.variables[var][M3,N3]
				date_cems.append(datetime(date.year, date.month, date.day,H,m,0))
				CEMS.close()

				#print(Z)
				if ma.getmaskarray(Z)==True:
					data.append(0)
				else:
					data.append(float(Z))
				if ma.getmaskarray(Z1)==True:
					data1.append(0)
				else:
					data1.append(float(Z1))
				if ma.getmaskarray(Z2)==True:
					data2.append(0)
				else:
					data2.append(float(Z2))
				if ma.getmaskarray(Z3)==True:
					data3.append(0)
				else:
					data3.append(float(Z3))
#			except :
#				CEMS = Dataset(fichier+".v2018", "r", format="NETCDF4")
			except:
				print("Fichier %s n'existe pas" %(fichier))
				data.append(np.inf)
				data1.append(np.inf)
				data2.append(np.inf)
				data3.append(np.inf)
				date_cems.append(datetime(date.year, date.month, date.day,H,m,0))

	end1 = time.time()
	#print("temps extract", end1-start1)


	data_moy.append(data[0])
	data_moy1.append(data1[0])
	data_moy2.append(data2[0])
	data_moy3.append(data3[0])
	date_cems_moy.append(date_cems[0])
	for i in range(1,24):
		moy = moyenne(data[(i*4)-3:i*4+1])
		moy1 = moyenne(data1[(i*4)-3:i*4+1])
		moy2 = moyenne(data2[(i*4)-3:i*4+1])
		moy3 = moyenne(data3[(i*4)-3:i*4+1])
		#print(data[(i*4)-3:i*4+1])
		date_cems_moy.append(date_cems[i*4])
		data_moy.append(moy)
		data_moy1.append(moy1)
		data_moy2.append(moy2)
		data_moy3.append(moy3)


	return date_cems_moy, data_moy, data_moy1, data_moy2, data_moy3



#date, data = plot_CEMS_hf(377,1995,datetime(2020,8,1),"cmic_cot")
#print(data)

#
#lon =1.37883
#lat = 43.621
#M = 471
#N = 1891
#date = datetime(2020,8,2)
#date_cems, data = plot_CEMS_moy(M,N,date,'ctth_effectiv')
#date_cems, data2 = plot_CEMS_moy(M,N,date,'cma')
###print(len(date_cems), len(data))
#for i in range(len(data)):
#	print(data[i], data2[i])
#print(data, data2)