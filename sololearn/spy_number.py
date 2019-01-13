def mcm(number):
	primes = [7, 5, 3, 2, 1]
	results = []
	for n in primes:
		if number % n == 0:
			results.append(n)
	if len(results) == 0:
		results = [number]
	return results


def mult(x: iter):
	result = 1
	for number in x:
		result *= number
	return result


def spy_number_checker(number):
	mcm_ = mcm(number)
	
	if sum(mcm_) == mult(mcm_) and len(mcm_) != 1:
		return True
	return False

for number in range(20001):
	result = spy_number_checker(number)
	if result:
		print(number)

