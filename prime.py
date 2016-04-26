''' this function checks if the number is divisable by 3 or 5 '''
def primeNumber(x):
	return x%3 == 0 or x%5 == 0

print 'The primeNumber is %s: ' %primeNumber(145)

print 'The filter option %s: ' %filter(primeNumber, range(1,11))

# convert decimal to binary
def dec_to_bin(x):
	return int(bin(x)[2:])

print "The binary conversion of number 14 is : %s " %dec_to_bin(14)
