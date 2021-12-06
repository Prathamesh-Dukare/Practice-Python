os=['Windows','mac','linux']
guys=['Pawan','Shiv','sairaj']
for i in range(0,len(guys)):
	template='{} uses {}'
	print(template.format(guys[i],os[i]))