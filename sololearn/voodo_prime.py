def is_prime(number):
	basic_primes = [2, 3, 5, 7, 11]
	if number in basic_primes:
		return True
	for prime in basic_primes:
		if number % prime == 0:
			return False
	return True


def voodo_prime(prime: int):
	decimal = str(1 / prime).split('.')[1]
	return str(prime) in decimal


number = int(input('prime:'))
if is_prime(number):
	if voodo_prime(number):
		print('it is a voodo prime')
	else:
		print('it\'s not a voodo prime')
else:
	print('The number is not a prime number')

