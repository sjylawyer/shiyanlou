#!/usr/bin/env python3
import sys

output_dict = {}

def handle_data(arg):
	a = arg.split(':')
	output_dict[a[0]] = a[1]
	return output_dict

def print_data(key,output_dict):
	print("ID:{} Name:{}".format(key,output_dict))


if __name__=='__main__':
	for arg in sys.argv[1:]:
		handle_data(arg)
	for key in output_dict:
		print_data(key,output_dict[key])
	
