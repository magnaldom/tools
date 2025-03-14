#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:51:07 2021

@author: magnaldom
"""
import sys; sys.path.insert(0,'/cnrm/phynh/data1/magnaldom/Outils')
import numpy as np
from masse_eau import HS_to_HR, rho

def calcul_z(p,HS,t):
	z = np.zeros((len(p)))
	p0  = 101325
	rho_c = np.zeros(len(HS))

	for k in range(len(p)):
		HR = HS_to_HR(HS[k], t[k]-273.15)
		#rho[k] = rho(HR, (p[k]+p[k+1])/2, (t[k]-273.15+t[k+1]-273.15)/2)
		rho_c[k] = rho(HR, p[k], t[k]-273.15)
#		print(rho(HR, p[k], t[k]-273.15))
#		print(t[k])
#		print(HR)
		#print("rho", rho_temp)

	for k in range(len(p)):
		z[k]=(-(p[k]-p0)/(rho_c[k]*9.81))
	return z