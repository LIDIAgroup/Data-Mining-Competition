FILENAME = "TrainFold0w4"
FILE_OUTPUT = "big_data_numeric.csv"


f = open(FILENAME, 'r')
output = open(FILE_OUTPUT, 'w')
for line in f:
	line = line.replace('H','1')
	line = line.replace('E','2')
	line = line.replace('C','3')
	line = line.replace('X','5')
	output.write(line)

	
