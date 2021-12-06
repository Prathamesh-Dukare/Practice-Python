def result(**args):
	for key,value in args.items():
		print(key,value)
marks={'jd':20,'jk':30,'kj':60,'pawan':100}
result(**marks)