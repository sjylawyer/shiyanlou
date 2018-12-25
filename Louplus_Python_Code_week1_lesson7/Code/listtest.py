#!/usr/bin/env python3
import sys
items = sys.argv[1:]
first_line =[]
second_line=[]
for item in items:
	#print(item)
	if len(item)<=3:
		first_line.append(item)
	else:
		second_line.append(item)
#print(first_line)
print(" ".join(str(i) for i in first_line))
#for first_item in first_line:
	#print(first_item,end=' ')
#print(second_line)
print(" ".join(str(i) for i in second_line))
#for second_item in second_line:
	#print(second_item,end=' ')
