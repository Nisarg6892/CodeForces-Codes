n = raw_input()

dict1 = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
dict2 = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

if len(n) == 1 :
	
	print dict1[int(n)]

else :

	if n[0] == '1' :

		print dict2[int(n)]

	elif n[1] == '0' :

		print dict2[int(n[0])]

	else :

		print dict2[int(n[0])]+'-'+dict1[int(n[1])]


