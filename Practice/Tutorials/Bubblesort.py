#buubble sorting algorithm
L=[1,3,8,4,2]

if(__name__=='__main__'):
	for j in range(1,len(L)):
		for i in range(len(L)-1):
			if(L[j]<L[i]):
				L[j],L[i]=L[i],L[j]
	print(L)
'''
L=[1,3,8,4,2]
for i in range(len(L)):
	for j in range(len(L)-i
		if(L[j]>L[j+1]):
			L[j],L[j+1]=L[j+1],L[j]
print(L)'''