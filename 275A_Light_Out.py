l = []

for x in range(0, 3) :

	l.append(map(int, raw_input().split()))

for x in range(0, 3) :

	s = ''

	for y in range(0, 3) :

		count = 0

		for p in range(0, 3) :

			for q in range(0, 3) :

				if ( x==p and abs(y-q)<=1 ) or ( y==q and abs(x-p)<=1 ) :

					count = count + l[p][q]

		if count % 2 == 0 :

			s = s + '1'

		else :

			s = s + '0'

	print s