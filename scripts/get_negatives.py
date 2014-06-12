FILENAME = "data.csv"
CLASS_INDEX = 4
NUMBER = 600000

f = open(FILENAME, 'r')
for line in f:
	if not line.startswith('@'):
		class_value = (line.split(',')[CLASS_INDEX]).strip()
		if ((class_value is '0') and (count < NUMBER)):
			print line,
			count = count + 1
