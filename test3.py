def fib_generator(n):
	first=0
	second=1
	tmp=0
	for i in range(0,n):
		yield first
		tmp=first+second
		first=second
		second=tmp

		

		

fb=fib_generator(8)
print(list(fib_generator(9)))
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))
