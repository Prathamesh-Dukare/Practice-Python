N=int(input('Enter'))
print('Prime numbers are')
num=2
if num<=N:
	for i in range(2,N+1):
		for j in range(2,i):
			if i%j==0:
				break
		else:
			print(i,end=' ')