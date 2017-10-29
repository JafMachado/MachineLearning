#!/usr/bin/env python3
import numpy as np

#POSSIVEIS CLASSIFICACOES
#0 - POP-ROCK
#1 - ELETRONIC
#2 - RAP
#3 - JAZZ
#4 - LATIN
#5 - RnB
#6 - INTERNATIONAL
#7 - COUNTRY
#8 - REAGGAE
#9 - BLUES

#FORMATO DE CADA LINHA
#00-047  MFCCs,  4*12 VALORES, I.E., (MEDIA,VAR,min,MAX)
#48-095  CHROMA, 12*4 VALORES, I.E., 12*(MEDIA,VAR,min,MAX)
#96-263  Rhythm, 24*7 VALORES, I.E., 24*(MEDIA,MEDIANA,VAR,KURT,SKEW,min,MAX)

data=np.genfromtxt("ACCURACY/train_data.csv",delimiter=',')
answers=np.genfromtxt("ACCURACY/train_labels.csv")

averages=np.ndarray(shape=(len(data),4+4+7), dtype=float, order='F')

for l in range(0,len(data)):
	for k in range(0,2):
		for j in range(0,4):
			for i in range(0,12):
				averages[l][j+k*4]+=data[l][i+j*12+k*48]/12
	for j in range(0,7):
		for i in range(0,24):
			averages[l][j+8]+=data[l][i+j*24+96]/24

print(averages[0:6])





