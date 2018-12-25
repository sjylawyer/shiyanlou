#!/usr/bin/env python3


def compute(result,start,end):
	while start <= end:
		result += start
		start +=1
	print(result)


if __name__=='__main__':
	result = 0
	start = 1
	end = 100
	compute(result,start,end)
