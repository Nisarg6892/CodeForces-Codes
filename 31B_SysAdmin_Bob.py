string = raw_input()
l = []
DifferenceOfThree = 1
final = []

for x in range(0,len(string)) :

	if string.startswith('@',x) :

		l.append(x)

for x in range( 0, len(l) - 1 ) :

	if l[x+1] - l[x] < 3 :

		DifferenceOfThree = 0
		break

if len(l) > 0 and max(l) < len(string)-1 :

	if DifferenceOfThree == 1 and l[0] > 0 and l[-1] < len(string) :

		for x in range(0, len(l)) :

			if x == 0 :

				d = 0

			if l[x] == l[-1] :

				final.append(string[d:])

			else :			

				final.append(string[d : l[x]+2])

			d = l[x] + 2

		print ','.join(final)

	else :

		print 'No solution'

else :

	print 'No solution'