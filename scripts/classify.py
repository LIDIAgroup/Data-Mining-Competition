'''
Clasifica todos los patrones que hay en TEST_FILE
Se almacenan los votos de cada clasificador para cada patron en la lista de votaciones,
el patron se clasifica segun la clase mas votada
'''

import numpy as np
import time
from sklearn import svm, datasets
from sklearn.externals import joblib
from os import listdir

SVM_DIR = "svm/"
NUM_FEATURES = 630
TEST_FILE = "test.csv"

# Cargamos todos los clasificadores entrenados y los guardamos en la lista svm_list
svm_list = []
for f in sorted(listdir(SVM_DIR)):
	if f.endswith(".pkl"):
		svm_list.append(joblib.load(SVM_DIR + f))

# Cargamos los datos a clasificar (TEST_FILE)
data = np.loadtxt(open(TEST_FILE,"rb"), delimiter=",", skiprows=0)
test_data = data[:, :NUM_FEATURES] # [patrones, features]


i = 0
for sample in test_data:
	votations = []
	# Cada svm clasifica el patron y almacena su voto
	for classifier in svm_list:
		votations.append(classifier.predict(sample))
	if (sum(votations) >= 0):
		print "Sample " + str(i) + " True " + str(sum(votations))
	else:
		print "Sample " + str(i) + " False " + str(sum(votations))
	i = i + 1
