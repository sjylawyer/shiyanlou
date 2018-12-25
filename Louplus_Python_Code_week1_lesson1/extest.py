#!/usr/bin/env python3
num = input("Enter a number:")
new_num = int(num)
try :
	isinstance(new_num,int)
	print("ERROR:abc")
except:
	print('INT:{}'.format(new_num))
