A = [[1, 2], [4, 5]]


def rotate(matrix):
	matrix.reverse()
	return [[matrix[y][x] for y in range(len(matrix[0]))]
									for x in range(len(matrix))]


for line in A:
	print(line)
print('#' * len(A[0])**2)
print(90)
m = rotate(A)
for line in m:
	print(line)
print('#' * len(A[0])**2)
m=A
for n in range(3):
	m=rotate(m)
for line in m:
	print(line)
print('#' * len(A[0])**2)



