n, m = map(int, raw_input().split())

if m == 0 :

	print 'YES'

else :

	l = map(int, raw_input().split())
	l.sort()
	Possible = 'YES'

	if 1 in l or n in l :

		print 'NO'

	else :

		for x in range(2,m) :

			if l[x]-l[x-2] == 2 :

				Possible = 'NO'
				break

		print Possible