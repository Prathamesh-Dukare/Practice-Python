class war:
	def __init__(self,name):
		self.name=name
		self.health=100
		self.damage=10
	def __str__(self):
		return '{} has health= {} '.format(self.name,self.health)
	def attack(self,defender):
		defender.health-=10
		return '{} attacked {}\n'.format(self.name,defender.name),'And {} loosed {} points'.format(defender.name, defender.damage)
		
hero=war('hero')
villen=war('villen')
hero.attack(villen)
print(villen.health)
print(villen)
