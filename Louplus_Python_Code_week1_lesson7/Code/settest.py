#!/usr/bin/env python3
import sys
items = sys.argv[1:]
settest = set()
a = []
for item in items:
	a.append(item)
	#print(a)
for i in a:
	settest.add(i)
#print(settest)
print(" ".join(str(i) for i in settest))

