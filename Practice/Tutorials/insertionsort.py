L=[1,3,7,4,2]
for i in range(len(L)):
	j=i-1
	k=L[i]
	while(j>=0 and k<L[j]):
		L[j+1]=L[j]	
		j-=1
	else:
		L[j+1]=k
print(L)