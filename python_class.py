
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def Name(self):
		print("Hello. My name is %s" % self.name)
	def Age(self):
		print("My age is %s" % self.age)


if __name__ == '__main__':
	human = Person("jungwoo", "29")
	human.Name()
	human.Age()

