#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Realiza un muestreo aleatorio de patrones pertenecientes a la clase mayoritaria.
El tamaño del muestreo viene dado por NUM_SAMPLES
'''
from random import randint

FILENAME = "big_data_numeric.csv"
FILE_OUTPUT = "majority.csv"
CLASS_INDEX = 631
NUM_SAMPLES = 687729

f = open(FILENAME, 'r')
file_out = open(FILE_OUTPUT, 'w')

selected = 0
count = 0
for line in f:
    if selected <= NUM_SAMPLES:
	    if (count % 1000 == 0):
	    	print 'Process: ' + str(count)
	    count = count + 1
	    if not line.startswith('@'):
		class_value = (line.split(',')[CLASS_INDEX]).strip()
		if (class_value is '0'):
		    if (randint(0,1000) < 100):  
		    	file_out.write(line)
			selected = selected + 1
    else:
	break

