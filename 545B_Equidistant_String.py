s=raw_input()
t=raw_input()
count = 0
l=[]

for x in range(0,len(s)) :

	if s[x] != t[x] :

		count+=1
		
		if count%2 == 0:
			l.append(s[x])
		else :
			l.append(t[x])

	else :

		l.append(s[x])


if count%2 != 0 :

	print 'impossible'

else :

	print ''.join(l)