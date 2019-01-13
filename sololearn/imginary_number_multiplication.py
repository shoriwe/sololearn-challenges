def get_values(eq: str):
	result = []
	for number in eq.split('*'):
		result.append([x if x != 'i' else '1i' for x in number.split('+')])
	return result


def mult(x: iter):
	result = 1
	for number in x:
		result *= number
	return result


def simplify(values):
	simplified = []
	for value in values:
		try:
			simplified.append(str(eval(value)))
		except:
			i = value.count('i')
			value = value.replace('i', '')
			value = str(eval(value)) + 'i' * i
			simplified.append(value)

	for number, value in enumerate(simplified):
		simplified[number] = value.replace('ii', '*-1')

	return simplified


def solve(simplified):
	i_cuantity = {'wi': [], 'ni': []}
	for number in simplified:
		if 'i' in number:
			i_cuantity['wi'].append(number)
		else:
			i_cuantity['ni'].append(number)

	return i_cuantity


def get_redult(i_cuantity):
	ni = 0
	wi = 0
	for number in i_cuantity['ni']:
		ni += eval(number)
	for number in i_cuantity['wi']:
		wi += float(number.strip('i'))
	return [str(ni), '{}i'.format(wi)]


def multiply(x, y):
	values = []
	for numero in x:
		for n in y:
			values.append('*'.join([numero, n]))
	simplified = simplify(values)
	i_cuantity = solve(simplified)
	result = get_redult(i_cuantity)
	return result


def eq_solver(equation):

	while len(equation) > 1:
		x, y = equation[0], equation[1]
		equation.remove(x)
		equation.remove(y)
		value = multiply(x, y)
		equation.insert(0, value)

	return '{}+{}'.format(*equation[0])


def main(values):
	eq = get_values(values)
	m = []
	for conjunto in eq:
		x = []
		for value in conjunto:
			x.append(float(value.strip('i')))
		m.append(x)
	m = [complex(*x) for x in m]
	print('python self complex number multiplication', mult(m))
	print('my implemented equation', eq_solver(eq))

while True:
	try:
		main(input('equation:'))
	except Exception as e:
		print(e)
