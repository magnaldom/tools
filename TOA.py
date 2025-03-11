#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:13:13 2021

@author: magnaldom
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
import sys; sys.path.insert(0,'/cnrm/phynh/data1/magnaldom/Outils')
from zenith_angle import zenith_angle_ephem
from get_solar_constant import get_solar_constant

def TOA_moyen(lon, lat, date_v):
	flux = []
	for h in range(1,23):
		for m in range(0,59):
			date = datetime(date_v.year, date_v.month, date_v.day, h, m)
			cos_zen = zenith_angle_ephem(lat,lon,date)
			S = get_solar_constant(date)
			if cos_zen>0.1:
				flux.append(cos_zen*S*1365)
	return np.mean(flux)

def TOA_moyen_heure(lon, lat, date_v, h):
	flux = []
	for m in range(0,59):
		date = datetime(date_v.year, date_v.month, date_v.day, h-1, m)
		cos_zen = zenith_angle_ephem(lat,lon,date)
		S = get_solar_constant(date)
		if cos_zen>0:
			flux.append(cos_zen*S*1365)
	return np.mean(flux)