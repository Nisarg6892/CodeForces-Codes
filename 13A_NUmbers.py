from fractions import Fraction

n = int(raw_input())
sum = 0

for x in range(2, n) :

	m = n

	while m > 0 :

		sum = sum + (m%x)
		m = m // x

string = str(Fraction(sum,n-2))

if '/' not in string :

	print string+'/1'

else :

	print string