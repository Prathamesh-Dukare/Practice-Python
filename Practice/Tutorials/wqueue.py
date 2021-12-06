a=[]
def push(element):
	a.append(element)
def pop():
	if(len(a)<=0):
		print('Empty List')
	else:
		return a.pop(0)
def display():
	print(a)
push(1)
display()
push(2)
display()
push(3)
display()
pop()
display()
pop()
display()
pop()
display()
