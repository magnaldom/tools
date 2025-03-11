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

def get_solar_constant(date):
	obs = ephem.Observer()
	obs.date = date
	sun = ephem.Sun(obs)
	distance = sun.earth_distance
	S = (1./distance)**2
	return S

#S = get_solar_constant(datetime(2020,8,5,1))
#print(S*1366)