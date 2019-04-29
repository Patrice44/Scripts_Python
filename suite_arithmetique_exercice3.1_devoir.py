#!/usr/bin/python
# -*-coding:Latin-1 -*
#
# Exercice 3.1
# Suite arithmétique   Un+1 = Un + r
print "Suite arithmétique   Un+1 = Un + r"
U1=10
r=-4
n=5

U0=U1-(1*r)
U5=U0+(n*r)
print 'U0  = ', U0
print 'U1  = ', U1
print 'r   = ', r
print 'n   = ', n
print 'U5 = U0+(n*r)= ', U5

# S12=((n+1)*(U0+U12))/2
# print 'S12 = ((n+1)*(U0+U12))/2 = ', S12
# print ''

#Un+1 = Un + r
Un=0
ST=0

for i in range(0,n+1):
	if i == 0:
		Un=U0
		ST=ST+Un
		print i,'U',i, '= ', Un #, 'ST = ', ST
	else:
		Un=Un+r
		ST=ST+Un
		print i,'U',i, '= ', Un #, 'ST = ', ST
exit()

"""
python suite_arithmétique_exercice3_devoir.py 
Suite arithmétique   Un+1 = Un + r
U0  =  14
U1  =  10
r   =  -4
n   =  5
U5 = U0+(n*r)=  -6
 0 U 0 =  14
 1 U 1 =  10
 2 U 2 =  6
 3 U 3 =  2
 4 U 4 =  -2
 5 U 5 =  -6  
"""
