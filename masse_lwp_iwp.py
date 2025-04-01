#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:06:46 2021

@author: magnaldom
"""

import numpy as np

def water_path(var_c, p_c): #p_c en point flux. Premier point : sol, dernier point : sommet atmosphère
	g = 9.81
#	print(np.shape(var_c), np.shape(p_c))
#	print(np.shape(p_c[:,:,:-1]-p_c[:,:,1:]))
	return ( -var_c * (p_c[:,:,:-1]-p_c[:,:,1:]) / g).sum(axis=-1)

def water_path_c(var_c, p_c): #p_c en point flux
	g = 9.81
#	print(np.shape(var_c), np.shape(p_c))
#	print(np.shape(p_c[:,:,:-1]-p_c[:,:,1:]))
	return (- var_c * (p_c[:-1]-p_c[1:]) / g).sum(axis=-1)

#def water_path_c(var_c, qt_c, p_c, t_c): #!!!!!! p_c et t_c en point de flux
#	g = 9.81
#	masse = 0
#	for it in range(len(var_c)):
#		rl = var_c[it]/(1-qt_c[it]) # qt = liquid + rain + ice + graupel + snow + vapor
#		dp = -(p_c[it]-p_c[it+1])
#		m = rl*dp/g
#		#if m<1000:
#		masse = masse + m
#	return masse

def HS_to_HR(HS,t):
	theta = t + 273.15
	psat = np.exp(23.3265-(3802.7/theta)-((472.68/theta)**2))
	c1 = 0.622
	c2 = 101325
	HR = (HS*c2)/(psat*(c1-HS))
	if HR>1:
		HR = 1
	return HR


def rho(HR, p,t):
	theta = t + 273.15
	T1 = 1/(287.06*theta)
	T2 = 230.617*HR*np.exp(17.5043*t/(241.2+t))
	rho = T1*(p-T2)
	return rho

def rho_sec(p, t):
	M = 0.029
	R = 8.3144621
	rho = p*M/(R*t)
	return rho






#		p_m = np.sqrt(p_c[j]*p_c[j+1]) # On récupe p au point de masse
#		t_m = np.interp(p_m,p_c[:],t_c[:]) # On interp pour avoir la t au point de masse
