def sendfile(hex):
	f = open("sample.txt", "w")
	f.write(str(hex))


sendfile(000000)
