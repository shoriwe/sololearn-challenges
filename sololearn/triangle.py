class Triangle:
	def __init__(self, form: (1, 2, 3)):
		self.a = form[0]
		self.b = form[1]
		self.c = form[2]
		self.real = self.is_real()

	def is_real(self):
		a, b, c = self.a, self.b, self.c
		real = True
		real = real and (a + b > c)
		real = real and (a + c > b)
		real = real and (b + c > a)
		return real


#Determine if a triangle can be formed
#1,2,2 = True
#1,4,4 = False
triangle = tuple(
	float(x)
	for x in input('example input 1,1,2\nyour input:').strip(' ').split(','))

t = Triangle(triangle)
if t.real:
	print('Can be formed')
else:
	print("Can't be formed")

