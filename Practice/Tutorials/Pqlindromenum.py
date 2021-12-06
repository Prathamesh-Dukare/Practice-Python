num=int(input('Enter a no_'))
temp=num #121
rev=0

while(num>0):
	dig=num%10
	rev=rev*10+dig
	num=num//10
#	print(dig,rev,num)
if(temp==rev):
	print(temp,'is palindrome')
else:
	print(temp,'is not palindrome')	
	