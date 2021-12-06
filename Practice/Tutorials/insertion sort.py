L=[1,3,7,4,9]
for i in range(len(L)):
	k=L[i]
	j=i-1
	
	while(j>=0 and k<L[j]):
		L[j+1]=L[j]
		j-=1
	else:
		L[j+1]=k
print('sorted list',L)
		