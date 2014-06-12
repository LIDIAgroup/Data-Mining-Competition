#!/usr/bin/env python
# -*- coding: utf-8 -*-

FILENAME = "data_numeric.csv"
NUM_SAMPLES = 687729
NUM_FILES = 17

samples_per_file = NUM_SAMPLES / NUM_FILES

f = open(FILENAME, 'r')
count = 0

for i in range(0, NUM_FILES):
	f_out = open("sample" + str(count), 'w')
	for i in range(0, samples_per_file):
		f_out.write(f.readline())
	count = count + 1	
