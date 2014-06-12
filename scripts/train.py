#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Entrena un clasificador por cada csv que hay en DATA_DIR y los guarda en disco.
'''
import numpy as np
import time
from sklearn import svm, datasets
from sklearn.externals import joblib
from os import listdir
from subprocess import call

DATA_DIR = "m_subsamples/"
NUM_FEATURES = 630

# Por cada archivo que hay en DATA_DIR entrenamos un svm
for f in sorted(listdir(DATA_DIR)):
	print "Training with " + str(f)
	start = time.time()
	# Cargamos los datos como CSV	
	data = np.loadtxt(open(DATA_DIR+f,"rb"), delimiter=",", skiprows=0)
	train = data[:, :NUM_FEATURES]
	# Entrenamos el clasificador
	classifier = svm.OneClassSVM(kernel='linear', verbose=True)
	classifier.fit(train)
	end = time.time()
	print "Time elapsed: " + str(end - start)
	# Guardamos el clasificador
	joblib.dump(classifier, 'svm'+str(f)+".pkl") 

#NOTA: Esto genera una serie de archivos .pkl y .npy que tienen que ser guardados juntos.

