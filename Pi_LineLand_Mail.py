n = int(raw_input())
l = map(int, raw_input().split())

for x in range(0, len(l)) :

	if x == 0 :

		print l[x+1]-l[x], l[-1]-l[x]

	elif x == n-1 :

		print l[x]-l[x-1], l[x]-l[0]

	else :

		print min(l[x]-l[x-1],l[x+1]-l[x]), max(l[x]-l[0], l[-1]-l[x])