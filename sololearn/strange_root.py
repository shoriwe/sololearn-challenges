from math import sqrt

def get_share_digits(s,sr):
	for number in sr:
		if number in s:
			return True
	return False

def main():
	number = float(input('Number:'))
	s = str(number**2).split('.')[0]
	sr = str(sqrt(number)).split('.')[1][:3]
	out = get_share_digits(s,sr)
	print(out,number,sqrt(number),number**2)
main()
