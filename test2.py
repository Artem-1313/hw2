class ReverseIter:
	def __init__(self, l):
		self.l=l
		self.counter=len(self.l)

	def __iter__(self):
		return self

	def __next__(self):
		
		while self.counter > 0:
			self.counter=self.counter-1
			return self.l[self.counter]
		else:
			raise StopIteration

r=ReverseIter([1,2,3,8,9,88])

print(r.__next__())
print(r.__next__())
print("---------------")
s=ReverseIter("hello")
print(s.__next__())
print(s.__next__())
