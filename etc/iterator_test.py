

class Iterator(object):
	def __init__(self, xs):
		self.xs = xs

	def __iter__(self):
		return self
	
	def __next__(self):
		if self.xs:
			return self.xs.pop(0)
		else:
			raise StopIteration

for i in Iterator([0, 1, 2]):
	print(i)

itrtr = Iterator([3, 4, 5, 6])

print(next(itrtr))
print(next(itrtr))
print(next(itrtr))

