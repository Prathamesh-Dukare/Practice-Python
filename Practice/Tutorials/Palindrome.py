def pali(str):
	revstr=str[::-1]
	if(str==revstr):
		print(str,'is Palindrome')
	else:
		print(str,'isnt Palindrome')
i=pali(input('Enter String to ckeck'))