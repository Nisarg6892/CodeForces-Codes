p = raw_input()
p = p.replace('-','').replace('_','').replace(';','').lower()

q = raw_input()
q = q.replace('-','').replace('_','').replace(';','').lower()

r = raw_input()
r = r.replace('-','').replace('_','').replace(';','').lower()

l = [p+q+r, p+r+q, q+p+r, q+r+p, r+p+q, r+q+p]

n = int(raw_input())

for x in range(0, n) :

	s = raw_input()

	s = s.replace('-','').replace('_','').replace(';','').lower()

	if s in l :

		print 'ACC'

	else :

		print 'WA'