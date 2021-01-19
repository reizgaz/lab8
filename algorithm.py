import math


def factorization(n):
	if n < 0:
		result = "error, try again"
	else:
		result = str(math.factorial(n))
	return result
