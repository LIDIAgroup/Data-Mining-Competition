FILENAME = "data.csv"
CLASS_INDEX = 630

f = open(FILENAME, 'r')
for line in f:
	if not line.startswith('@'):
		class_value = (line.split(',')[CLASS_INDEX]).strip()
		if (class_value is '1'):
			print line,
