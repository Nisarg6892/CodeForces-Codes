# string = raw_input()
string = 'httpruhhphhhpuhruruhhpruhhphruhhru'

a, b, c = string.partition('tp')

d, e, f = c.rpartition('ru')

if f:
	e += '/'

print a+b+'://'+d+'.'+e+f