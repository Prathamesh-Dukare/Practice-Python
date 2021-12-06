a=int(input('Enter Your Birth year\n'))
isbirth=False
isyear=False
if(1899<a<2121):
	isbirth=True
elif(a<1900 or a>2120):
	print('Enter a valid year')


if(isbirth):
	b=int(input('Enter Year at which wanna know your age : \n'))
	if(b>a):
		isyear=True
	elif(a>b):
		print('Enter a Valid year')
		
if(isbirth and isyear):
	print('Your Age at {} will be {}'.format(b,b-a))

	

		