#!/usr/bin/env pyfilename = input("Enter file path:")
filename = '/etc/protocols'
f = open(filename)
try:
	f.write('shiyanlou')
except:
	print("File write error")
finally:
	print("finally")
	f.close()
