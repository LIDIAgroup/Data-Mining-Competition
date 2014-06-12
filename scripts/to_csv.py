'''
Elimina las cabeceras del .arff para quedarse con un csv.
'''

FILENAME = "TrainFold0w4"
FILE_OUTPUT = "data.csv"

f = open(FILENAME, 'r')
file_out = open(FILE_OUTPUT, 'w')

count = 0
for line in f:
    if (count % 1000 == 0):
    	print 'Process: ' + str(count)
    count = count + 1
    if not line.startswith('@'):
	file_out.write(line)
