f = open('input.txt','r')
n = f.readline().strip()
str1 = f.readline().strip()
str2 = f.readline().strip()
str3 = f.readline().strip()

fw = open('output.txt','w')

if n in str1 :

	n = str1.replace(n,'').replace(' ','')

if n in str2 :

	n = str2.replace(n,'').replace(' ','')

if n in str3 :

	n = str3.replace(n,'').replace(' ','')

fw.write(n)