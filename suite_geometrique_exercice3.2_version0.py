#!/usr/bin/python
# -*-coding:Latin-1 -*
#
# Exercice 3.2
# Suite geometrique   Vn = V0 x q puissance n
# Syntaxe python 3.x
# Print avec des (), d�finitions des variables num�riques sous la forme Vx: int = y

import fractions

print("# Suite geometrique   Vn = V0 x q puissance n")
V1: int = 5
q: int = 4
n: int = 5
# V0=V1/(q**1) soit V0=5/(4**1)  V0=5/4
V0 = fractions.Fraction(5, 4)
V5 = V0 * (q ** n)

print('V0  = ', V0)
print('V1  = ', V1)
print('q   = ', q)
print('n   = ', n)
print('V5 = V0*(q**n)= ', V5)
print('/n')

# S5=V0*((1-q**(n+1)))/(1-q)
# calcVl = "S5 = V0*((1-q**(n+1)))/(1-q) = "
# print calcVl, S5
print('/n')

# Vn = V0*q**n
Vn = 0  # type: int
ST = 0

for i in range(0, n + 1):
    if i == 0:
        Vn = V0
        ST = ST + Vn
        print(i, 'V', i, '= ', Vn)  # , 'ST = ', ST)
    else:
        m: int = i
        Vn = V0 * q ** m
        ST = ST + Vn
        print(i, 'V', i, '= ', Vn)  # , 'ST = ', ST)
exit()

"""
python suite_géométrique_exercice3.2.py 
# Suite géométrique   Vn = V0 x q puissance n
V0  =  5/4
V1  =  5
q   =  4
n   =  5
V5 = V0*(q**n)=  1280


0 V 0 =  5/4
1 V 1 =  5
2 V 2 =  20
3 V 3 =  80
4 V 4 =  320
5 V 5 =  1280
"""
