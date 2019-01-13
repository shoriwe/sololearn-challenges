class Stack:
	def __init__(self, data):
		self._items = data

	def __len__(self):
		return len(self._items)

	def __repr__(self):
		return self._items

	def __str__(self):
		return str(self.__repr__())

	def pop(self):
		self._items.remove(self._items[-1])

	def push(self, item):
		self._items.append(item)

	def top(self):
		return self._items[0]


class Queue:
	def __init__(self, data):
		self.items = data

	def __repr__(self):
		return self.items

	def __str__(self):
		return str(self.__repr__())

	def __len__(self):
		return len(self.items)

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		self.items.pop()


class Mutant_dict:
	def __init__(self):
		self.keys = []
		self.values = []

	def __getitem__(self, key):
		return self.getList(key)

	def __setitem__(self, key, value):
		self.keys.append(key)
		self.values.append(value)

	def __contains__(self, key):
		return key in self.keys

	def __delitem__(self, key):
		self.remove(key)

	def __repr__(self):
		out = {}
		for number, key in enumerate(self.keys):
			if key not in out:
				out[key] = [self.values[number]]
			else:
				out[key].append(self.values[number])
		return out

	def __str__(self):
		return str(self.__repr__())

	def __len__(self):
		return self.count()

	def insert(self, key, value):
		self[key] = value

	def remove(self, key):
		numbers = []
		dict_values = {n: v for n, v in enumerate(self.values)}
		result_value = []

		for n, k in enumerate(self.keys):
			if k == key:
				numbers.append(n)
		while True:
			try:
				self.keys.remove(key)
			except:
				break

		for key in dict_values:
			if key not in numbers:
				result_value.append(dict_values[key])
		self.values = result_value

	def merge(self, other_dict):
		try:
			self.keys += other_dict.keys
			self.values += other_dict.values
		except:
			print(1837)
			self.keys += other_dict.keys()
			self.values += other_dict.values()

	def count(self):
		return len(self.__repr__())

	def getList(self, key):
		return self.__repr__()[key]

	def find(self, key):
		return key in self.keys

	def toQueue(self):
		return Queue(list(zip(self.keys, self.values)))

	def toStack(self):
		data = list(zip(self.keys, self.values))
		data.reverse()
		return Stack(data)


x = Mutant_dict()
y = Mutant_dict()

y['1'] = 2

x['chango'] = 2
x['perro'] = 3
x['gato'] = 2
x['lego'] = 1
x['lego'] = 10

print('mutant array x', x, sep='\n')
print('mutant array y', y, sep='\n')

r = x.find('chango')
lst = x.getList('chango')

print('chango in hash', r, sep='\n')
print('key chango have this values', lst, sep='\n')
x.remove('chango')
print('mutant array x after remove', x, sep='\n')
x.insert(1, 3)
x.merge(y)
print('hash x after merge', x, sep='\n')
lenght = x.count()
print('len(x)', lenght, sep='\n')

q = x.toQueue()
s = x.toStack()

print('queue', q, sep='\n')
print('stack', s, sep='\n')

