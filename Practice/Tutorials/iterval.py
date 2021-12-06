def gen(n):
	for i in range(n):
		yield i
obj=gen(10)

iterl=iter('Duke')
print(next(iterl))