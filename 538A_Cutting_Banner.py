string = raw_input()
result = 'NO'

for x in range(0, len(string)+1) :

	for y in range(x, len(string)+1) :

		if string[:x] + string[y:] == 'CODEFORCES' :
			
			result = 'YES'
			break

print result