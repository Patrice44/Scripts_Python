#!/usr/bin/python
# -*-coding:Latin-1 -*
#
# Suite geometrique   Un = U0 x q puissance n
# Ajout () aux instructions print / Compatibilite python 3.x

print("# Suite geometrique   Un = U0 x q puissance n")
U0=3
q=2
n=4
U4=U0*(q**n)
LineBreak = "\n"

print('U0  = ', U0)
print('q   = ', q)
print('n   = ', n)
print('U4 = U0*(q**n)= ', U4)
print(LineBreak)

S5=U0*((1-q**(n+1)))/(1-q)
calcul = "S5 = U0*((1-q**(n+1)))/(1-q) = "
print(calcul, S5)
print(LineBreak)

# Un = U0*q**n
Un=0
ST=0

for i in range(0,n+1):
	if i == 0:
		Un=U0
		ST=ST+Un
		print(i,'U',i, '= ', Un, 'ST = ', ST)
	else:
		n=i
		Un=U0*q**n
		ST=ST+Un
		print(i,'U',i, '= ', Un, 'ST = ', ST)
exit()
