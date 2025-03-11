# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:03:15 2020

@author: Adèle
"""
import numpy as np
import pylab
import os
from math import *
import time
from datetime import datetime, time, date, timedelta
import dateutil
import math
from sunposition import sunpos
import ephem

#In : lattitude et longitude, et date/heure en format datetime
#Out : l'altitude du soleil (complémentaire de l'angle zénithal)
# def zenith_angle_ephem(lat_site,lon_site,date_i):
#     home = ephem.Observer()
#     home.date = date_i
#     home.lat = lat_site
#     home.lon = lon_site
#     sun = ephem.Sun()
#     sun.compute(home)
#     return 90-math.degrees(sun.alt)

def zenith_angle(lat_site,lon_site,date_i):
    az,zen = sunpos(date_i,lat_site,lon_site,0)[:2]
    return zen

def zenith_angle_ephem(lat_site,lon_site,date_i):
	obs=ephem.Observer()
	obs.date = date_i
	obs.lat=lat_site* ephem.degree
	obs.long=lon_site* ephem.degree
	sun = ephem.Sun(obs)
	zen_angle = np.pi/2 - sun.alt
	cos_solar_zenith_angle = np.cos(zen_angle)
	return cos_solar_zenith_angle

def degree_angle_ephem(lat_site,lon_site,date_i):
	obs=ephem.Observer()
	obs.date = date_i
	obs.lat=lat_site* ephem.degree
	obs.long=lon_site* ephem.degree
	sun = ephem.Sun(obs)
	zen_angle = np.pi/2 - sun.alt
	azi_angle = sun.az
	return math.degrees(zen_angle),math.degrees(azi_angle)



#print(zenith_angle_ephem(51,4.3,datetime(2020,8,8,12,30,)))