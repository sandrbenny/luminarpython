class Employee:
    def __init__(self,id,name,des,sal):
        self.id=id
        self.name=name
        self.des=des
        self.sal=sal
    def printvalues(self):
        print("id:",self.id)
        print("name:",self.name)
        print("designation:",self.des)
        print("salary:",self.sal)
    def __str__(self):
        return self.name

lst=[]
f=open("edetails","r")
for data in f:
    values=data.rstrip("/n").split(",")
    id=values[0]
    name=values[1]
    des=values[2]
    sal=values[3]
    ob=Employee(id,name,des,sal)
    ob.printvalues()
    print(lst)
    lst.append(ob)
   

uppername=list(map(lambda ob:ob.name.upper(),lst))
salarylist=list(map(lambda ob:ob.salary+5000,lst))
maxsalary=filter(lambda ob:ob.salary>25000,lst)

print(uppername)
print(salarylist)
print(maxsalary)
