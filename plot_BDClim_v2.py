#
#Marie-Adele Magnaldo
#04/11/2020
#

#####Import
import numpy as np
from datetime import datetime, timedelta
import math
import csv
from num_jour import num_jour
from num_jour_between import num_jour_between
import matplotlib.pyplot as plt
#from zenith_angle import zenith_angle
import matplotlib.dates as md

def plot_BDClim(fichier,date):
#On importe l'heure et la date
	data_date = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(0,1), unpack=True)

#On importe les valeurs
	data_val_str = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(2,3), unpack=True)

#On recupere les dates
	dates=[]
	k = 0
	M = 0
	for n in range(len(data_date[0][:])):
		d_h = data_date[0][n]+ ' ' + data_date[1][n]
		D = datetime.strptime(d_h, '%Y-%m-%d %H:%M:%S')
		dates.append(D)

		if D==date and k == 0:

			M = n
			k = 1
	N = M + 24


#On convertit en float
	qlot = []
	dirt = []
	for i in range(len(data_val_str[0,:])):
		s1 = data_val_str[0,i]
		s2 = data_val_str[1,i]
		if s1!="":
			f = float(s1)
			qlot.append((f/3600)*10000)
		else :
			qlot.append(np.inf)
		# if s2!="":
		#	 f = float(s2)
		#	 dirt.append(((f/3600)*10000)*abs(math.sin(zenith_angle(lat,lon,dates[i]))))
		# else :
		#	 dirt.append(np.inf)


	return dates[M:N], qlot[M:N]

def plot_BDClim_inter_date(fichier,date1, date2):
#On importe l'heure et la date
	data_date = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(0,1), unpack=True)

#On importe les valeurs
	data_val_str = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(2,3), unpack=True)

#On recupere les dates
	dates=[]
	k = 0
	l = 0
	M = 0
	N = 0
	for n in range(len(data_date[0][:])):
		d_h = data_date[0][n]+ ' ' + data_date[1][n]
		D = datetime.strptime(d_h, '%Y-%m-%d %H:%M:%S')
		dates.append(D)

		if D==date1 and k == 0:
			M = n
			k = 1
		if D==date2 and l == 0:
			N = n + 24
			l = 1



#On convertit en float
	qlot = []
	dirt = []
	for i in range(len(data_val_str[0,:])):
		s1 = data_val_str[0,i]
		s2 = data_val_str[1,i]
		if s1!="":
			f = float(s1)
			qlot.append((f/3600)*10000)
		else :
			qlot.append(np.inf)
		# if s2!="":
		#	 f = float(s2)
		#	 dirt.append(((f/3600)*10000)*abs(math.sin(zenith_angle(lat,lon,dates[i]))))
		# else :
		#	 dirt.append(np.inf)


	return dates[M:N], qlot[M:N]

def plot_BDClim_station(num_station,date1, date2):
#On importe l'heure et la date
	nb_jour = num_jour_between(date1, date2)
	date_l = []
	qlot = []
	for d in range(nb_jour):
		date = date1 + timedelta(days=d)
		if date.month<10:
			m_str = '0'+str(date.month)
		else:
			m_str = str(date.month)
		if date.day<10:
			d_str = '0'+str(date.day)
		else :
			d_str = str(date.day)
		for h in range(0,24):
			if h<10:
				h_str = '0'+str(h)
			else :
				h_str = str(h)
			fichier = '/cnrm/phynh/data1/magnaldom/BDClim/obs_BDClim/BDClim_%s_%s_%s_%s' %(date.year, m_str, d_str, h_str )



#On importe les valeurs
			data_val_str = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(0,3), unpack=True)
			#data = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(4), unpack=True)
			station = data_val_str[0]
			data = data_val_str[1]
			#print(station)


			for i in range(len(station)):
				if float(station[i]) == float(num_station):

					qlot.append((float(data[i])/3600)*10000)
					date_l.append(datetime(date.year, date.month, date.day,h))


	return date_l, qlot

def plot_BDClim_station_h(num_station,date1,h):
	m_str = str(date1.month).zfill(2)
	d_str = str(date1.day).zfill(2)
	h_str = str(h).zfill(2)
	fichier = '/cnrm/phynh/data1/magnaldom/BDClim/obs_BDClim/BDClim_%s_%s_%s_%s' %(date1.year, m_str, d_str, h_str )
#On importe les valeurs
	data_val_str = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(0,3), unpack=True)
	#data = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(4), unpack=True)
	station = data_val_str[0]
	data = data_val_str[1]
	#print(station)
	qlot = np.inf

	for i in range(len(station)):
		if float(station[i]) == float(num_station):
			qlot = (float(data[i])/3600)*10000
	return  qlot

def plot_BDClim_station_cumul(num_station,date1, date2):
#On importe l'heure et la date
	nb_jour = num_jour_between(date1, date2)
	qlot = 0
	for d in range(nb_jour):
		date = date1 + timedelta(days=d)
		if date.month<10:
			m_str = '0'+str(date.month)
		else:
			m_str = str(date.month)
		if date.day<10:
			d_str = '0'+str(date.day)
		else :
			d_str = str(date.day)
		for h in range(0,24):
			if h<10:
				h_str = '0'+str(h)
			else :
				h_str = str(h)
			fichier = '/cnrm/phynh/data1/magnaldom/BDClim/obs_BDClim/BDClim_%s_%s_%s_%s' %(date.year, m_str, d_str, h_str )



#On importe les valeurs
			data_val_str = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(0,3), unpack=True)
			#data = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(4), unpack=True)
			station = data_val_str[0]
			data = data_val_str[1]
			#print(station)


			for i in range(len(station)):
				if float(station[i]) == float(num_station):

					qlot = qlot + (float(data[i])*10000)



	return date1, qlot

def plot_BDClim_station_dif(num_station,lon, lat, date1, date2):
#On importe l'heure et la date
	nb_jour = num_jour_between(date1, date2)
	date_l = []
	qlot = []
	dift = []
	for d in range(nb_jour):
		date = date1 + timedelta(days=d)
		if date.month<10:
			m_str = '0'+str(date.month)
		else:
			m_str = str(date.month)
		if date.day<10:
			d_str = '0'+str(date.day)
		else :
			d_str = str(date.day)
		for h in range(0,24):
			if h<10:
				h_str = '0'+str(h)
			else :
				h_str = str(h)
			fichier = '/cnrm/phynh/data1/magnaldom/BDClim/obs_BDClim/BDClim_%s_%s_%s_%s' %(date.year, m_str, d_str, h_str )
			D = datetime(date.year, date.month, date.day,h)



#On importe les valeurs
			data_val_str = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(0,3,5), unpack=True)
			#data = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(4), unpack=True)
			station = data_val_str[0]
			data_glo = data_val_str[1]
			data_dir = data_val_str[2]
			#print(station)


			for i in range(len(station)):
				if station[i] == str(num_station):
					f = (float(data_glo[i])/3600)*10000
					#print(f)
					qlot.append(f)
					dift.append(f-((float(data_dir[i])*10000/3600)*abs(np.cos(math.radians(zenith_angle(lat,lon,D))))))
					date_l.append(D)


	return date_l, qlot, dift

def plot_BDClim_station_nebul(num_station, date1, date2):
#On importe l'heure et la date
	nb_jour = num_jour_between(date1, date2)
	date_l = []
	n1 = []
	n2 = []
	n3 = []
	n4 = []
	n = []
	for d in range(nb_jour):
		date = date1 + timedelta(days=d)
		if date.month<10:
			m_str = '0'+str(date.month)
		else:
			m_str = str(date.month)
		if date.day<10:
			d_str = '0'+str(date.day)
		else :
			d_str = str(date.day)
		for h in range(0,24):
			if h<10:
				h_str = '0'+str(h)
			else :
				h_str = str(h)
			fichier = '/cnrm/phynh/data1/magnaldom/BDClim/obs_BDClim/BDClim_%s_%s_%s_%s' %(date.year, m_str, d_str, h_str )
			D = datetime(date.year, date.month, date.day,h)



#On importe les valeurs
			data_val_str = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(0,9, 10, 11, 12, 13), unpack=True)
			#data = np.loadtxt(fichier, dtype = 'str', delimiter=' ', usecols=(4), unpack=True)
			station = data_val_str[0]
			data_n1 = data_val_str[1]
			data_n2 = data_val_str[2]
			data_n3 = data_val_str[3]
			data_n4 = data_val_str[4]
			data_n = data_val_str[5]
			#print(station)


			for i in range(len(station)):
				if station[i] == str(num_station):
					f1 = (data_n1[i])
					if f1 != "":
						n1.append(float(f1))
					else :
						n1.append(np.inf)
					f2 = (data_n2[i])
					if f2 != "":
						n2.append(float(f2))
					else :
						n2.append(np.inf)
					f3 = (data_n3[i])
					if f3 != "":
						n3.append(float(f3))
					else :
						n3.append(np.inf)
					f4 = (data_n4[i])
					if f4 != "":
						n4.append(float(f4))
					else :
						n4.append(np.inf)
					f = (data_n[i])
					if f != "":
						n.append(float(f))
					else :
						n.append(np.inf)

					date_l.append(D)


	return date_l, n1, n2, n3, n4, n


def plot_DSO(date):
	time = []
	data = []
	fichier_out = '/cnrm/phynh/data1/magnaldom/BDClim/Donnees_min/rayonnement_20190801_20200901_v2.dat'
	#Pour convertir du .csv en .dat
	# fi = open(fichier_out,'w')
	# M = 0
	# N = 24*3600
	# with open(fichier+'.csv', newline='') as csvfile:
	#	 spamreader = csv.reader(csvfile, delimiter=';', quotechar='\t')
	#	 for row in spamreader:
	#		 fi.write(' '.join(row)+'\n')
	# fi.close()

	data_val_str = np.loadtxt(fichier_out, dtype = 'str', delimiter=' ', usecols=(1), unpack=True)
	data_date = np.loadtxt(fichier_out, dtype = 'str', delimiter=' ', usecols=(0), unpack=True)

	k = 0
	M=5*24
	for n in range(2,len(data_date)):
		D = datetime.strptime(data_date[n], '%Y%m%d_%H%M')
		time.append(D)
		#print(D)
		if D==date and k == 0:
			M = n
			k = 1

		if float(data_val_str[n])>-10:
			data.append(float(data_val_str[n]))
		else :
			data.append(np.inf)

	N = M + 24*60


	return time[M:N], data[M:N]



def plot_BDClim_toulouse_inter_date(fichier,date1,date2):
	time = []
	data = []
	fichier_out = fichier+'.dat'

	data_val_str = np.loadtxt(fichier_out, dtype = 'str', delimiter=' ', usecols=(1), unpack=True)
	data_date = np.loadtxt(fichier_out, dtype = 'str', delimiter=' ', usecols=(0), unpack=True)

	k = 0
	l =0
	M =0
	N = 0
	for n in range(1,len(data_date)):
		D = datetime.strptime(data_date[n], '%Y%m%d_%H%M')
		time.append(D)
		#print(D)
		if D==date1 and k == 0:
			#print(D)
			M = n
			k = 1
		if D==date2 and l == 0:
			N = n +(24*60)
			l = 1

		if float(data_val_str[n])>-10:
			data.append(float(data_val_str[n]))
		else :
			data.append(np.inf)



	return time[M:N], data[M:N]

#date_test = datetime(2020,8,20)
#date, ghi= plot_BDClim_station('01033002', date_test, date_test)
##date, ghi = plot_BDClim_station(31069001, date_test, date_test)
#
##date2, ancien= plot_BDClim("/cnrm/phynh/data1/magnaldom/BDClim/H_2019_31069001.dat", date_test)
#
#axes = plt.gca()
#xfmt = md.DateFormatter('%H:%M:%S')
#axes.xaxis.set_major_formatter(xfmt)
#plt.setp(axes.get_xticklabels(), rotation = 25)
#plt.plot_date(md.date2num(date), ghi, 'r-', label='ghi')
##plt.plot_date(md.date2num(date), dif, 'b-', label='dif', linewidth = 1)
#plt.title("Flux de rayonnement total la journee sur une journee")
#plt.ylabel('W.m-2')
#plt.xlabel('UTC')
#plt.legend()
##plt.savefig("/cnrm/phynh/data1/magnaldom/ETUDES/detection_ciel_clair/GRAPHES/MPF_%s_%s_%s" %(date.day, date.month, date.year), bbox_inches="tight")
#plt.show()
##plt.close()

#date1 = datetime(2020,8,5)
#num_station = '1033002'
#
#date, data = plot_BDClim_station(num_station,date1, date1)
#print(data)
