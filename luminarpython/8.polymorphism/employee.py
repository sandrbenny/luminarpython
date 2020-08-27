class employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def printVal(self):
        print(self.id)
        print(self.name)
        print(self.sal)
    def __str__(self):
       #return self.name#at a imeonly one return works.
       return str(self.id)+self.name+str(self.sal)

obj1=employee(1011,"ajay",25000)
obj2=employee(1012,"ajaya",30000)
obj3=employee(1013,"ajaneesh",35000)
#print(obj)#<__main__.employee object at 0x012DB178> this will be output.works an method def __ str__(self).there is a object class which works when we are cfreating a object.we have to override that method.soinclude our method __str__

ls=[]
ls.append(obj1)
ls.append(obj2)
ls.append(obj3)

for emp in ls:
    if(emp.sal>32000):
        print(emp.name)