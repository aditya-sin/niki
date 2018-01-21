import math

def factorization(num):
	factors = []

	for i in range(2,int(math.sqrt(num))+1):
		if num%i == 0:
			if num/i != i:
				factors.extend([i,num/i])
			else:
				factors.append(i)
	factors.append(num)
	factors.sort()
	if len(factors) == 1:
		print "%s is a prime number" %num
		print "There are no factors other than 1 and %s"%num
	else:
		print "%s is not a prime number" %num
		print "Factors of %s are:"%num
		for f in factors:
			print f


num = raw_input()
factorization(int(num))