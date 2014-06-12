'''
Muestrea todos los patrones pertenecientes a la clase minoritaria.
'''
FILENAME = "big_data_numeric.csv"
FILE_OUTPUT = "data_min.csv"
CLASS_INDEX = 631

f = open(FILENAME, 'r')
file_out = open(FILE_OUTPUT, 'w')

count = 0
for line in f:
    if (count % 1000 == 0):
    	print 'Process: ' + str(count)
    count = count + 1
    if not line.startswith('@'):
        class_value = (line.split(',')[CLASS_INDEX]).strip()
        if (class_value is '1'):
            file_out.write(line)
