class war:

    def __init__(self,name):
        self.name=name
        self.health=100
        self.damage=10

    def attack(self,other):
        other.health-=10
        self.health+=10
        print(f"{self.name} attacked {other.name}")


    def __str__(self):
        return f"{self.name} has health {self.health}"
hero=war("Hero")
villen=war("Villen")

hero.attack(villen)
print(villen)

























