n = int(raw_input())
l = map(int, raw_input().split())

x = min(l)
y = max(l)

if x != y :
	
	print y-x, l.count(x)*l.count(y)

else :

	print 0, (n*(n-1))/2