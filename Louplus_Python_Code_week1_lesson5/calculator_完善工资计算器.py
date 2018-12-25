#!/usr/bin/env python3
import sys
def debug(arg):
	try:
		isinstance(arg,int)
		c=arg.split(":")
		#print(c)
		number,wages= c[0],int(c[1])
		#print(type(wages))
		#return number ,wages
		tax_all(number,wages)
	except:
		print("Parameter Error")

def tax_all(number,wages):
	wage = wages*0.835
	#print(wage)
	if wage<=3500:
		cal = wage
		print('{}:{:.2f}'.format(number,cal))
	elif 3500<wage<=5000:
		cal = wage-(wage-3500)*3/100
		print('{}:{:.2f}'.format(number,cal))
	elif 5000<wage<=8000:
		cal = wage-((wage-3500)*10/100 - 105)
		print('{}:{:.2f}'.format(number,cal))
	elif 8000<wage<=12500:
		cal = wage-((wage-3500)*20/100 - 555)
		print('{}:{:.2f}'.format(number,cal))
	elif 12500<wage<=38500:
		cal = wage-((wage-3500)*25/100 - 1005)
		print('{}:{:.2f}'.format(number,cal))
	elif 38500<wage<=58500:
		cal = wage-((wage-3500)*30/100 - 2755)
		print('{}:{:.2f}'.format(number,cal))
	elif 58500<wage<=83500:
		cal = wage-((wage-3500)*35/100 - 5505)
		print('{}:{:.2f}'.format(number,cal))
	else:
		cal = wage-((wage-3500)*45/100 - 13505)
		print('{}:{:.2f}'.format(number,cal))

if __name__=='__main__':
	for arg in sys.argv[1:]:
		#print(arg)
		debug(arg)
		
		
