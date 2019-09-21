

def openFile(name):
	with open(name) as f:
		read_data = f.read()
		print(read_data)

