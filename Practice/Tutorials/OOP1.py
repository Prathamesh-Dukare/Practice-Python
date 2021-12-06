class employee:
    num=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        employee.num+=1
        
    def __add__(self,other):
        sum=self.salary+other.salary
        return sum
    def __str__(self):
        return f"in str{self.fname},{self.lname},{self.salary}"
    def __repr__(self):
        return f"in repr{self.fname},{self.lname},{self.salary}"
    def info(self, other):
        a=self.salary+other.salary
        print(a)
pawan=employee("prathamesh","dukare",95000)
rutik=employee('rutik',"ingale",90000)

print(pawan)
